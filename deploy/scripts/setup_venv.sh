#!/bin/bash

# FastAPI 虛擬環境設置腳本
# 適用於 macOS/Linux

# 獲取腳本所在目錄的父目錄（項目根目錄）
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 切換到項目根目錄
cd "$PROJECT_ROOT"

echo "🚀 開始設置 FastAPI 虛擬環境..."

# 檢查 Python 版本
echo "📋 檢查 Python 版本..."
python3 --version

# 創建虛擬環境
echo "📦 創建虛擬環境..."
python3 -m venv fastapi_env

# 激活虛擬環境
echo "⚡ 激活虛擬環境..."
source fastapi_env/bin/activate

# 升級 pip
echo "🔄 升級 pip..."
pip install --upgrade pip

# 安裝依賴
echo "📚 安裝項目依賴..."
pip install -r requirements.txt

echo "✅ 虛擬環境設置完成！"
echo ""
echo "🎯 接下來的步驟："
echo "1. 激活虛擬環境: source fastapi_env/bin/activate"
echo "2. 運行應用: python main.py"
echo "3. 訪問 API 文檔: http://127.0.0.1:8000/docs"
echo "4. 退出虛擬環境: deactivate"
echo ""
echo "💡 提示: 每次開發時都需要先激活虛擬環境！"