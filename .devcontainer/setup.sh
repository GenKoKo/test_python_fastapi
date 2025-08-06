#!/bin/bash

# GitHub Codespaces 基礎設置腳本
# 只做最基本的工具安裝，其他邏輯交給 just 處理

echo "🔧 安裝基礎工具..."

# 安裝 Just 命令執行器
echo "📦 安裝 Just..."
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin

# 確保 just 在 PATH 中
export PATH="/usr/local/bin:$PATH"

# 設置腳本權限
chmod +x .devcontainer/*.sh

echo "✅ 基礎工具安裝完成！"
echo "🚀 執行完整設置: just codespaces-setup"