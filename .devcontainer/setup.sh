#!/bin/bash

# 🚀 Codespaces 設置腳本
# 此腳本在 Codespace 創建時自動執行

set -e

echo "🚀 開始設置 FastAPI Codespaces 環境..."

# 檢查 Python 版本
echo "🐍 Python 版本: $(python --version)"

# 安裝 uv（如果尚未安裝）
if ! command -v uv >/dev/null 2>&1; then
    echo "📦 安裝 uv 包管理器..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# 檢查 uv 版本
echo "📦 uv 版本: $(uv --version 2>/dev/null || echo '未安裝')"

# 安裝 Just（如果尚未安裝）
if ! command -v just >/dev/null 2>&1; then
    echo "🔧 安裝 Just 命令工具..."
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin
fi

# 檢查 Just 版本
echo "🔧 Just 版本: $(just --version 2>/dev/null || echo '未安裝')"

# 創建必要的目錄
mkdir -p logs

# 同步 Python 依賴
echo "📚 同步 Python 依賴..."
if [ -f "pyproject.toml" ]; then
    uv sync --dev || echo "⚠️ uv sync 失敗，嘗試使用 pip..."
    if [ -f "requirements/base.txt" ]; then
        pip install -r requirements/base.txt
    fi
else
    echo "⚠️ 未找到 pyproject.toml，嘗試使用 requirements..."
    if [ -f "requirements/base.txt" ]; then
        pip install -r requirements/base.txt
    fi
fi

# 驗證安裝
echo "🧪 驗證環境設置..."
python -c "
try:
    import fastapi
    print('✅ FastAPI 已安裝')
except ImportError:
    print('❌ FastAPI 未安裝')

try:
    import uvicorn
    print('✅ Uvicorn 已安裝')
except ImportError:
    print('❌ Uvicorn 未安裝')
"

echo "🎉 FastAPI Codespaces 環境設置完成！"
echo ""
echo "📋 快速開始："
echo "  just --list          # 查看所有可用命令"
echo "  just dev             # 啟動開發服務器"
echo "  just test-unit       # 運行單元測試"
echo ""
echo "📖 API 文檔將在: http://localhost:8000/docs"