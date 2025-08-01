#!/usr/bin/env python3
"""
虛擬環境測試腳本
檢查虛擬環境是否正確設置並測試 FastAPI 應用
"""

import sys
import subprocess
import importlib.util
import os

def check_virtual_env():
    """檢查是否在虛擬環境中"""
    print("🔍 檢查虛擬環境狀態...")
    
    # 檢查虛擬環境
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ 當前在虛擬環境中")
        print(f"   Python 路徑: {sys.executable}")
        print(f"   虛擬環境路徑: {sys.prefix}")
        return True
    else:
        print("❌ 當前不在虛擬環境中")
        print("💡 請先激活虛擬環境:")
        print("   macOS/Linux: source fastapi_env/bin/activate")
        print("   Windows: fastapi_env\\Scripts\\activate.bat")
        return False

def check_dependencies():
    """檢查必要的依賴是否已安裝"""
    print("\n📦 檢查依賴包...")
    
    required_packages = ['fastapi', 'uvicorn', 'pydantic', 'requests']
    missing_packages = []
    
    for package in required_packages:
        spec = importlib.util.find_spec(package)
        if spec is None:
            missing_packages.append(package)
            print(f"❌ {package} 未安裝")
        else:
            try:
                module = importlib.import_module(package)
                version = getattr(module, '__version__', 'unknown')
                print(f"✅ {package} {version}")
            except ImportError:
                print(f"⚠️  {package} 已安裝但無法導入")
    
    if missing_packages:
        print(f"\n❌ 缺少依賴: {', '.join(missing_packages)}")
        print("💡 請運行: pip install -r requirements.txt")
        return False
    
    return True

def check_python_version():
    """檢查 Python 版本"""
    print("\n🐍 檢查 Python 版本...")
    
    version = sys.version_info
    print(f"Python 版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print("✅ Python 版本符合要求 (3.7+)")
        return True
    else:
        print("❌ Python 版本過低，需要 3.7 或更高版本")
        return False

def test_fastapi_import():
    """測試 FastAPI 導入"""
    print("\n🚀 測試 FastAPI 導入...")
    
    try:
        from fastapi import FastAPI
        from pydantic import BaseModel
        import uvicorn
        
        # 創建一個簡單的測試應用
        test_app = FastAPI(title="Test App")
        
        @test_app.get("/test")
        def test_endpoint():
            return {"message": "FastAPI 工作正常！"}
        
        print("✅ FastAPI 導入成功")
        print("✅ 可以創建 FastAPI 應用")
        return True
        
    except ImportError as e:
        print(f"❌ FastAPI 導入失敗: {e}")
        return False

def check_project_files():
    """檢查項目文件是否存在"""
    print("\n📁 檢查項目文件...")
    
    required_files = ['main.py', 'requirements.txt', 'README.md']
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            missing_files.append(file)
            print(f"❌ {file} 不存在")
    
    if missing_files:
        print(f"\n❌ 缺少文件: {', '.join(missing_files)}")
        return False
    
    return True

def main():
    """主函數"""
    print("🧪 FastAPI 虛擬環境測試")
    print("=" * 40)
    
    # 執行所有檢查
    checks = [
        ("虛擬環境", check_virtual_env),
        ("Python 版本", check_python_version),
        ("項目文件", check_project_files),
        ("依賴包", check_dependencies),
        ("FastAPI 導入", test_fastapi_import)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name} 檢查時出錯: {e}")
            results.append((name, False))
    
    # 總結
    print("\n" + "=" * 40)
    print("📊 檢查結果總結:")
    
    all_passed = True
    for name, result in results:
        status = "✅ 通過" if result else "❌ 失敗"
        print(f"   {name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("🎉 所有檢查都通過！你的環境已準備就緒。")
        print("💡 現在可以運行: python main.py")
    else:
        print("⚠️  有些檢查未通過，請根據上面的提示進行修復。")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)