#!/usr/bin/env python3
"""
FastAPI 應用啟動腳本
使用配置系統啟動應用
"""

import sys
from pathlib import Path

# 添加項目根目錄到 Python 路徑
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

import uvicorn
from src.core import settings, app_logger

if __name__ == "__main__":
    app_logger.info("🌟 啟動 FastAPI 開發服務器...")

    if settings.enable_auto_test:
        app_logger.info("📝 注意: 服務器啟動後會自動運行 API 測試")

    # 使用配置中的值
    uvicorn.run(
        "src.app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.lower(),
    )
