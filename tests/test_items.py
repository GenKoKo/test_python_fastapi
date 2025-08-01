"""
商品 API 測試
測試商品相關的 API 端點
"""

import pytest
from fastapi.testclient import TestClient


def test_get_all_items_empty(client: TestClient, clean_db):
    """測試獲取空商品列表"""
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item(client: TestClient, clean_db, sample_item):
    """測試創建商品"""
    response = client.post("/items/", json=sample_item)
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == sample_item["name"]
    assert data["price"] == sample_item["price"]
    assert "id" in data


def test_get_item_by_id(client: TestClient, clean_db, sample_item):
    """測試根據 ID 獲取商品"""
    # 先創建商品
    create_response = client.post("/items/", json=sample_item)
    item_id = create_response.json()["id"]
    
    # 獲取商品
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == sample_item["name"]


def test_get_nonexistent_item(client: TestClient, clean_db):
    """測試獲取不存在的商品"""
    response = client.get("/items/999")
    assert response.status_code == 404


def test_update_item(client: TestClient, clean_db, sample_item):
    """測試更新商品"""
    # 先創建商品
    create_response = client.post("/items/", json=sample_item)
    item_id = create_response.json()["id"]
    
    # 更新商品
    update_data = {"name": "更新後的商品", "price": 200.0}
    response = client.put(f"/items/{item_id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["name"] == "更新後的商品"
    assert data["price"] == 200.0


def test_delete_item(client: TestClient, clean_db, sample_item):
    """測試刪除商品"""
    # 先創建商品
    create_response = client.post("/items/", json=sample_item)
    item_id = create_response.json()["id"]
    
    # 刪除商品
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    
    # 確認商品已被刪除
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404


def test_search_items(client: TestClient, clean_db):
    """測試搜索商品"""
    # 創建測試商品
    items = [
        {"name": "iPhone 15", "description": "蘋果手機", "price": 30000.0, "is_available": True},
        {"name": "Samsung Galaxy", "description": "三星手機", "price": 25000.0, "is_available": True},
        {"name": "iPad", "description": "蘋果平板", "price": 20000.0, "is_available": False}
    ]
    
    for item in items:
        client.post("/items/", json=item)
    
    # 測試關鍵字搜索
    response = client.get("/items/search/?q=iPhone")
    assert response.status_code == 200
    
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["name"] == "iPhone 15"
    
    # 測試價格範圍搜索
    response = client.get("/items/search/?min_price=25000&max_price=35000")
    assert response.status_code == 200
    
    data = response.json()
    assert data["count"] == 2  # iPhone 和 Samsung
    
    # 測試包含不可用商品
    response = client.get("/items/search/?available_only=false")
    assert response.status_code == 200
    
    data = response.json()
    assert data["count"] == 3  # 包含 iPad


def test_create_item_validation(client: TestClient, clean_db):
    """測試商品創建時的數據驗證"""
    # 測試缺少必填字段
    response = client.post("/items/", json={"name": "測試商品"})  # 缺少 price
    assert response.status_code == 422
    
    # 測試無效價格
    response = client.post("/items/", json={"name": "測試商品", "price": -100})
    assert response.status_code == 422
    
    # 測試空名稱
    response = client.post("/items/", json={"name": "", "price": 100})
    assert response.status_code == 422