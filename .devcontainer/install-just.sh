#!/bin/bash

# 🔧 Codespaces 專用 Just 安裝腳本
# 解決權限和 PATH 問題

set -e

echo "🚀 開始安裝 Just 命令工具..."

# 檢查是否已安裝
if command -v just >/dev/null 2>&1; then
    echo "✅ Just 已安裝，版本: $(just --version)"
    exit 0
fi

# 創建本地 bin 目錄
LOCAL_BIN="$HOME/.local/bin"
mkdir -p "$LOCAL_BIN"

echo "📥 下載 Just 安裝腳本..."

# 下載並安裝 Just
if curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to "$LOCAL_BIN"; then
    echo "✅ Just 下載安裝成功"
else
    echo "❌ Just 安裝失敗，嘗試手動下載..."
    
    # 手動下載方式（備用）
    JUST_VERSION="1.42.4"
    JUST_URL="https://github.com/casey/just/releases/download/${JUST_VERSION}/just-${JUST_VERSION}-x86_64-unknown-linux-musl.tar.gz"
    
    cd /tmp
    wget "$JUST_URL" -O just.tar.gz
    tar -xzf just.tar.gz
    mv just "$LOCAL_BIN/"
    chmod +x "$LOCAL_BIN/just"
    rm -f just.tar.gz
    
    echo "✅ Just 手動安裝完成"
fi

# 設定 PATH
export PATH="$LOCAL_BIN:$PATH"

# 添加到 shell 配置文件
BASHRC="$HOME/.bashrc"
ZSHRC="$HOME/.zshrc"

# 添加到 .bashrc
if [ -f "$BASHRC" ]; then
    if ! grep -q "export PATH=\"\$HOME/.local/bin:\$PATH\"" "$BASHRC"; then
        echo "" >> "$BASHRC"
        echo "# Just 命令工具 PATH" >> "$BASHRC"
        echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$BASHRC"
        echo "✅ 已添加到 .bashrc"
    fi
fi

# 添加到 .zshrc
if [ -f "$ZSHRC" ]; then
    if ! grep -q "export PATH=\"\$HOME/.local/bin:\$PATH\"" "$ZSHRC"; then
        echo "" >> "$ZSHRC"
        echo "# Just 命令工具 PATH" >> "$ZSHRC"
        echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$ZSHRC"
        echo "✅ 已添加到 .zshrc"
    fi
fi

# 驗證安裝
if command -v just >/dev/null 2>&1; then
    echo "🎉 Just 安裝成功！"
    echo "🔧 版本: $(just --version)"
    echo ""
    echo "📋 現在您可以使用："
    echo "  just --list    # 查看所有命令"
    echo "  just dev       # 啟動開發服務器"
else
    echo "⚠️ Just 安裝完成，但可能需要重新載入 shell"
    echo "💡 請執行: source ~/.bashrc"
fi

echo "✅ 安裝腳本執行完成"