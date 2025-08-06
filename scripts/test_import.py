#!/usr/bin/env python3
"""
測試應用導入
"""

try:
    from src.app.main import app
    from src.core import settings, app_logger

    print("✅ 應用導入成功")
    print(f"配置: {settings.app_name} v{settings.app_version}")
    print(f"服務器: {settings.host}:{settings.port}")
    print(f"日誌級別: {settings.log_level}")

    app_logger.info("測試日誌記錄")

    print("🎉 所有模組都正常工作！")

except Exception as e:
    print(f"❌ 導入失敗: {e}")
    import traceback

    traceback.print_exc()
