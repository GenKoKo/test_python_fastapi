"""
商品數據模型
定義商品相關的 Pydantic 模型
"""

from typing import Optional
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """商品基礎模型"""

    name: str = Field(..., description="商品名稱", min_length=1, max_length=100)
    description: Optional[str] = Field(None, description="商品描述", max_length=500)
    price: float = Field(..., description="商品價格", gt=0)
    is_available: bool = Field(True, description="是否可用")


class ItemCreate(ItemBase):
    """創建商品模型"""

    pass


class ItemUpdate(ItemBase):
    """更新商品模型"""

    name: Optional[str] = Field(None, description="商品名稱", min_length=1, max_length=100)
    price: Optional[float] = Field(None, description="商品價格", gt=0)


class Item(ItemBase):
    """商品完整模型（包含 ID）"""

    id: int = Field(..., description="商品 ID")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "iPhone 15",
                "description": "最新款 iPhone",
                "price": 32000.0,
                "is_available": True,
            }
        }
