from fastapi import FastAPI, HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import asyncio
import threading
import time
import requests
import sys

# 導入配置和日誌模組
from config import settings, validate_config, print_config
from logger import app_logger, log_startup, log_shutdown, log_request, log_error

# 驗證配置
try:
    validate_config()
    app_logger.info("✅ 配置驗證通過")
except ValueError as e:
    app_logger.error(f"❌ 配置驗證失敗: {e}")
    sys.exit(1)

# 創建 FastAPI 應用實例（使用配置中的值）
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url
)

# Pydantic 模型定義
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

# 日誌中間件
class LoggingMiddleware(BaseHTTPMiddleware):
    """API 請求日誌中間件"""
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # 記錄請求開始
        app_logger.debug(f"📥 收到請求: {request.method} {request.url}")
        
        try:
            response = await call_next(request)
            
            # 計算處理時間
            process_time = time.time() - start_time
            
            # 記錄請求完成
            log_request(
                method=request.method,
                url=str(request.url),
                status_code=response.status_code,
                duration=process_time
            )
            
            # 添加處理時間到響應頭
            response.headers["X-Process-Time"] = str(process_time)
            
            return response
            
        except Exception as e:
            process_time = time.time() - start_time
            log_error(e, f"處理請求 {request.method} {request.url}")
            
            # 記錄錯誤請求
            app_logger.error(
                f"❌ 請求失敗 - {request.method} {request.url} - 耗時: {process_time:.3f}s"
            )
            raise

# 添加中間件
app.add_middleware(LoggingMiddleware)

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    full_name: Optional[str] = None

# 模擬數據庫
items_db = []
users_db = []
next_item_id = 1
next_user_id = 1

# 根路由
@app.get("/")
async def read_root():
    """歡迎頁面"""
    app_logger.info("📋 訪問根路徑")
    return {
        "message": "歡迎使用 FastAPI 初級入門 API！",
        "docs": settings.docs_url,
        "redoc": settings.redoc_url,
        "version": settings.app_version
    }

# 健康檢查
@app.get("/health")
async def health_check():
    """API 健康檢查"""
    app_logger.debug("🏥 健康檢查請求")
    return {
        "status": "healthy", 
        "message": "API 運行正常",
        "timestamp": time.time(),
        "version": settings.app_version
    }

# ===== 商品相關 API =====

@app.get("/items", response_model=List[Item])
async def get_all_items():
    """獲取所有商品"""
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """根據 ID 獲取特定商品"""
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="商品未找到")

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    """創建新商品"""
    global next_item_id
    
    app_logger.info(f"📦 創建新商品: {item.name}")
    
    try:
        item_dict = item.dict()
        item_dict["id"] = next_item_id
        next_item_id += 1
        items_db.append(item_dict)
        
        app_logger.info(f"✅ 商品創建成功: ID={item_dict['id']}, 名稱={item.name}")
        return item_dict
        
    except Exception as e:
        app_logger.error(f"❌ 創建商品失敗: {e}")
        raise HTTPException(status_code=500, detail="創建商品時發生錯誤")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """更新商品信息"""
    for i, existing_item in enumerate(items_db):
        if existing_item["id"] == item_id:
            item_dict = item.dict()
            item_dict["id"] = item_id
            items_db[i] = item_dict
            return item_dict
    raise HTTPException(status_code=404, detail="商品未找到")

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """刪除商品"""
    app_logger.info(f"🗑️  嘗試刪除商品: ID={item_id}")
    
    for i, item in enumerate(items_db):
        if item["id"] == item_id:
            deleted_item = items_db.pop(i)
            app_logger.info(f"✅ 商品刪除成功: {deleted_item['name']}")
            return {"message": f"商品 '{deleted_item['name']}' 已成功刪除"}
    
    app_logger.warning(f"⚠️  商品未找到: ID={item_id}")
    raise HTTPException(status_code=404, detail="商品未找到")

# ===== 用戶相關 API =====

@app.get("/users", response_model=List[User])
async def get_all_users():
    """獲取所有用戶"""
    return users_db

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """根據 ID 獲取特定用戶"""
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="用戶未找到")

@app.post("/users", response_model=User)
async def create_user(user: User):
    """創建新用戶"""
    global next_user_id
    # 檢查用戶名是否已存在
    for existing_user in users_db:
        if existing_user["username"] == user.username:
            raise HTTPException(status_code=400, detail="用戶名已存在")
    
    user_dict = user.dict()
    user_dict["id"] = next_user_id
    next_user_id += 1
    users_db.append(user_dict)
    return user_dict

# ===== 查詢參數示例 =====

@app.get("/search/items")
async def search_items(
    q: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    available_only: bool = True
):
    """搜索商品（支持查詢參數）"""
    filtered_items = items_db.copy()
    
    if available_only:
        filtered_items = [item for item in filtered_items if item["is_available"]]
    
    if q:
        filtered_items = [
            item for item in filtered_items 
            if q.lower() in item["name"].lower() or 
               (item["description"] and q.lower() in item["description"].lower())
        ]
    
    if min_price is not None:
        filtered_items = [item for item in filtered_items if item["price"] >= min_price]
    
    if max_price is not None:
        filtered_items = [item for item in filtered_items if item["price"] <= max_price]
    
    return {
        "query": q,
        "filters": {
            "min_price": min_price,
            "max_price": max_price,
            "available_only": available_only
        },
        "results": filtered_items,
        "count": len(filtered_items)
    }

# ===== 統計和其他功能 =====

@app.get("/stats")
async def get_stats():
    """獲取 API 統計信息"""
    total_items = len(items_db)
    available_items = len([item for item in items_db if item["is_available"]])
    total_users = len(users_db)
    
    if total_items > 0:
        avg_price = sum(item["price"] for item in items_db) / total_items
        max_price = max(item["price"] for item in items_db)
        min_price = min(item["price"] for item in items_db)
    else:
        avg_price = max_price = min_price = 0
    
    return {
        "items": {
            "total": total_items,
            "available": available_items,
            "unavailable": total_items - available_items,
            "price_stats": {
                "average": round(avg_price, 2),
                "maximum": max_price,
                "minimum": min_price
            }
        },
        "users": {
            "total": total_users
        }
    }

# ===== 啟動時測試功能 =====

def populate_sample_data():
    """填充示例數據（僅在啟動時執行一次）"""
    global next_item_id, next_user_id
    
    # 檢查配置是否啟用示例數據
    if not settings.populate_sample_data:
        app_logger.info("⏭️  跳過示例數據填充（配置已禁用）")
        return
    
    # 檢查是否已有數據，避免重複添加
    if len(items_db) > 0 or len(users_db) > 0:
        app_logger.info("⏭️  示例數據已存在，跳過填充")
        return
    
    app_logger.info("📊 開始填充示例數據...")
    
    try:
        # 添加示例商品
        sample_items = [
            {
                "id": 1,
                "name": "iPhone 15",
                "description": "最新款 iPhone",
                "price": 32000.0,
                "is_available": True
            },
            {
                "id": 2,
                "name": "MacBook Pro",
                "description": "專業筆記本電腦",
                "price": 65000.0,
                "is_available": True
            },
            {
                "id": 3,
                "name": "AirPods Pro",
                "description": "無線耳機",
                "price": 8000.0,
                "is_available": False
            }
        ]
        
        # 添加示例用戶
        sample_users = [
            {
                "id": 1,
                "username": "alice",
                "email": "alice@example.com",
                "full_name": "Alice Wang"
            },
            {
                "id": 2,
                "username": "bob",
                "email": "bob@example.com",
                "full_name": "Bob Chen"
            }
        ]
        
        items_db.extend(sample_items)
        users_db.extend(sample_users)
        next_item_id = 4
        next_user_id = 3
        
        app_logger.info(f"✅ 示例數據填充完成: {len(sample_items)} 個商品, {len(sample_users)} 個用戶")
        
    except Exception as e:
        app_logger.error(f"❌ 示例數據填充失敗: {e}")
        raise

def run_api_tests():
    """在服務器啟動後運行 API 測試"""
    BASE_URL = f"http://{settings.host}:{settings.port}"
    
    def wait_for_server():
        """等待服務器啟動"""
        max_attempts = 30
        app_logger.info("⏳ 等待服務器啟動...")
        
        for attempt in range(max_attempts):
            try:
                response = requests.get(f"{BASE_URL}/health", timeout=1)
                if response.status_code == 200:
                    app_logger.info("✅ 服務器已就緒")
                    return True
            except requests.exceptions.RequestException:
                pass
            time.sleep(1)
        
        app_logger.error("❌ 服務器啟動超時")
        return False
    
    def run_tests():
        """運行測試"""
        app_logger.info("🧪 開始 API 自動測試...")
        
        if not wait_for_server():
            app_logger.error("❌ 服務器啟動超時，跳過測試")
            return
        
        test_results = []
        
        try:
            # 1. 測試根路徑
            app_logger.info("1️⃣ 測試根路徑...")
            response = requests.get(f"{BASE_URL}/")
            test_results.append(("根路徑", response.status_code == 200))
            
            # 2. 測試健康檢查
            app_logger.info("2️⃣ 測試健康檢查...")
            response = requests.get(f"{BASE_URL}/health")
            test_results.append(("健康檢查", response.status_code == 200))
            
            # 3. 測試獲取商品
            app_logger.info("3️⃣ 測試獲取商品...")
            response = requests.get(f"{BASE_URL}/items")
            items = response.json()
            test_results.append(("獲取商品", response.status_code == 200))
            app_logger.info(f"   找到 {len(items)} 個商品")
            
            # 4. 測試獲取用戶
            app_logger.info("4️⃣ 測試獲取用戶...")
            response = requests.get(f"{BASE_URL}/users")
            users = response.json()
            test_results.append(("獲取用戶", response.status_code == 200))
            app_logger.info(f"   找到 {len(users)} 個用戶")
            
            # 5. 測試搜索功能
            app_logger.info("5️⃣ 測試搜索功能...")
            response = requests.get(f"{BASE_URL}/search/items?q=iPhone")
            search_result = response.json()
            test_results.append(("搜索功能", response.status_code == 200))
            app_logger.info(f"   搜索結果: {search_result['count']} 個商品")
            
            # 6. 測試統計功能
            app_logger.info("6️⃣ 測試統計功能...")
            response = requests.get(f"{BASE_URL}/stats")
            stats = response.json()
            test_results.append(("統計功能", response.status_code == 200))
            app_logger.info(f"   統計: {stats['items']['total']} 商品, {stats['users']['total']} 用戶")
            
            # 測試結果總結
            passed_tests = sum(1 for _, result in test_results if result)
            total_tests = len(test_results)
            
            if passed_tests == total_tests:
                app_logger.info(f"🎉 所有測試通過！({passed_tests}/{total_tests})")
            else:
                app_logger.warning(f"⚠️  部分測試失敗: {passed_tests}/{total_tests}")
            
            app_logger.info("💡 你可以訪問以下地址:")
            app_logger.info(f"   📖 API 文檔: {BASE_URL}{settings.docs_url}")
            app_logger.info(f"   📚 ReDoc: {BASE_URL}{settings.redoc_url}")
            
        except Exception as e:
            app_logger.error(f"❌ 測試過程中出錯: {e}")
    
    # 在新線程中運行測試，避免阻塞服務器
    test_thread = threading.Thread(target=run_tests, daemon=True)
    test_thread.start()

# FastAPI 事件處理
@app.on_event("startup")
async def startup_event():
    """應用啟動時執行"""
    log_startup()
    
    # 打印配置信息（如果是調試模式）
    if settings.debug:
        print_config()
    
    # 填充示例數據
    populate_sample_data()
    
    # 啟動自動測試（如果啟用）
    if settings.enable_auto_test:
        app_logger.info(f"🧪 將在 {settings.test_delay} 秒後啟動自動測試")
        
        def delayed_test():
            time.sleep(settings.test_delay)
            run_api_tests()
        
        test_thread = threading.Thread(target=delayed_test, daemon=True)
        test_thread.start()
    else:
        app_logger.info("⏭️  自動測試已禁用")

@app.on_event("shutdown")
async def shutdown_event():
    """應用關閉時執行"""
    log_shutdown()
    app_logger.info(f"📊 最終統計: {len(items_db)} 個商品, {len(users_db)} 個用戶")
# 運行服務器
if __name__ == "__main__":
    app_logger.info("🌟 啟動 FastAPI 開發服務器...")
    
    if settings.enable_auto_test:
        app_logger.info("📝 注意: 服務器啟動後會自動運行 API 測試")
    
    # 使用配置中的值
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.lower()
    )