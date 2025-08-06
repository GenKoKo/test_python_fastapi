#!/usr/bin/env python3
"""
配置測試腳本
測試配置系統和日誌系統是否正常工作
"""

import os
import sys
from pathlib import Path

def test_config_system():
    """測試配置系統"""
    print("🧪 測試配置系統...")
    
    try:
        from src.core import settings, validate_config, print_config
        
        print("✅ 配置模組導入成功")
        
        # 測試配置驗證
        validate_config()
        print("✅ 配置驗證通過")
        
        # 打印配置信息
        print("\n📋 當前配置:")
        print_config()
        
        return True
        
    except Exception as e:
        print(f"❌ 配置系統測試失敗: {e}")
        return False


def test_logger_system():
    """測試日誌系統"""
    print("\n🧪 測試日誌系統...")
    
    try:
        from src.core.logger import setup_logger, app_logger
        
        print("✅ 日誌模組導入成功")
        
        # 測試日誌記錄
        test_logger = setup_logger("test", level="DEBUG")
        
        test_logger.debug("這是調試信息")
        test_logger.info("這是信息")
        test_logger.warning("這是警告")
        test_logger.error("這是錯誤")
        
        print("✅ 日誌系統測試通過")
        
        return True
        
    except Exception as e:
        print(f"❌ 日誌系統測試失敗: {e}")
        return False


def test_environment_variables():
    """測試環境變量"""
    print("\n🧪 測試環境變量...")
    
    # 檢查 .env 文件是否存在
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_file.exists() and env_example.exists():
        print("💡 提示: .env 文件不存在，但 .env.example 存在")
        print("   你可以複製 .env.example 為 .env 並根據需要修改")
    elif env_file.exists():
        print("✅ .env 文件存在")
    
    # 測試一些環境變量
    test_vars = [
        ("APP_NAME", "應用名稱"),
        ("HOST", "主機地址"),
        ("PORT", "端口號"),
        ("LOG_LEVEL", "日誌級別")
    ]
    
    print("\n🔍 環境變量檢查:")
    for var_name, description in test_vars:
        value = os.getenv(var_name)
        if value:
            print(f"  ✅ {var_name} ({description}): {value}")
        else:
            print(f"  ⚪ {var_name} ({description}): 使用默認值")
    
    return True


def test_dependencies():
    """測試依賴包"""
    print("\n🧪 測試依賴包...")
    
    required_packages = [
        ("fastapi", "FastAPI 框架"),
        ("pydantic", "數據驗證"),
        ("pydantic_settings", "設置管理"),
        ("uvicorn", "ASGI 服務器"),
        ("requests", "HTTP 客戶端"),
        ("dotenv", "環境變量加載")
    ]
    
    missing_packages = []
    
    for package, description in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package} ({description})")
        except ImportError:
            print(f"  ❌ {package} ({description}) - 未安裝")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ 缺少依賴包: {', '.join(missing_packages)}")
        print("💡 請運行: pip install -r requirements/base.txt")
        return False
    
    print("✅ 所有依賴包都已安裝")
    return True


def main():
    """主函數"""
    print("🔧 FastAPI 配置和日誌系統測試")
    print("=" * 50)
    
    tests = [
        ("依賴包", test_dependencies),
        ("環境變量", test_environment_variables),
        ("配置系統", test_config_system),
        ("日誌系統", test_logger_system)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} 測試時出錯: {e}")
            results.append((test_name, False))
    
    # 總結
    print("\n" + "=" * 50)
    print("📊 測試結果總結:")
    
    all_passed = True
    for test_name, result in results:
        status = "✅ 通過" if result else "❌ 失敗"
        print(f"   {test_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 所有測試都通過！配置和日誌系統已準備就緒。")
        print("💡 現在可以運行: python main.py")
    else:
        print("⚠️  有些測試未通過，請根據上面的提示進行修復。")
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)