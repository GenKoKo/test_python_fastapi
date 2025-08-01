"""
pytest 配置文件
提供測試的共用配置和 fixtures
"""

import sys
from pathlib import Path

# 添加項目根目錄到 Python 路徑
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
from fastapi.testclient import TestClient
from src.app.main import app
from src.app.database.memory_db import db


@pytest.fixture
def client():
    """創建測試客戶端"""
    return TestClient(app)


@pytest.fixture
def clean_db():
    """清理數據庫的 fixture"""
    # 測試前清理數據庫
    db.clear_all_data()
    yield
    # 測試後清理數據庫
    db.clear_all_data()


@pytest.fixture
def sample_item():
    """示例商品數據"""
    return {
        "name": "測試商品",
        "description": "這是一個測試商品",
        "price": 100.0,
        "is_available": True
    }


@pytest.fixture
def sample_user():
    """示例用戶數據"""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    }