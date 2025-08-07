#!/bin/bash

# 🔧 修復 Codespaces 中 Just 安裝問題的腳本
# 位置: scripts/fix-just-install.sh
# 用途: 解決 GitHub Codespaces 中 Just 命令安裝和 PATH 問題

echo "🚀 修復 Just 安裝問題..."

# 創建本地 bin 目錄
mkdir -p ~/.local/bin

# 安裝 Just 到用戶目錄
echo "📦 安裝 Just 到用戶目錄..."
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin

# 添加到 PATH
export PATH="$HOME/.local/bin:$PATH"

# 永久添加到 shell 配置
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc

# 重新載入 bashrc
source ~/.bashrc

# 驗證安裝
if command -v just >/dev/null 2>&1; then
    echo "✅ Just 安裝成功！"
    echo "🔧 Just 版本: $(just --version)"
    echo ""
    echo "📋 現在您可以使用以下命令："
    echo "  just --list          # 查看所有可用命令"
    echo "  just dev             # 啟動開發服務器"
    echo "  just test-unit       # 運行單元測試"
else
    echo "❌ Just 安裝失敗，請手動檢查"
fi

echo ""
echo "💡 如果 just 命令仍然無法使用，請執行："
echo "  source ~/.bashrc"
echo "  或重新啟動終端"
echo ""
echo "🔍 更多幫助請查看："
echo "  - .devcontainer/README.md"
echo "  - 項目根目錄的 README.md 故障排除章節"