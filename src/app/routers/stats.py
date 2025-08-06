"""
統計路由
處理統計相關的 API 端點
"""

from fastapi import APIRouter, HTTPException
from ..database.memory_db import db
from src.core import app_logger

router = APIRouter(prefix="/stats", tags=["統計信息"])


@router.get("/", summary="獲取統計信息")
async def get_stats():
    """
    獲取系統統計信息

    返回以下統計數據：
    - 商品統計：總數、可用數量、價格統計
    - 用戶統計：總數
    """
    app_logger.debug("獲取統計信息")

    try:
        stats = db.get_stats()
        app_logger.info("統計信息獲取成功")
        return stats

    except Exception as e:
        app_logger.error(f"獲取統計信息失敗: {e}")
        raise HTTPException(status_code=500, detail="獲取統計信息時發生錯誤")


@router.get("/health", summary="健康檢查")
async def health_check():
    """
    API 健康檢查

    返回 API 服務的健康狀態
    """
    app_logger.debug("健康檢查請求")

    from src.core import settings
    import time

    return {
        "status": "healthy",
        "message": "API 運行正常",
        "timestamp": time.time(),
        "version": settings.app_version,
        "service": settings.app_name,
    }
