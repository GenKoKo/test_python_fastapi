"""
FastAPI 主應用文件
應用的入口點和配置
"""

import threading
import time
from typing import Dict, Any
import requests
from fastapi import FastAPI

# 導入配置和日誌
from src.core import (
    settings,
    validate_config,
    print_config,
    app_logger,
    log_startup,
    log_shutdown,
)

# 導入路由
from .routers import items_router, users_router, stats_router

# 導入中間件
from .utils import LoggingMiddleware

# 導入數據庫
from .database.memory_db import db

# 驗證配置
try:
    validate_config()
    app_logger.info("✅ 配置驗證通過")
except ValueError as e:
    app_logger.error(f"❌ 配置驗證失敗: {e}")
    import sys

    sys.exit(1)

# 創建 FastAPI 應用實例
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url,
)

# 添加中間件
app.add_middleware(LoggingMiddleware)

# 註冊路由
app.include_router(items_router)
app.include_router(users_router)
app.include_router(stats_router)


# 根路由
@app.get("/", tags=["基本"])
async def read_root() -> Dict[str, Any]:
    """歡迎頁面"""
    app_logger.info("📋 訪問根路徑")
    return {
        "message": "歡迎使用 FastAPI 初級入門 API！",
        "docs": settings.docs_url,
        "redoc": settings.redoc_url,
        "version": settings.app_version,
        "features": [
            "商品管理 CRUD",
            "用戶管理",
            "搜索功能",
            "統計信息",
            "自動 API 文檔",
        ],
    }


def populate_sample_data() -> None:
    """填充示例數據"""
    if not settings.populate_sample_data:
        app_logger.info("⏭️  跳過示例數據填充（配置已禁用）")
        return

    app_logger.info("📊 開始填充示例數據...")

    try:
        db.populate_sample_data()
        app_logger.info("✅ 示例數據填充完成")

    except Exception as e:
        app_logger.error(f"❌ 示例數據填充失敗: {e}")
        raise


def run_api_tests() -> None:
    """運行 API 測試"""
    BASE_URL = f"http://{settings.host}:{settings.port}"

    def wait_for_server() -> bool:
        """等待服務器啟動"""
        max_attempts = 30
        app_logger.info("⏳ 等待服務器啟動...")

        for attempt in range(max_attempts):
            try:
                response = requests.get(f"{BASE_URL}/stats/health", timeout=1)
                if response.status_code == 200:
                    app_logger.info("✅ 服務器已就緒")
                    return True
            except requests.exceptions.RequestException:
                pass
            time.sleep(1)

        app_logger.error("❌ 服務器啟動超時")
        return False

    def run_tests() -> None:
        """運行測試"""
        app_logger.info("🧪 開始 API 自動測試...")

        if not wait_for_server():
            app_logger.error("❌ 服務器啟動超時，跳過測試")
            return

        test_results = []

        try:
            # 1. 測試根路徑
            app_logger.info("1️⃣ 測試根路徑...")
            response = requests.get(f"{BASE_URL}/")
            test_results.append(("根路徑", response.status_code == 200))

            # 2. 測試健康檢查
            app_logger.info("2️⃣ 測試健康檢查...")
            response = requests.get(f"{BASE_URL}/stats/health")
            test_results.append(("健康檢查", response.status_code == 200))

            # 3. 測試獲取商品
            app_logger.info("3️⃣ 測試獲取商品...")
            response = requests.get(f"{BASE_URL}/items/")
            items = response.json()
            test_results.append(("獲取商品", response.status_code == 200))
            app_logger.info(f"   找到 {len(items)} 個商品")

            # 4. 測試獲取用戶
            app_logger.info("4️⃣ 測試獲取用戶...")
            response = requests.get(f"{BASE_URL}/users/")
            users = response.json()
            test_results.append(("獲取用戶", response.status_code == 200))
            app_logger.info(f"   找到 {len(users)} 個用戶")

            # 5. 測試搜索功能
            app_logger.info("5️⃣ 測試搜索功能...")
            response = requests.get(f"{BASE_URL}/items/search/?q=iPhone")
            search_result = response.json()
            test_results.append(("搜索功能", response.status_code == 200))
            app_logger.info(f"   搜索結果: {search_result['count']} 個商品")

            # 6. 測試統計功能
            app_logger.info("6️⃣ 測試統計功能...")
            response = requests.get(f"{BASE_URL}/stats/")
            stats = response.json()
            test_results.append(("統計功能", response.status_code == 200))
            app_logger.info(
                f"   統計: {stats['items']['total']} 商品, {stats['users']['total']} 用戶"
            )

            # 測試結果總結
            passed_tests = sum(1 for _, result in test_results if result)
            total_tests = len(test_results)

            if passed_tests == total_tests:
                app_logger.info(f"🎉 所有測試通過！({passed_tests}/{total_tests})")
            else:
                app_logger.warning(f"⚠️  部分測試失敗: {passed_tests}/{total_tests}")

            app_logger.info("💡 你可以訪問以下地址:")
            app_logger.info(f"   📖 API 文檔: {BASE_URL}{settings.docs_url}")
            app_logger.info(f"   📚 ReDoc: {BASE_URL}{settings.redoc_url}")

        except Exception as e:
            app_logger.error(f"❌ 測試過程中出錯: {e}")

    # 在新線程中運行測試，避免阻塞服務器
    test_thread = threading.Thread(target=run_tests, daemon=True)
    test_thread.start()


# FastAPI 事件處理
@app.on_event("startup")
async def startup_event() -> None:
    """應用啟動時執行"""
    log_startup()

    # 打印配置信息（如果是調試模式）
    if settings.debug:
        print_config()

    # 填充示例數據
    populate_sample_data()

    # 啟動自動測試（如果啟用）
    if settings.enable_auto_test:
        app_logger.info(f"🧪 將在 {settings.test_delay} 秒後啟動自動測試")

        def delayed_test() -> None:
            time.sleep(settings.test_delay)
            run_api_tests()

        test_thread = threading.Thread(target=delayed_test, daemon=True)
        test_thread.start()
    else:
        app_logger.info("⏭️  自動測試已禁用")


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """應用關閉時執行"""
    log_shutdown()
    stats = db.get_stats()
    app_logger.info(
        f"📊 最終統計: {stats['items']['total']} 個商品, {stats['users']['total']} 個用戶"
    )
