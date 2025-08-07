"""
用戶數據模型
定義用戶相關的 Pydantic 模型
"""

from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    """用戶基礎模型"""

    username: str = Field(..., description="用戶名", min_length=3, max_length=50)
    email: str = Field(..., description="電子郵件")
    full_name: Optional[str] = Field(None, description="全名", max_length=100)


class UserCreate(UserBase):
    """創建用戶模型"""

    pass


class UserUpdate(BaseModel):
    """更新用戶模型"""

    username: Optional[str] = Field(
        None, description="用戶名", min_length=3, max_length=50
    )
    email: Optional[str] = Field(None, description="電子郵件")
    full_name: Optional[str] = Field(None, description="全名", max_length=100)


class User(UserBase):
    """用戶完整模型（包含 ID）"""

    id: int = Field(..., description="用戶 ID")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "alice",
                "email": "alice@example.com",
                "full_name": "Alice Wang",
            }
        }
