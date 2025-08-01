#!/bin/bash

# FastAPI 應用運行腳本

# 檢查虛擬環境是否存在
if [ ! -d "fastapi_env" ]; then
    echo "❌ 虛擬環境不存在，請先運行 ./setup_venv.sh"
    exit 1
fi

# 激活虛擬環境
echo "⚡ 激活虛擬環境..."
source fastapi_env/bin/activate

# 檢查依賴是否已安裝
if ! pip show fastapi > /dev/null 2>&1; then
    echo "📚 安裝依賴..."
    pip install -r requirements.txt
fi

echo "🚀 啟動 FastAPI 應用..."
echo "📖 API 文檔將在 http://127.0.0.1:8000/docs 可用"
echo "🧪 服務器啟動後會自動運行 API 測試"
echo "🛑 按 Ctrl+C 停止服務器"
echo ""

# 運行應用
python main.py