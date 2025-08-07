#!/bin/bash

# 🧪 Codespaces 環境測試腳本
# 用於驗證環境是否正確設置

echo "🧪 測試 Codespaces 環境..."
echo "================================"

# 測試基本命令
echo "📋 基本環境檢查:"
echo "  工作目錄: $(pwd)"
echo "  用戶: $(whoami)"
echo "  Python: $(python --version 2>/dev/null || echo '❌ 未找到')"
echo "  uv: $(uv --version 2>/dev/null || echo '❌ 未找到')"
echo "  just: $(just --version 2>/dev/null || echo '❌ 未找到')"

echo ""
echo "🔍 PATH 檢查:"
echo "  PATH: $PATH"

echo ""
echo "📦 Python 環境檢查:"
if [ -d ".venv" ]; then
    echo "  ✅ 虛擬環境存在: .venv"
    echo "  Python 解釋器: $(.venv/bin/python --version 2>/dev/null || echo '❌ 虛擬環境 Python 不可用')"
else
    echo "  ❌ 虛擬環境不存在"
fi

echo ""
echo "🚀 Just 命令測試:"
if command -v just >/dev/null 2>&1; then
    echo "  ✅ just 命令可用"
    echo "  📋 可用命令:"
    just --list 2>/dev/null || echo "  ❌ just --list 失敗"
else
    echo "  ❌ just 命令不可用"
    echo "  💡 檢查 /usr/local/bin/just:"
    ls -la /usr/local/bin/just 2>/dev/null || echo "  ❌ /usr/local/bin/just 不存在"
fi

echo ""
echo "📁 專案結構檢查:"
echo "  src/: $([ -d 'src' ] && echo '✅ 存在' || echo '❌ 不存在')"
echo "  tests/: $([ -d 'tests' ] && echo '✅ 存在' || echo '❌ 不存在')"
echo "  pyproject.toml: $([ -f 'pyproject.toml' ] && echo '✅ 存在' || echo '❌ 不存在')"
echo "  justfile: $([ -f 'justfile' ] && echo '✅ 存在' || echo '❌ 不存在')"

echo ""
echo "🧪 FastAPI 導入測試:"
python -c "
try:
    import fastapi
    print('  ✅ FastAPI 可導入')
    print(f'  版本: {fastapi.__version__}')
except ImportError as e:
    print(f'  ❌ FastAPI 導入失敗: {e}')

try:
    import uvicorn
    print('  ✅ Uvicorn 可導入')
except ImportError as e:
    print(f'  ❌ Uvicorn 導入失敗: {e}')
" 2>/dev/null || echo "  ❌ Python 測試失敗"

echo ""
echo "================================"
echo "🎯 測試完成！"

# 如果 just 可用，顯示快速開始指南
if command -v just >/dev/null 2>&1; then
    echo ""
    echo "🚀 快速開始:"
    echo "  just dev          # 啟動開發服務器"
    echo "  just test-unit    # 運行單元測試"
    echo "  just --list       # 查看所有命令"
fi