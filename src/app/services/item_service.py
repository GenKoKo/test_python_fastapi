"""
商品業務邏輯服務
處理商品相關的業務邏輯
"""

from typing import List, Optional, Dict, Any
from fastapi import HTTPException
from ..models import Item, ItemCreate, ItemUpdate
from ..database.memory_db import db
from src.core import app_logger


class ItemService:
    """商品服務類"""

    @staticmethod
    def get_all_items() -> List[Dict[str, Any]]:
        """獲取所有商品"""
        app_logger.debug("獲取所有商品")
        items = db.get_all_items()
        app_logger.info(f"返回 {len(items)} 個商品")
        return items

    @staticmethod
    def get_item_by_id(item_id: int) -> Dict[str, Any]:
        """根據 ID 獲取商品"""
        app_logger.debug(f"獲取商品: ID={item_id}")
        item = db.get_item_by_id(item_id)
        if not item:
            app_logger.warning(f"商品未找到: ID={item_id}")
            raise HTTPException(status_code=404, detail="商品未找到")

        app_logger.info(f"找到商品: {item['name']}")
        return item

    @staticmethod
    def create_item(item_data: ItemCreate) -> Dict[str, Any]:
        """創建新商品"""
        app_logger.info(f"創建新商品: {item_data.name}")

        try:
            item_dict = item_data.dict()
            created_item = db.create_item(item_dict)

            app_logger.info(f"商品創建成功: ID={created_item['id']}, 名稱={item_data.name}")
            return created_item

        except Exception as e:
            app_logger.error(f"創建商品失敗: {e}")
            raise HTTPException(status_code=500, detail="創建商品時發生錯誤")

    @staticmethod
    def update_item(item_id: int, item_data: ItemUpdate) -> Dict[str, Any]:
        """更新商品"""
        app_logger.info(f"更新商品: ID={item_id}")

        # 檢查商品是否存在
        existing_item = db.get_item_by_id(item_id)
        if not existing_item:
            app_logger.warning(f"要更新的商品未找到: ID={item_id}")
            raise HTTPException(status_code=404, detail="商品未找到")

        try:
            # 只更新提供的字段
            update_data = item_data.dict(exclude_unset=True)

            # 合併現有數據和更新數據
            updated_data = {**existing_item, **update_data}

            updated_item = db.update_item(item_id, updated_data)

            app_logger.info(f"商品更新成功: ID={item_id}")
            return updated_item

        except Exception as e:
            app_logger.error(f"更新商品失敗: {e}")
            raise HTTPException(status_code=500, detail="更新商品時發生錯誤")

    @staticmethod
    def delete_item(item_id: int) -> Dict[str, str]:
        """刪除商品"""
        app_logger.info(f"刪除商品: ID={item_id}")

        deleted_item = db.delete_item(item_id)
        if not deleted_item:
            app_logger.warning(f"要刪除的商品未找到: ID={item_id}")
            raise HTTPException(status_code=404, detail="商品未找到")

        app_logger.info(f"商品刪除成功: {deleted_item['name']}")
        return {"message": f"商品 '{deleted_item['name']}' 已成功刪除"}

    @staticmethod
    def search_items(
        query: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        available_only: bool = True,
    ) -> Dict[str, Any]:
        """搜索商品"""
        app_logger.debug(
            f"搜索商品: query={query}, min_price={min_price}, max_price={max_price}"
        )

        try:
            filtered_items = db.search_items(
                query=query,
                min_price=min_price,
                max_price=max_price,
                available_only=available_only,
            )

            result = {
                "query": query,
                "filters": {
                    "min_price": min_price,
                    "max_price": max_price,
                    "available_only": available_only,
                },
                "results": filtered_items,
                "count": len(filtered_items),
            }

            app_logger.info(f"搜索完成: 找到 {len(filtered_items)} 個商品")
            return result

        except Exception as e:
            app_logger.error(f"搜索商品失敗: {e}")
            raise HTTPException(status_code=500, detail="搜索商品時發生錯誤")
