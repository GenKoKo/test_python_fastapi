from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import asyncio
import threading
import time
import requests
import sys

# 創建 FastAPI 應用實例
app = FastAPI(
    title="FastAPI 初級入門 API",
    description="這是一個 FastAPI 的基本入門實作，包含常用的 API 操作",
    version="1.0.0"
)

# Pydantic 模型定義
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

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
    return {
        "message": "歡迎使用 FastAPI 初級入門 API！",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# 健康檢查
@app.get("/health")
async def health_check():
    """API 健康檢查"""
    return {"status": "healthy", "message": "API 運行正常"}

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
    item_dict = item.dict()
    item_dict["id"] = next_item_id
    next_item_id += 1
    items_db.append(item_dict)
    return item_dict

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
    for i, item in enumerate(items_db):
        if item["id"] == item_id:
            deleted_item = items_db.pop(i)
            return {"message": f"商品 '{deleted_item['name']}' 已成功刪除"}
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
    
    # 檢查是否已有數據，避免重複添加
    if len(items_db) > 0 or len(users_db) > 0:
        return
    
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
    
    print("✅ 示例數據已加載")

def run_api_tests():
    """在服務器啟動後運行 API 測試"""
    BASE_URL = "http://127.0.0.1:8000"
    
    def wait_for_server():
        """等待服務器啟動"""
        max_attempts = 30
        for attempt in range(max_attempts):
            try:
                response = requests.get(f"{BASE_URL}/health", timeout=1)
                if response.status_code == 200:
                    return True
            except requests.exceptions.RequestException:
                pass
            time.sleep(1)
        return False
    
    def run_tests():
        """運行測試"""
        print("\n" + "="*50)
        print("🧪 開始 API 自動測試...")
        print("="*50)
        
        if not wait_for_server():
            print("❌ 服務器啟動超時，跳過測試")
            return
        
        try:
            # 1. 測試根路徑
            print("1. 測試根路徑...")
            response = requests.get(f"{BASE_URL}/")
            print(f"   狀態碼: {response.status_code} ✅")
            
            # 2. 測試健康檢查
            print("2. 測試健康檢查...")
            response = requests.get(f"{BASE_URL}/health")
            print(f"   狀態碼: {response.status_code} ✅")
            
            # 3. 測試獲取商品
            print("3. 測試獲取商品...")
            response = requests.get(f"{BASE_URL}/items")
            items = response.json()
            print(f"   找到 {len(items)} 個商品 ✅")
            
            # 4. 測試獲取用戶
            print("4. 測試獲取用戶...")
            response = requests.get(f"{BASE_URL}/users")
            users = response.json()
            print(f"   找到 {len(users)} 個用戶 ✅")
            
            # 5. 測試搜索功能
            print("5. 測試搜索功能...")
            response = requests.get(f"{BASE_URL}/search/items?q=iPhone")
            search_result = response.json()
            print(f"   搜索結果: {search_result['count']} 個商品 ✅")
            
            # 6. 測試統計功能
            print("6. 測試統計功能...")
            response = requests.get(f"{BASE_URL}/stats")
            stats = response.json()
            print(f"   統計: {stats['items']['total']} 商品, {stats['users']['total']} 用戶 ✅")
            
            print("\n🎉 所有測試通過！")
            print("💡 你可以訪問以下地址:")
            print(f"   📖 API 文檔: {BASE_URL}/docs")
            print(f"   📚 ReDoc: {BASE_URL}/redoc")
            print("="*50)
            
        except Exception as e:
            print(f"❌ 測試過程中出錯: {e}")
    
    # 在新線程中運行測試，避免阻塞服務器
    test_thread = threading.Thread(target=run_tests, daemon=True)
    test_thread.start()

# FastAPI 事件處理
@app.on_event("startup")
async def startup_event():
    """應用啟動時執行"""
    print("🚀 FastAPI 應用正在啟動...")
    populate_sample_data()
    
    # 延遲啟動測試，確保服務器完全啟動
    def delayed_test():
        time.sleep(2)  # 等待2秒確保服務器完全啟動
        run_api_tests()
    
    test_thread = threading.Thread(target=delayed_test, daemon=True)
    test_thread.start()

@app.on_event("shutdown")
async def shutdown_event():
    """應用關閉時執行"""
    print("👋 FastAPI 應用正在關閉...")

# 運行服務器
if __name__ == "__main__":
    print("🌟 啟動 FastAPI 開發服務器...")
    print("📝 注意: 服務器啟動後會自動運行 API 測試")
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )