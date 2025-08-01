"""
用戶路由
處理用戶相關的 API 端點
"""

from typing import List
from fastapi import APIRouter
from ..models import User, UserCreate, UserUpdate
from ..services import UserService

router = APIRouter(
    prefix="/users",
    tags=["用戶管理"],
    responses={404: {"description": "用戶未找到"}}
)


@router.get("/", response_model=List[User], summary="獲取所有用戶")
async def get_all_users():
    """
    獲取所有用戶列表
    
    返回系統中所有用戶的詳細信息
    """
    return UserService.get_all_users()


@router.get("/{user_id}", response_model=User, summary="獲取特定用戶")
async def get_user(user_id: int):
    """
    根據 ID 獲取特定用戶
    
    - **user_id**: 用戶的唯一標識符
    """
    return UserService.get_user_by_id(user_id)


@router.post("/", response_model=User, summary="創建新用戶", status_code=201)
async def create_user(user: UserCreate):
    """
    創建新用戶
    
    - **username**: 用戶名（必填，3-50 字符，必須唯一）
    - **email**: 電子郵件（必填）
    - **full_name**: 全名（可選，最多 100 字符）
    """
    return UserService.create_user(user)


@router.put("/{user_id}", response_model=User, summary="更新用戶")
async def update_user(user_id: int, user: UserUpdate):
    """
    更新用戶信息
    
    - **user_id**: 要更新的用戶 ID
    - 只需提供要更新的字段
    - 用戶名必須保持唯一性
    """
    return UserService.update_user(user_id, user)


@router.delete("/{user_id}", summary="刪除用戶")
async def delete_user(user_id: int):
    """
    刪除用戶
    
    - **user_id**: 要刪除的用戶 ID
    """
    return UserService.delete_user(user_id)