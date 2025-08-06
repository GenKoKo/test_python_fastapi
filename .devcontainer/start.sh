#!/bin/bash

# GitHub Codespaces 啟動腳本
# 簡化版本，主要邏輯交給 just 處理

echo "🌟 歡迎使用 FastAPI Codespaces 開發環境！"

# 確保 just 在 PATH 中
export PATH="/usr/local/bin:$PATH"

# 執行 just 啟動邏輯
if command -v just >/dev/null 2>&1; then
    just codespaces-welcome
else
    echo "⚠️ Just 未安裝，請稍等環境設置完成..."
fi