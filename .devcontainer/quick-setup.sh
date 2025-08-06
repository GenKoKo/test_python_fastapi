#!/bin/bash

# 🚀 GitHub Codespaces 快速設置腳本
# 這個腳本會在 Codespace 創建時自動運行

set -e

echo "🌟 開始 FastAPI Codespaces 快速設置..."

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日誌函數
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# 檢查是否在 Codespaces 中
if [ "$CODESPACES" != "true" ]; then
    log_warning "不在 GitHub Codespaces 環境中，跳過 Codespaces 特定設置"
    exit 0
fi

log_info "檢測到 GitHub Codespaces 環境"
log_info "Codespace: $CODESPACE_NAME"

# 1. 安裝 Just 命令工具
log_info "檢查 Just 命令工具..."
if ! command -v just >/dev/null 2>&1; then
    log_info "安裝 Just 命令工具..."
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin
    log_success "Just 命令工具安裝完成"
else
    log_success "Just 命令工具已安裝: $(just --version)"
fi

# 2. 配置 Git（如果需要）
log_info "配置 Git 設置..."
if [ -n "$GITHUB_USER" ] && [ -z "$(git config --global user.name)" ]; then
    git config --global user.name "$GITHUB_USER"
    git config --global user.email "$GITHUB_USER@users.noreply.github.com"
    log_success "Git 用戶配置完成: $GITHUB_USER"
else
    log_success "Git 配置已存在或無需配置"
fi

# 3. 創建環境配置文件
log_info "創建環境配置文件..."
if [ ! -f .env ]; then
    cat > .env << EOF
# GitHub Codespaces 環境配置
DEBUG=true
LOG_LEVEL=info
HOST=0.0.0.0
PORT=8000
RELOAD=true
ENABLE_AUTO_TEST=false

# Codespaces 特定設置
CODESPACES=true
ENVIRONMENT=codespaces
CODESPACE_NAME=$CODESPACE_NAME

# API 配置
API_TITLE=FastAPI Development (Codespaces)
API_DESCRIPTION=FastAPI application running in GitHub Codespaces
API_VERSION=1.0.0
EOF
    log_success "環境配置文件創建完成"
else
    log_success "環境配置文件已存在"
fi

# 4. 更新 Python 依賴
log_info "更新 Python 依賴..."
pip install --upgrade pip --quiet
pip install -r requirements/dev.txt --quiet
log_success "Python 依賴更新完成"

# 5. 創建必要的目錄
log_info "創建項目目錄..."
mkdir -p logs
mkdir -p .pytest_cache
log_success "項目目錄創建完成"

# 6. 驗證環境
log_info "驗證環境設置..."
python -c "from src.app.main import app; print('FastAPI 應用導入成功')" 2>/dev/null
if [ $? -eq 0 ]; then
    log_success "FastAPI 應用驗證通過"
else
    log_error "FastAPI 應用驗證失敗"
fi

# 7. 設置 Zsh（如果可用）
if command -v zsh >/dev/null 2>&1; then
    log_info "配置 Zsh shell..."
    # 設置 Zsh 為默認 shell（如果尚未設置）
    if [ "$SHELL" != "/bin/zsh" ] && [ "$SHELL" != "/usr/bin/zsh" ]; then
        echo "export SHELL=/bin/zsh" >> ~/.bashrc
    fi
    log_success "Zsh 配置完成"
fi

# 8. 創建快速啟動別名
log_info "創建快速啟動別名..."
cat >> ~/.bashrc << 'EOF'

# FastAPI Codespaces 快速命令
alias fapi-dev='just dev'
alias fapi-test='just test-unit'
alias fapi-status='just codespaces-status'
alias fapi-docs='echo "📖 API 文檔: https://$CODESPACE_NAME-8000.app.github.dev/docs"'
alias fapi-help='just help'

# 顯示歡迎信息
if [ "$CODESPACES" = "true" ]; then
    echo ""
    echo "🚀 FastAPI Codespaces 環境已就緒！"
    echo ""
    echo "📋 快速命令："
    echo "  fapi-dev     # 啟動開發服務器"
    echo "  fapi-test    # 運行測試"
    echo "  fapi-status  # 檢查環境狀態"
    echo "  fapi-docs    # 顯示 API 文檔 URL"
    echo "  fapi-help    # 顯示所有可用命令"
    echo ""
    echo "📖 API 文檔: https://$CODESPACE_NAME-8000.app.github.dev/docs"
    echo "🔍 項目狀態: just status"
    echo ""
fi
EOF

# 9. 創建部署信息文件
log_info "創建部署信息文件..."
cat > .devcontainer/CODESPACE_INFO.md << EOF
# 🚀 Codespace 環境信息

## 環境詳情
- **Codespace 名稱**: $CODESPACE_NAME
- **設置時間**: $(date -u +"%Y-%m-%d %H:%M:%S UTC")
- **Python 版本**: $(python --version)
- **Just 版本**: $(just --version 2>/dev/null || echo 'Not installed')
- **Git 用戶**: $(git config --global user.name || echo 'Not configured')

## 快速開始
\`\`\`bash
# 啟動開發服務器
just dev

# 運行測試
just test-unit

# 檢查狀態
just codespaces-status
\`\`\`

## 有用的 URL
- **API 文檔**: https://$CODESPACE_NAME-8000.app.github.dev/docs
- **Codespace**: https://$CODESPACE_NAME.github.dev

## 快速命令別名
- \`fapi-dev\` - 啟動開發服務器
- \`fapi-test\` - 運行測試
- \`fapi-status\` - 檢查環境狀態
- \`fapi-docs\` - 顯示 API 文檔 URL

---
*此文件由 Codespaces 快速設置腳本自動生成*
EOF

log_success "部署信息文件創建完成"

# 10. 最終檢查和總結
log_info "執行最終檢查..."

# 檢查關鍵文件
REQUIRED_FILES=(".env" "requirements/base.txt" "src/app/main.py" "justfile")
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        log_success "✓ $file"
    else
        log_error "✗ $file (缺失)"
    fi
done

# 檢查關鍵命令
REQUIRED_COMMANDS=("python" "pip" "just" "git")
for cmd in "${REQUIRED_COMMANDS[@]}"; do
    if command -v "$cmd" >/dev/null 2>&1; then
        log_success "✓ $cmd"
    else
        log_error "✗ $cmd (未安裝)"
    fi
done

echo ""
echo "🎉 FastAPI Codespaces 快速設置完成！"
echo ""
echo "📋 下一步："
echo "1. 運行 'just dev' 啟動開發服務器"
echo "2. 訪問 https://$CODESPACE_NAME-8000.app.github.dev/docs 查看 API 文檔"
echo "3. 運行 'just test-unit' 執行測試"
echo "4. 運行 'just codespaces-status' 檢查環境狀態"
echo ""
echo "💡 提示: 使用 'fapi-*' 別名可以快速執行常用命令"
echo ""

log_success "設置腳本執行完成！"