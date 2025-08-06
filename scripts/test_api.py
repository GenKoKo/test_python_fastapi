#!/usr/bin/env python3
"""
FastAPI 測試腳本
這個腳本演示如何使用 requests 庫與 FastAPI 應用進行交互
"""

import requests
import json
import time

# API 基礎 URL
BASE_URL = "http://127.0.0.1:8000"


def test_api():
    """測試 API 的各種功能"""

    print("🚀 開始測試 FastAPI 應用...")
    print("=" * 50)

    # 1. 測試根路徑
    print("1. 測試根路徑...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"狀態碼: {response.status_code}")
        print(f"響應: {response.json()}")
        print()
    except requests.exceptions.ConnectionError:
        print("❌ 無法連接到 API，請確保服務器正在運行")
        return

    # 2. 測試健康檢查
    print("2. 測試健康檢查...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"狀態碼: {response.status_code}")
    print(f"響應: {response.json()}")
    print()

    # 3. 創建商品
    print("3. 創建商品...")
    items_to_create = [
        {
            "name": "iPhone 15",
            "description": "最新款 iPhone",
            "price": 32000.0,
            "is_available": True,
        },
        {
            "name": "MacBook Pro",
            "description": "專業筆記本電腦",
            "price": 65000.0,
            "is_available": True,
        },
        {
            "name": "AirPods Pro",
            "description": "無線耳機",
            "price": 8000.0,
            "is_available": False,
        },
    ]

    created_items = []
    for item_data in items_to_create:
        response = requests.post(f"{BASE_URL}/items", json=item_data)
        if response.status_code == 200:
            created_item = response.json()
            created_items.append(created_item)
            print(f"✅ 創建商品成功: {created_item['name']} (ID: {created_item['id']})")
        else:
            print(f"❌ 創建商品失敗: {response.text}")
    print()

    # 4. 獲取所有商品
    print("4. 獲取所有商品...")
    response = requests.get(f"{BASE_URL}/items")
    items = response.json()
    print(f"商品總數: {len(items)}")
    for item in items:
        print(
            f"  - {item['name']}: NT${item['price']} ({'可用' if item['is_available'] else '不可用'})"
        )
    print()

    # 5. 獲取特定商品
    if created_items:
        print("5. 獲取特定商品...")
        item_id = created_items[0]["id"]
        response = requests.get(f"{BASE_URL}/items/{item_id}")
        if response.status_code == 200:
            item = response.json()
            print(f"✅ 獲取商品成功: {json.dumps(item, ensure_ascii=False, indent=2)}")
        else:
            print(f"❌ 獲取商品失敗: {response.text}")
        print()

    # 6. 創建用戶
    print("6. 創建用戶...")
    users_to_create = [
        {"username": "alice", "email": "alice@example.com", "full_name": "Alice Wang"},
        {"username": "bob", "email": "bob@example.com", "full_name": "Bob Chen"},
    ]

    for user_data in users_to_create:
        response = requests.post(f"{BASE_URL}/users", json=user_data)
        if response.status_code == 200:
            user = response.json()
            print(f"✅ 創建用戶成功: {user['username']} (ID: {user['id']})")
        else:
            print(f"❌ 創建用戶失敗: {response.text}")
    print()

    # 7. 搜索商品
    print("7. 搜索商品...")
    search_params = {"q": "iPhone", "min_price": 30000, "available_only": True}
    response = requests.get(f"{BASE_URL}/search/items", params=search_params)
    search_result = response.json()
    print(f"搜索結果: {search_result['count']} 個商品")
    for item in search_result["results"]:
        print(f"  - {item['name']}: NT${item['price']}")
    print()

    # 8. 更新商品
    if created_items:
        print("8. 更新商品...")
        item_id = created_items[0]["id"]
        update_data = {
            "name": "iPhone 15 Pro",
            "description": "升級版 iPhone 15",
            "price": 38000.0,
            "is_available": True,
        }
        response = requests.put(f"{BASE_URL}/items/{item_id}", json=update_data)
        if response.status_code == 200:
            updated_item = response.json()
            print(f"✅ 更新商品成功: {updated_item['name']}")
        else:
            print(f"❌ 更新商品失敗: {response.text}")
        print()

    # 9. 獲取統計信息
    print("9. 獲取統計信息...")
    response = requests.get(f"{BASE_URL}/stats")
    stats = response.json()
    print("📊 統計信息:")
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    print()

    # 10. 刪除商品
    if created_items and len(created_items) > 1:
        print("10. 刪除商品...")
        item_id = created_items[-1]["id"]  # 刪除最後一個商品
        response = requests.delete(f"{BASE_URL}/items/{item_id}")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ {result['message']}")
        else:
            print(f"❌ 刪除商品失敗: {response.text}")
        print()

    print("🎉 API 測試完成！")
    print("💡 你可以訪問 http://127.0.0.1:8000/docs 查看交互式 API 文檔")


if __name__ == "__main__":
    test_api()
