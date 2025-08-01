#!/bin/bash

# 在虛擬環境中運行測試腳本

# 檢查虛擬環境是否存在
if [ ! -d "fastapi_env" ]; then
    echo "❌ 虛擬環境不存在，請先運行 ./setup_venv.sh"
    exit 1
fi

# 激活虛擬環境
echo "⚡ 激活虛擬環境..."
source fastapi_env/bin/activate

# 檢查依賴是否已安裝
if ! pip show requests > /dev/null 2>&1; then
    echo "📚 安裝依賴..."
    pip install -r requirements.txt
fi

echo "🧪 在虛擬環境中運行 API 測試..."
echo "📝 注意: 請確保 FastAPI 服務器正在運行 (python main.py)"
echo ""

# 運行測試
python test_api.py