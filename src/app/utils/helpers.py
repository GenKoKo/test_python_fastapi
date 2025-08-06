"""
工具函數
提供通用的輔助功能
"""

import time
from typing import Any, Dict
from src.core import app_logger


def generate_id() -> int:
    """生成唯一 ID（基於時間戳）"""
    return int(time.time() * 1000000)


def format_response(data: Any, message: str = "success") -> Dict[str, Any]:
    """格式化 API 響應"""
    return {
        "status": "success",
        "message": message,
        "data": data,
        "timestamp": time.time(),
    }


def format_error_response(error: str, status_code: int = 500) -> Dict[str, Any]:
    """格式化錯誤響應"""
    return {
        "status": "error",
        "message": error,
        "status_code": status_code,
        "timestamp": time.time(),
    }


def validate_pagination(
    page: int = 1, size: int = 10, max_size: int = 100
) -> Dict[str, int]:
    """驗證分頁參數"""
    if page < 1:
        page = 1
    if size < 1:
        size = 10
    if size > max_size:
        size = max_size

    offset = (page - 1) * size

    return {"page": page, "size": size, "offset": offset}


def log_function_execution(func_name: str, duration: float, success: bool = True):
    """記錄函數執行日誌"""
    status = "成功" if success else "失敗"
    app_logger.info(f"函數執行 - {func_name}: {status}, 耗時: {duration:.3f}s")


def safe_dict_get(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    """安全獲取字典值"""
    try:
        return data.get(key, default)
    except (AttributeError, TypeError):
        return default


def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """清理字典中的 None 值"""
    return {k: v for k, v in data.items() if v is not None}
