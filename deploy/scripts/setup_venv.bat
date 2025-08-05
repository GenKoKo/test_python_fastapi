@echo off
REM FastAPI 虛擬環境設置腳本 - Windows 版本

echo 🚀 開始設置 FastAPI 虛擬環境...

REM 檢查 Python 版本
echo 📋 檢查 Python 版本...
python --version

REM 創建虛擬環境
echo 📦 創建虛擬環境...
python -m venv fastapi_env

REM 激活虛擬環境
echo ⚡ 激活虛擬環境...
call fastapi_env\Scripts\activate.bat

REM 升級 pip
echo 🔄 升級 pip...
python -m pip install --upgrade pip

REM 安裝依賴
echo 📚 安裝項目依賴...
pip install -r requirements.txt

echo ✅ 虛擬環境設置完成！
echo.
echo 🎯 接下來的步驟：
echo 1. 激活虛擬環境: fastapi_env\Scripts\activate.bat
echo 2. 運行應用: python main.py
echo 3. 訪問 API 文檔: http://127.0.0.1:8000/docs
echo 4. 退出虛擬環境: deactivate
echo.
echo 💡 提示: 每次開發時都需要先激活虛擬環境！

pause