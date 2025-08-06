#!/usr/bin/env python3
"""
測試新的模塊化結構
驗證所有模組是否正確導入和工作
"""

import sys
from pathlib import Path

# 添加項目根目錄到 Python 路徑
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_imports():
    """測試所有模組導入"""
    print("🧪 測試模組導入...")
    
    try:
        # 測試配置和日誌
        from src.core import settings, app_logger
        print("✅ 配置和日誌模組導入成功")
        
        # 測試數據模型
        from src.app.models import Item, User, ItemCreate, UserCreate
        print("✅ 數據模型導入成功")
        
        # 測試數據庫
        from src.app.database import MemoryDatabase
        from src.app.database.memory_db import db
        print("✅ 數據庫模組導入成功")
        
        # 測試服務
        from src.app.services import ItemService, UserService
        print("✅ 服務模組導入成功")
        
        # 測試工具
        from src.app.utils import LoggingMiddleware, generate_id
        print("✅ 工具模組導入成功")
        
        # 測試路由
        from src.app.routers import items_router, users_router, stats_router
        print("✅ 路由模組導入成功")
        
        # 測試主應用
        from src.app.main import app
        print("✅ 主應用導入成功")
        
        return True
        
    except Exception as e:
        print(f"❌ 導入失敗: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_database_operations():
    """測試數據庫操作"""
    print("\n🧪 測試數據庫操作...")
    
    try:
        from src.app.database.memory_db import db
        
        # 清理數據庫
        db.clear_all_data()
        
        # 測試商品操作
        item_data = {
            "name": "測試商品",
            "description": "這是測試商品",
            "price": 100.0,
            "is_available": True
        }
        
        created_item = db.create_item(item_data)
        print(f"✅ 創建商品成功: {created_item['name']}")
        
        retrieved_item = db.get_item_by_id(created_item['id'])
        print(f"✅ 獲取商品成功: {retrieved_item['name']}")
        
        # 測試用戶操作
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "full_name": "Test User"
        }
        
        created_user = db.create_user(user_data)
        print(f"✅ 創建用戶成功: {created_user['username']}")
        
        # 測試統計
        stats = db.get_stats()
        print(f"✅ 統計信息: {stats['items']['total']} 商品, {stats['users']['total']} 用戶")
        
        return True
        
    except Exception as e:
        print(f"❌ 數據庫操作失敗: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_services():
    """測試服務層"""
    print("\n🧪 測試服務層...")
    
    try:
        from src.app.services import ItemService, UserService
        from src.app.models import ItemCreate, UserCreate
        from src.app.database.memory_db import db
        
        # 清理數據庫
        db.clear_all_data()
        
        # 測試商品服務
        item_data = ItemCreate(
            name="服務測試商品",
            description="通過服務創建的商品",
            price=200.0,
            is_available=True
        )
        
        created_item = ItemService.create_item(item_data)
        print(f"✅ 商品服務創建成功: {created_item['name']}")
        
        items = ItemService.get_all_items()
        print(f"✅ 商品服務獲取列表: {len(items)} 個商品")
        
        # 測試用戶服務
        user_data = UserCreate(
            username="serviceuser",
            email="service@example.com",
            full_name="Service User"
        )
        
        created_user = UserService.create_user(user_data)
        print(f"✅ 用戶服務創建成功: {created_user['username']}")
        
        users = UserService.get_all_users()
        print(f"✅ 用戶服務獲取列表: {len(users)} 個用戶")
        
        return True
        
    except Exception as e:
        print(f"❌ 服務層測試失敗: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_fastapi_app():
    """測試 FastAPI 應用"""
    print("\n🧪 測試 FastAPI 應用...")
    
    try:
        from fastapi.testclient import TestClient
        from src.app.main import app
        
        client = TestClient(app)
        
        # 測試根路徑
        response = client.get("/")
        assert response.status_code == 200
        print("✅ 根路徑測試通過")
        
        # 測試健康檢查
        response = client.get("/stats/health")
        assert response.status_code == 200
        print("✅ 健康檢查測試通過")
        
        # 測試商品 API
        response = client.get("/items/")
        assert response.status_code == 200
        print("✅ 商品 API 測試通過")
        
        # 測試用戶 API
        response = client.get("/users/")
        assert response.status_code == 200
        print("✅ 用戶 API 測試通過")
        
        return True
        
    except Exception as e:
        print(f"❌ FastAPI 應用測試失敗: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主函數"""
    print("🔧 FastAPI 模塊化結構測試")
    print("=" * 50)
    
    tests = [
        ("模組導入", test_imports),
        ("數據庫操作", test_database_operations),
        ("服務層", test_services),
        ("FastAPI 應用", test_fastapi_app)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} 測試時出錯: {e}")
            results.append((test_name, False))
    
    # 總結
    print("\n" + "=" * 50)
    print("📊 測試結果總結:")
    
    all_passed = True
    for test_name, result in results:
        status = "✅ 通過" if result else "❌ 失敗"
        print(f"   {test_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 所有測試都通過！模塊化結構工作正常。")
        print("💡 現在可以運行: python run.py")
    else:
        print("⚠️  有些測試未通過，請檢查上面的錯誤信息。")
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)