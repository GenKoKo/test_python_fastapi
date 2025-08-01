"""
內存數據庫
提供內存中的數據存儲和操作功能
"""

from typing import List, Dict, Any, Optional
from threading import Lock
from ..models import Item, User


class MemoryDatabase:
    """內存數據庫類"""
    
    def __init__(self):
        """初始化數據庫"""
        self._items: List[Dict[str, Any]] = []
        self._users: List[Dict[str, Any]] = []
        self._next_item_id = 1
        self._next_user_id = 1
        self._lock = Lock()  # 線程安全
    
    # ===== 商品相關操作 =====
    
    def get_all_items(self) -> List[Dict[str, Any]]:
        """獲取所有商品"""
        with self._lock:
            return self._items.copy()
    
    def get_item_by_id(self, item_id: int) -> Optional[Dict[str, Any]]:
        """根據 ID 獲取商品"""
        with self._lock:
            for item in self._items:
                if item["id"] == item_id:
                    return item.copy()
            return None
    
    def create_item(self, item_data: Dict[str, Any]) -> Dict[str, Any]:
        """創建新商品"""
        with self._lock:
            item_data["id"] = self._next_item_id
            self._next_item_id += 1
            self._items.append(item_data.copy())
            return item_data
    
    def update_item(self, item_id: int, item_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """更新商品"""
        with self._lock:
            for i, item in enumerate(self._items):
                if item["id"] == item_id:
                    item_data["id"] = item_id
                    self._items[i] = item_data.copy()
                    return item_data
            return None
    
    def delete_item(self, item_id: int) -> Optional[Dict[str, Any]]:
        """刪除商品"""
        with self._lock:
            for i, item in enumerate(self._items):
                if item["id"] == item_id:
                    return self._items.pop(i)
            return None
    
    def search_items(self, 
                    query: Optional[str] = None,
                    min_price: Optional[float] = None,
                    max_price: Optional[float] = None,
                    available_only: bool = True) -> List[Dict[str, Any]]:
        """搜索商品"""
        with self._lock:
            filtered_items = self._items.copy()
            
            if available_only:
                filtered_items = [item for item in filtered_items if item["is_available"]]
            
            if query:
                filtered_items = [
                    item for item in filtered_items 
                    if query.lower() in item["name"].lower() or 
                       (item.get("description") and query.lower() in item["description"].lower())
                ]
            
            if min_price is not None:
                filtered_items = [item for item in filtered_items if item["price"] >= min_price]
            
            if max_price is not None:
                filtered_items = [item for item in filtered_items if item["price"] <= max_price]
            
            return filtered_items
    
    # ===== 用戶相關操作 =====
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        """獲取所有用戶"""
        with self._lock:
            return self._users.copy()
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """根據 ID 獲取用戶"""
        with self._lock:
            for user in self._users:
                if user["id"] == user_id:
                    return user.copy()
            return None
    
    def get_user_by_username(self, username: str) -> Optional[Dict[str, Any]]:
        """根據用戶名獲取用戶"""
        with self._lock:
            for user in self._users:
                if user["username"] == username:
                    return user.copy()
            return None
    
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """創建新用戶"""
        with self._lock:
            user_data["id"] = self._next_user_id
            self._next_user_id += 1
            self._users.append(user_data.copy())
            return user_data
    
    def update_user(self, user_id: int, user_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """更新用戶"""
        with self._lock:
            for i, user in enumerate(self._users):
                if user["id"] == user_id:
                    user_data["id"] = user_id
                    self._users[i] = user_data.copy()
                    return user_data
            return None
    
    def delete_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        """刪除用戶"""
        with self._lock:
            for i, user in enumerate(self._users):
                if user["id"] == user_id:
                    return self._users.pop(i)
            return None
    
    # ===== 統計相關操作 =====
    
    def get_stats(self) -> Dict[str, Any]:
        """獲取統計信息"""
        with self._lock:
            total_items = len(self._items)
            available_items = len([item for item in self._items if item["is_available"]])
            total_users = len(self._users)
            
            if total_items > 0:
                avg_price = sum(item["price"] for item in self._items) / total_items
                max_price = max(item["price"] for item in self._items)
                min_price = min(item["price"] for item in self._items)
            else:
                avg_price = max_price = min_price = 0
            
            return {
                "items": {
                    "total": total_items,
                    "available": available_items,
                    "unavailable": total_items - available_items,
                    "price_stats": {
                        "average": round(avg_price, 2),
                        "maximum": max_price,
                        "minimum": min_price
                    }
                },
                "users": {
                    "total": total_users
                }
            }
    
    # ===== 數據初始化 =====
    
    def populate_sample_data(self):
        """填充示例數據"""
        with self._lock:
            # 檢查是否已有數據
            if len(self._items) > 0 or len(self._users) > 0:
                return
            
            # 添加示例商品
            sample_items = [
                {
                    "id": 1,
                    "name": "iPhone 15",
                    "description": "最新款 iPhone",
                    "price": 32000.0,
                    "is_available": True
                },
                {
                    "id": 2,
                    "name": "MacBook Pro",
                    "description": "專業筆記本電腦",
                    "price": 65000.0,
                    "is_available": True
                },
                {
                    "id": 3,
                    "name": "AirPods Pro",
                    "description": "無線耳機",
                    "price": 8000.0,
                    "is_available": False
                }
            ]
            
            # 添加示例用戶
            sample_users = [
                {
                    "id": 1,
                    "username": "alice",
                    "email": "alice@example.com",
                    "full_name": "Alice Wang"
                },
                {
                    "id": 2,
                    "username": "bob",
                    "email": "bob@example.com",
                    "full_name": "Bob Chen"
                }
            ]
            
            self._items.extend(sample_items)
            self._users.extend(sample_users)
            self._next_item_id = 4
            self._next_user_id = 3
    
    def clear_all_data(self):
        """清空所有數據（用於測試）"""
        with self._lock:
            self._items.clear()
            self._users.clear()
            self._next_item_id = 1
            self._next_user_id = 1


# 創建全局數據庫實例
db = MemoryDatabase()