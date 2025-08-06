"""
商品路由
處理商品相關的 API 端點
"""

from typing import List, Optional
from fastapi import APIRouter, Query
from ..models import Item, ItemCreate, ItemUpdate
from ..services import ItemService

router = APIRouter(
    prefix="/items", tags=["商品管理"], responses={404: {"description": "商品未找到"}}
)


@router.get("/", response_model=List[Item], summary="獲取所有商品")
async def get_all_items():
    """
    獲取所有商品列表

    返回系統中所有商品的詳細信息
    """
    return ItemService.get_all_items()


@router.get("/{item_id}", response_model=Item, summary="獲取特定商品")
async def get_item(item_id: int):
    """
    根據 ID 獲取特定商品

    - **item_id**: 商品的唯一標識符
    """
    return ItemService.get_item_by_id(item_id)


@router.post("/", response_model=Item, summary="創建新商品", status_code=201)
async def create_item(item: ItemCreate):
    """
    創建新商品

    - **name**: 商品名稱（必填）
    - **description**: 商品描述（可選）
    - **price**: 商品價格（必填，必須大於 0）
    - **is_available**: 是否可用（默認為 true）
    """
    return ItemService.create_item(item)


@router.put("/{item_id}", response_model=Item, summary="更新商品")
async def update_item(item_id: int, item: ItemUpdate):
    """
    更新商品信息

    - **item_id**: 要更新的商品 ID
    - 只需提供要更新的字段
    """
    return ItemService.update_item(item_id, item)


@router.delete("/{item_id}", summary="刪除商品")
async def delete_item(item_id: int):
    """
    刪除商品

    - **item_id**: 要刪除的商品 ID
    """
    return ItemService.delete_item(item_id)


@router.get("/search/", summary="搜索商品")
async def search_items(
    q: Optional[str] = Query(None, description="搜索關鍵字"),
    min_price: Optional[float] = Query(None, description="最低價格", ge=0),
    max_price: Optional[float] = Query(None, description="最高價格", ge=0),
    available_only: bool = Query(True, description="只顯示可用商品"),
):
    """
    搜索商品

    支持多種搜索條件：
    - **q**: 在商品名稱和描述中搜索關鍵字
    - **min_price**: 最低價格篩選
    - **max_price**: 最高價格篩選
    - **available_only**: 是否只顯示可用商品
    """
    return ItemService.search_items(
        query=q, min_price=min_price, max_price=max_price, available_only=available_only
    )
