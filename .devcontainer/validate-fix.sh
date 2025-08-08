#!/bin/bash

# 🧪 驗證 Codespaces 修復腳本
# 用於測試修復後的環境是否正常工作

echo "🔍 驗證 Codespaces 修復..."
echo "================================"

# 檢查基本命令是否存在
echo "📋 基本命令檢查:"
commands=("sleep" "curl" "git" "bash" "ps" "which" "whoami")
for cmd in "${commands[@]}"; do
    if command -v "$cmd" >/dev/null 2>&1; then
        echo "  ✅ $cmd: 可用"
    else
        echo "  ❌ $cmd: 不可用"
    fi
done

echo ""
echo "👤 用戶和權限檢查:"
echo "  當前用戶: $(whoami)"
echo "  用戶 ID: $(id)"
echo "  工作目錄: $(pwd)"
echo "  家目錄: $HOME"

echo ""
echo "🔧 Just 命令檢查:"
if command -v just >/dev/null 2>&1; then
    echo "  ✅ just 可用"
    echo "  版本: $(just --version)"
    echo "  位置: $(which just)"
else
    echo "  ❌ just 不可用"
    echo "  檢查 /usr/local/bin/just:"
    ls -la /usr/local/bin/just 2>/dev/null || echo "  ❌ 不存在"
fi

echo ""
echo "🐍 Python 環境檢查:"
if command -v python >/dev/null 2>&1; then
    echo "  ✅ Python: $(python --version)"
else
    echo "  ❌ Python 不可用"
fi

if command -v uv >/dev/null 2>&1; then
    echo "  ✅ uv: $(uv --version)"
else
    echo "  ❌ uv 不可用"
fi

echo ""
echo "📁 目錄權限檢查:"
dirs=("/app" "/workspaces" "$HOME")
for dir in "${dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "  ✅ $dir: 存在"
        echo "    權限: $(ls -ld "$dir" | awk '{print $1, $3, $4}')"
        if [ -w "$dir" ]; then
            echo "    ✅ 可寫"
        else
            echo "    ❌ 不可寫"
        fi
    else
        echo "  ❌ $dir: 不存在"
    fi
done

echo ""
echo "🌐 網路連接檢查:"
if curl -s --connect-timeout 5 https://github.com >/dev/null; then
    echo "  ✅ 網路連接正常"
else
    echo "  ❌ 網路連接問題"
fi

echo ""
echo "🔍 Codespaces 特定檢查:"
echo "  CODESPACES 環境變數: ${CODESPACES:-未設置}"
echo "  ENVIRONMENT 環境變數: ${ENVIRONMENT:-未設置}"
echo "  PATH: $PATH"

echo ""
echo "================================"
echo "🎯 驗證完成！"

# 總結
echo ""
echo "📊 修復狀態總結:"
if command -v just >/dev/null 2>&1 && command -v python >/dev/null 2>&1 && command -v sleep >/dev/null 2>&1; then
    echo "  🎉 主要修復成功！環境應該可以正常工作"
    echo ""
    echo "🚀 建議的下一步:"
    echo "  1. 測試 'just --list' 查看可用命令"
    echo "  2. 運行 'just dev' 啟動開發服務器"
    echo "  3. 訪問 http://localhost:8000/docs 查看 API 文檔"
else
    echo "  ⚠️ 仍有問題需要解決"
    echo "  💡 請檢查上述失敗的項目"
fi