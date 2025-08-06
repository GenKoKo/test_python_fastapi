"""
用戶 API 測試
測試用戶相關的 API 端點
"""

import pytest
from fastapi.testclient import TestClient


def test_get_all_users_empty(client: TestClient, clean_db):
    """測試獲取空用戶列表"""
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_user(client: TestClient, clean_db, sample_user):
    """測試創建用戶"""
    response = client.post("/users/", json=sample_user)
    assert response.status_code == 201

    data = response.json()
    assert data["username"] == sample_user["username"]
    assert data["email"] == sample_user["email"]
    assert "id" in data


def test_get_user_by_id(client: TestClient, clean_db, sample_user):
    """測試根據 ID 獲取用戶"""
    # 先創建用戶
    create_response = client.post("/users/", json=sample_user)
    user_id = create_response.json()["id"]

    # 獲取用戶
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == user_id
    assert data["username"] == sample_user["username"]


def test_get_nonexistent_user(client: TestClient, clean_db):
    """測試獲取不存在的用戶"""
    response = client.get("/users/999")
    assert response.status_code == 404


def test_create_duplicate_username(client: TestClient, clean_db, sample_user):
    """測試創建重複用戶名"""
    # 創建第一個用戶
    client.post("/users/", json=sample_user)

    # 嘗試創建相同用戶名的用戶
    response = client.post("/users/", json=sample_user)
    assert response.status_code == 400


def test_update_user(client: TestClient, clean_db, sample_user):
    """測試更新用戶"""
    # 先創建用戶
    create_response = client.post("/users/", json=sample_user)
    user_id = create_response.json()["id"]

    # 更新用戶
    update_data = {"full_name": "Updated Name", "email": "updated@example.com"}
    response = client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200

    data = response.json()
    assert data["full_name"] == "Updated Name"
    assert data["email"] == "updated@example.com"


def test_delete_user(client: TestClient, clean_db, sample_user):
    """測試刪除用戶"""
    # 先創建用戶
    create_response = client.post("/users/", json=sample_user)
    user_id = create_response.json()["id"]

    # 刪除用戶
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200

    # 確認用戶已被刪除
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404


def test_create_user_validation(client: TestClient, clean_db):
    """測試用戶創建時的數據驗證"""
    # 測試缺少必填字段
    response = client.post("/users/", json={"username": "testuser"})  # 缺少 email
    assert response.status_code == 422

    # 測試用戶名太短
    response = client.post(
        "/users/", json={"username": "ab", "email": "test@example.com"}
    )
    assert response.status_code == 422

    # 測試空用戶名
    response = client.post(
        "/users/", json={"username": "", "email": "test@example.com"}
    )
    assert response.status_code == 422
