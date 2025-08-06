"""
用戶業務邏輯服務
處理用戶相關的業務邏輯
"""

from typing import List, Optional, Dict, Any
from fastapi import HTTPException
from ..models import User, UserCreate, UserUpdate
from ..database.memory_db import db
from src.core import app_logger


class UserService:
    """用戶服務類"""

    @staticmethod
    def get_all_users() -> List[Dict[str, Any]]:
        """獲取所有用戶"""
        app_logger.debug("獲取所有用戶")
        users = db.get_all_users()
        app_logger.info(f"返回 {len(users)} 個用戶")
        return users

    @staticmethod
    def get_user_by_id(user_id: int) -> Dict[str, Any]:
        """根據 ID 獲取用戶"""
        app_logger.debug(f"獲取用戶: ID={user_id}")
        user = db.get_user_by_id(user_id)
        if not user:
            app_logger.warning(f"用戶未找到: ID={user_id}")
            raise HTTPException(status_code=404, detail="用戶未找到")

        app_logger.info(f"找到用戶: {user['username']}")
        return user

    @staticmethod
    def create_user(user_data: UserCreate) -> Dict[str, Any]:
        """創建新用戶"""
        app_logger.info(f"創建新用戶: {user_data.username}")

        # 檢查用戶名是否已存在
        existing_user = db.get_user_by_username(user_data.username)
        if existing_user:
            app_logger.warning(f"用戶名已存在: {user_data.username}")
            raise HTTPException(status_code=400, detail="用戶名已存在")

        try:
            user_dict = user_data.dict()
            created_user = db.create_user(user_dict)

            app_logger.info(
                f"用戶創建成功: ID={created_user['id']}, 用戶名={user_data.username}"
            )
            return created_user

        except Exception as e:
            app_logger.error(f"創建用戶失敗: {e}")
            raise HTTPException(status_code=500, detail="創建用戶時發生錯誤")

    @staticmethod
    def update_user(user_id: int, user_data: UserUpdate) -> Dict[str, Any]:
        """更新用戶"""
        app_logger.info(f"更新用戶: ID={user_id}")

        # 檢查用戶是否存在
        existing_user = db.get_user_by_id(user_id)
        if not existing_user:
            app_logger.warning(f"要更新的用戶未找到: ID={user_id}")
            raise HTTPException(status_code=404, detail="用戶未找到")

        # 如果要更新用戶名，檢查是否與其他用戶衝突
        if user_data.username and user_data.username != existing_user["username"]:
            conflicting_user = db.get_user_by_username(user_data.username)
            if conflicting_user and conflicting_user["id"] != user_id:
                app_logger.warning(f"用戶名已被其他用戶使用: {user_data.username}")
                raise HTTPException(status_code=400, detail="用戶名已存在")

        try:
            # 只更新提供的字段
            update_data = user_data.dict(exclude_unset=True)

            # 合併現有數據和更新數據
            updated_data = {**existing_user, **update_data}

            updated_user = db.update_user(user_id, updated_data)

            app_logger.info(f"用戶更新成功: ID={user_id}")
            return updated_user

        except Exception as e:
            app_logger.error(f"更新用戶失敗: {e}")
            raise HTTPException(status_code=500, detail="更新用戶時發生錯誤")

    @staticmethod
    def delete_user(user_id: int) -> Dict[str, str]:
        """刪除用戶"""
        app_logger.info(f"刪除用戶: ID={user_id}")

        deleted_user = db.delete_user(user_id)
        if not deleted_user:
            app_logger.warning(f"要刪除的用戶未找到: ID={user_id}")
            raise HTTPException(status_code=404, detail="用戶未找到")

        app_logger.info(f"用戶刪除成功: {deleted_user['username']}")
        return {"message": f"用戶 '{deleted_user['username']}' 已成功刪除"}
