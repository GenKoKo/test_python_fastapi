# FastAPI 項目管理 - Just 命令集合
# 
# 這個 justfile 提供了完整的 FastAPI 項目管理命令
# 包含開發、測試、部署、Docker 和 GitHub Codespaces 支持
#
# 🚀 快速開始:
#   just setup    # 設置開發環境
#   just dev      # 啟動開發服務器
#   just help     # 查看所有可用命令
#
# 📋 主要功能:
#   - 虛擬環境管理
#   - 開發服務器啟動
#   - 測試和代碼品質檢查
#   - Docker 容器管理
#   - GitHub Codespaces 支持
#   - 依賴管理和清理工具
#
# 💡 使用提示:
#   - 所有命令都有詳細的錯誤檢查和提示
#   - 支持 Docker 和 Podman 容器引擎
#   - 自動檢測 GitHub Codespaces 環境
#   - 提供快速開始的組合命令

# 🔧 設定變數
python := "python3"
venv_dir := ".venv"
venv_python := venv_dir + "/bin/python"
# 使用 uv 進行依賴管理
uv_run := "uv run"
# 容器引擎設定 (支援 Docker 和 Podman)
# 使用 Podman 作為默認容器引擎
docker_compose := "DOCKER_HOST=unix:///var/run/docker.sock docker-compose -f docker/docker-compose.yml"

# 預設命令：顯示所有可用命令
default:
    @just --list

# 🚀 開發環境設置
# 使用 uv 創建並設置虛擬環境
setup:
    #!/usr/bin/env bash
    echo "🚀 開始設置 FastAPI 開發環境 (使用 uv)..."
    echo "📋 檢查 Python 版本..."
    {{python}} --version
    echo "📦 檢查 uv 安裝..."
    if ! command -v uv >/dev/null 2>&1; then
        echo "❌ uv 未安裝，請先安裝 uv: https://docs.astral.sh/uv/getting-started/installation/"
        exit 1
    fi
    echo "📚 同步項目依賴..."
    uv sync --dev
    echo "✅ 開發環境設置完成！"

# 🏃 運行應用
run:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🚀 啟動 FastAPI 應用..."
    {{uv_run}} python run.py

# 🔧 開發模式運行
dev:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🔧 開發模式啟動 FastAPI 應用..."
    {{uv_run}} uvicorn src.app.main:app --reload --host 127.0.0.1 --port 8000

# 🧪 測試相關命令
# 運行 API 功能測試
test:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🧪 運行 API 功能測試..."
    {{uv_run}} python scripts/test_api.py

# 運行單元測試
test-unit:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🧪 運行單元測試..."
    {{uv_run}} pytest tests/ -v

# 運行測試並生成覆蓋率報告
test-coverage:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "📊 運行測試並生成覆蓋率報告..."
    {{uv_run}} pytest tests/ --cov=src --cov-report=html --cov-report=term

# 運行代碼格式化
format:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🎨 格式化 Python 代碼..."
    {{uv_run}} black src/ tests/ scripts/ run.py
    echo "✅ 代碼格式化完成"

# 運行代碼檢查
lint:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🔍 檢查代碼品質..."
    echo "📋 運行 flake8..."
    {{uv_run}} flake8 src/ tests/ scripts/
    echo "📋 運行 mypy..."
    {{uv_run}} mypy src/ --ignore-missing-imports
    echo "✅ 代碼檢查完成"

# 更新依賴鎖定文件
freeze:
    #!/usr/bin/env bash
    echo "📦 更新依賴鎖定文件..."
    uv lock
    echo "✅ uv.lock 已更新"
    echo "💡 依賴現在由 pyproject.toml 和 uv.lock 管理"

# 安裝新的依賴包
install PACKAGE:
    #!/usr/bin/env bash
    echo "📦 安裝依賴包: {{PACKAGE}}"
    uv add {{PACKAGE}}
    echo "✅ {{PACKAGE}} 安裝完成並已更新 pyproject.toml"

# 安裝開發依賴包
install-dev PACKAGE:
    #!/usr/bin/env bash
    echo "📦 安裝開發依賴包: {{PACKAGE}}"
    uv add --dev {{PACKAGE}}
    echo "✅ {{PACKAGE}} 安裝完成並已更新 pyproject.toml"

# 🐳 Docker 開發命令
# 構建 Docker 開發鏡像
docker-build:
    #!/usr/bin/env bash
    echo "🐳 構建 Docker 開發鏡像..."
    {{docker_compose}} build fastapi-app

# 構建 Docker 生產鏡像
docker-build-prod:
    #!/usr/bin/env bash
    echo "🐳 構建 Docker 生產鏡像..."
    {{docker_compose}} -f docker/docker-compose.prod.yml build fastapi-prod

# 啟動 Docker 開發環境
docker-dev:
    #!/usr/bin/env bash
    echo "🐳 啟動 Docker 開發環境..."
    echo "📖 API 文檔: http://localhost:8000/docs"
    {{docker_compose}} -f docker/docker-compose.override.yml up fastapi-app

# 後台啟動 Docker 開發環境
docker-dev-bg:
    #!/usr/bin/env bash
    echo "🐳 後台啟動 Docker 開發環境..."
    {{docker_compose}} -f docker/docker-compose.override.yml up -d fastapi-app
    echo "✅ 服務已在後台啟動"
    echo "📖 API 文檔: http://localhost:8000/docs"

# 在 Docker 中運行測試
docker-test:
    #!/usr/bin/env bash
    echo "🧪 在 Docker 中運行測試..."
    {{docker_compose}} --profile testing run --rm fastapi-test

# 進入 Docker 容器 shell
docker-shell:
    #!/usr/bin/env bash
    echo "🐚 進入 Docker 容器..."
    {{docker_compose}} exec fastapi-app bash

# 查看 Docker 服務日誌
docker-logs:
    #!/usr/bin/env bash
    echo "📋 查看 Docker 服務日誌..."
    {{docker_compose}} logs -f fastapi-app

# 停止 Docker 服務
docker-stop:
    #!/usr/bin/env bash
    echo "🛑 停止 Docker 服務..."
    {{docker_compose}} down

# 停止並清理 Docker 資源
docker-clean:
    #!/usr/bin/env bash
    echo "🧹 停止並清理 Docker 資源..."
    {{docker_compose}} down --volumes --remove-orphans
    echo "🗑️ 清理未使用的 Docker 鏡像..."
    docker image prune -f

# 🌟 GitHub Codespaces 命令
# 設置 GitHub Codespaces 開發環境
codespaces-setup:
    #!/usr/bin/env bash
    echo "🚀 設置 FastAPI Codespaces 開發環境..."
    
    # 檢查是否在 Codespaces 中
    if [ "$CODESPACES" = "true" ]; then
        echo "📍 檢測到 GitHub Codespaces 環境"
        
        # 安裝 Just（如果尚未安裝）
        if ! command -v just >/dev/null 2>&1; then
            echo "📦 安裝 Just 命令工具..."
            curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin
        fi
        
        # 安裝 uv（如果尚未安裝）
        if ! command -v uv >/dev/null 2>&1; then
            echo "📦 安裝 uv 包管理器..."
            curl -LsSf https://astral.sh/uv/install.sh | sh
            source ~/.bashrc
        fi
        
        # 設置 Git 配置（如果需要）
        if [ -n "$GITHUB_USER" ] && [ -z "$(git config --global user.name)" ]; then
            echo "🔧 配置 Git 用戶信息..."
            git config --global user.name "$GITHUB_USER"
            git config --global user.email "$GITHUB_USER@users.noreply.github.com"
        fi
        
        # 創建 Codespaces 特定的環境文件
        if [ ! -f .env ]; then
            echo "📝 創建 Codespaces 環境配置..."
            echo "# Codespaces 環境配置" > .env
            echo "DEBUG=true" >> .env
            echo "LOG_LEVEL=info" >> .env
            echo "HOST=0.0.0.0" >> .env
            echo "PORT=8000" >> .env
            echo "RELOAD=true" >> .env
            echo "ENABLE_AUTO_TEST=false" >> .env
            echo "" >> .env
            echo "# Codespaces 特定設置" >> .env
            echo "CODESPACES=true" >> .env
            echo "ENVIRONMENT=codespaces" >> .env
        fi
    else
        echo "📍 本地開發環境"
        if [ ! -f .env ]; then
            cp .env.example .env
        fi
    fi
    
    # 通用設置
    echo "📦 同步 Python 依賴 (使用 uv)..."
    uv sync --dev
    
    # 創建必要的目錄
    mkdir -p logs
    
    # 驗證安裝
    echo "🧪 驗證環境設置..."
    python -c "from src.app.main import app; print('✅ FastAPI 應用導入成功')"
    
    # 顯示有用信息
    echo ""
    echo "🎉 FastAPI Codespaces 環境設置完成！"
    echo ""
    echo "📋 快速開始："
    echo "  just dev          # 啟動開發服務器"
    echo "  just test-unit    # 運行單元測試"
    echo "  just docker-dev   # Docker 開發環境"
    echo ""
    echo "📖 API 文檔: http://localhost:8000/docs"
    echo "🔍 項目狀態: just status"

# 在 GitHub Codespaces 中啟動 FastAPI 應用
codespaces-start:
    #!/usr/bin/env bash
    if [ "$CODESPACES" = "true" ]; then
        echo "🌟 在 GitHub Codespaces 中啟動 FastAPI..."
        echo "📍 Codespace URL: $CODESPACE_NAME.github.dev"
        echo "📖 API 文檔將在: https://$CODESPACE_NAME-8000.app.github.dev/docs"
        echo ""
        python run.py
    else
        echo "⚠️ 這個命令只能在 GitHub Codespaces 中使用"
        echo "💡 在本地環境請使用: just dev"
    fi

# 檢查 GitHub Codespaces 環境狀態
codespaces-status:
    #!/usr/bin/env bash
    echo "📊 GitHub Codespaces 環境狀態："
    echo ""
    if [ "$CODESPACES" = "true" ]; then
        echo "✅ 環境: GitHub Codespaces"
        echo "📍 Codespace: $CODESPACE_NAME"
        echo "🌐 URL: https://$CODESPACE_NAME.github.dev"
        echo "🔧 機器類型: $(echo $CODESPACE_MACHINE_DISPLAY_NAME || echo 'Unknown')"
        echo ""
        echo "🐍 Python 版本: $(python --version)"
        echo "📦 Just 版本: $(just --version 2>/dev/null || echo 'Not installed')"
        echo "🐳 Docker 版本: $(docker --version 2>/dev/null || echo 'Not available')"
        echo ""
        echo "📂 工作目錄: $(pwd)"
        echo "💾 磁盤使用: $(df -h . | tail -1 | awk '{print $3 "/" $2 " (" $5 ")"}')"
        echo ""
        echo "🚀 快速命令："
        echo "  just codespaces-start  # 啟動 FastAPI 服務器"
        echo "  just dev              # 開發模式（推薦）"
        echo "  just test-unit        # 運行測試"
    else
        echo "❌ 當前不在 GitHub Codespaces 環境中"
        echo "💡 這個命令只能在 Codespaces 中使用"
    fi

# 重置 GitHub Codespaces 環境
codespaces-reset:
    #!/usr/bin/env bash
    if [ "$CODESPACES" = "true" ]; then
        echo "🔄 重置 Codespaces 環境..."
        echo "⚠️ 這將清理所有臨時文件和緩存"
        read -p "確定要繼續嗎？(y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "🧹 清理 Python 緩存..."
            find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
            find . -type f -name "*.pyc" -delete 2>/dev/null || true
            
            echo "🧹 清理日誌文件..."
            rm -rf logs/*.log 2>/dev/null || true
            
            echo "🔄 重新同步依賴..."
            uv sync --dev
            
            echo "✅ Codespaces 環境重置完成！"
            echo "💡 運行 'just codespaces-status' 檢查狀態"
        else
            echo "❌ 重置已取消"
        fi
    else
        echo "⚠️ 這個命令只能在 GitHub Codespaces 中使用"
    fi

# 📋 信息查看
# 檢查項目狀態
status:
    #!/usr/bin/env bash
    echo "📋 FastAPI 項目狀態："
    echo ""
    
    # 檢查虛擬環境
    if [ -d "{{venv_dir}}" ]; then
        echo "✅ 虛擬環境: 已創建 (uv 管理)"
        echo "📍 Python 版本: $({{venv_python}} --version 2>/dev/null || echo '未知')"
        echo "📦 uv 版本: $(uv --version 2>/dev/null || echo '未安裝')"
    else
        echo "❌ 虛擬環境: 未創建"
        echo "💡 運行 'just setup' 創建虛擬環境"
    fi
    
    # 檢查舊環境
    if [ -d "fastapi_env" ]; then
        echo "⚠️ 發現舊的 fastapi_env 環境，建議清理"
        echo "💡 運行 'just clean' 清理舊環境"
    fi
    
    echo ""
    
    # 檢查關鍵文件
    echo "📁 項目文件檢查："
    FILES=("src/app/main.py" "requirements/base.txt" "Dockerfile" ".env.example")
    for file in "${FILES[@]}"; do
        if [ -f "$file" ]; then
            echo "✅ $file"
        else
            echo "❌ $file (缺失)"
        fi
    done
    
    echo ""
    
    # 檢查環境
    if [ "$CODESPACES" = "true" ]; then
        echo "🌟 環境: GitHub Codespaces"
        echo "📍 Codespace: $CODESPACE_NAME"
    else
        echo "💻 環境: 本地開發"
    fi
    
    # 檢查端口
    if command -v lsof >/dev/null 2>&1; then
        if lsof -i :8000 >/dev/null 2>&1; then
            echo "🚀 端口 8000: 使用中 (可能有服務在運行)"
        else
            echo "🔌 端口 8000: 可用"
        fi
    fi
    
    echo ""
    echo "💡 下一步建議："
    if [ ! -d "{{venv_dir}}" ]; then
        echo "  1. 運行 'just setup' 設置環境"
        echo "  2. 運行 'just dev' 啟動開發服務器"
    else
        echo "  1. 運行 'just dev' 啟動開發服務器"
        echo "  2. 運行 'just test-unit' 執行測試"
        echo "  3. 訪問 http://localhost:8000/docs 查看 API 文檔"
    fi

# 顯示項目信息
info:
    #!/usr/bin/env bash
    echo "📊 FastAPI 項目信息"
    echo "===================="
    echo ""
    echo "📋 項目詳情："
    echo "  名稱: FastAPI 初級快速入門實作"
    echo "  版本: $(grep version pyproject.toml | cut -d'"' -f2 2>/dev/null || echo '未知')"
    echo "  Python: $(python3 --version)"
    echo "  Just: $(just --version)"
    echo ""
    echo "📁 項目結構："
    echo "  src/           - 源代碼"
    echo "  tests/         - 測試文件"
    echo "  scripts/       - 開發腳本"
    echo "  docker/        - Docker 配置"
    echo "  docs/          - 項目文檔"
    echo "  requirements/  - 依賴管理"
    echo ""
    echo "🔗 有用的鏈接："
    echo "  API 文檔: http://localhost:8000/docs"
    echo "  項目文檔: docs/README.md"
    echo "  GitHub: .github/workflows/"
    echo ""
    echo "🚀 快速命令："
    echo "  just help      - 查看所有命令"
    echo "  just status    - 檢查項目狀態"
    echo "  just dev       - 啟動開發服務器"

# 🧹 清理和維護
# 清理虛擬環境
clean:
    #!/usr/bin/env bash
    echo "🧹 清理虛擬環境..."
    if [ -d "{{venv_dir}}" ]; then
        rm -rf {{venv_dir}}
        echo "✅ uv 虛擬環境已刪除"
    fi
    if [ -d "fastapi_env" ]; then
        rm -rf fastapi_env
        echo "✅ 舊的 fastapi_env 虛擬環境已刪除"
    fi

# 清理 Python 緩存文件
clean-cache:
    #!/usr/bin/env bash
    echo "🧹 清理 Python 緩存文件..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    echo "✅ Python 緩存文件已清理"

# 清理所有臨時文件和緩存
clean-all: clean clean-cache
    #!/usr/bin/env bash
    echo "🧹 清理所有臨時文件..."
    rm -rf .pytest_cache/ 2>/dev/null || true
    rm -rf htmlcov/ 2>/dev/null || true
    rm -rf .coverage 2>/dev/null || true
    rm -rf logs/*.log 2>/dev/null || true
    echo "✅ 所有臨時文件已清理"

# 重新安裝所有依賴
reinstall: clean
    #!/usr/bin/env bash
    echo "🔄 重新安裝項目環境..."
    uv sync --dev
    echo "✅ 項目環境重新安裝完成"

# 🚀 快速開始命令
# 一鍵設置並運行應用
start: setup run

# 一鍵設置並啟動開發模式
dev-start: setup dev

# 一鍵 Docker 開發環境
docker-start: docker-build docker-dev-bg

# 🐳 容器引擎管理
# 設置使用 Podman
use-podman:
    #!/usr/bin/env bash
    echo "🐳 設置使用 Podman 作為容器引擎..."
    echo "export CONTAINER_ENGINE=podman" >> ~/.zshrc
    echo "export DOCKER_HOST=unix:///var/run/docker.sock" >> ~/.zshrc
    echo "✅ 已設置 Podman 為默認容器引擎"
    echo "💡 請重新啟動終端或執行: source ~/.zshrc"

# 設置使用 Docker
use-docker:
    #!/usr/bin/env bash
    echo "🐳 設置使用 Docker 作為容器引擎..."
    echo "export CONTAINER_ENGINE=docker" >> ~/.zshrc
    echo "✅ 已設置 Docker 為默認容器引擎"
    echo "💡 請重新啟動終端或執行: source ~/.zshrc"

# 檢查容器引擎狀態
container-status:
    #!/usr/bin/env bash
    echo "🔍 容器引擎狀態檢查："
    echo "  當前設置: podman (通過 DOCKER_HOST)"
    echo ""
    if command -v podman >/dev/null 2>&1; then
        echo "📦 Podman:"
        echo "  版本: $(podman --version)"
        echo "  狀態: $(podman machine list 2>/dev/null | grep -v NAME | head -1 | awk '{print $1 ": " $4 " " $5}' || echo '未運行')"
    else
        echo "📦 Podman: 未安裝"
    fi
    echo ""
    if command -v docker >/dev/null 2>&1; then
        echo "🐳 Docker:"
        echo "  版本: $(docker --version)"
        echo "  狀態: $(docker info >/dev/null 2>&1 && echo '運行中' || echo '未運行')"
    else
        echo "🐳 Docker: 未安裝"
    fi

# 🧪 CI/CD 測試命令
# 運行完整 CI/CD 流程測試
test-ci-cd:
    #!/usr/bin/env bash
    echo "🚀 開始 CI/CD 流程測試..."
    if [ -f "./scripts/test_ci_cd.sh" ]; then
        ./scripts/test_ci_cd.sh
    else
        echo "❌ 測試腳本不存在: ./scripts/test_ci_cd.sh"
        exit 1
    fi

# 測試 Feature CI 流程
test-feature-ci:
    #!/usr/bin/env bash
    echo "🔧 測試 Feature CI 流程..."
    if [ -f "./scripts/test_ci_cd.sh" ]; then
        ./scripts/test_ci_cd.sh feature
    else
        echo "❌ 測試腳本不存在: ./scripts/test_ci_cd.sh"
        exit 1
    fi

# 快速觸發 CI 測試
trigger-ci:
    #!/usr/bin/env bash
    echo "⚡ 快速觸發 CI 測試..."
    current_branch=$(git branch --show-current)
    test_branch="feature/quick-ci-test-$(date +%s)"
    
    echo "📝 創建測試分支: $test_branch"
    git checkout -b "$test_branch"
    git commit --allow-empty -m "feat: trigger CI test - $(date)"
    git push origin "$test_branch"
    
    echo "✅ CI 測試已觸發"
    echo "🔗 查看結果: https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[:/]\([^.]*\).*/\1/')/actions"
    
    git checkout "$current_branch"

# 測試修復後的 CI/CD 部署
test-deployment-fix:
    #!/usr/bin/env bash
    echo "🔧 測試 Codespaces 部署修復..."
    current_branch=$(git branch --show-current)
    
    # 檢查是否有未提交的變更
    if ! git diff --quiet || ! git diff --cached --quiet; then
        echo "⚠️ 發現未提交的變更，正在提交..."
        git add -A
        git commit -m "fix: resolve CD-Codespaces deployment issues - $(date)"
    else
        # 創建空提交來觸發 CI/CD
        git commit --allow-empty -m "fix: test CD-Codespaces deployment fix - $(date)"
    fi
    
    echo "📤 推送到當前分支: $current_branch"
    git push origin "$current_branch"
    
    echo "✅ 部署修復測試已觸發"
    echo ""
    echo "🔧 修復內容："
    echo "   CI 工作流程："
    echo "   - 移除了有權限問題的 workflow dispatch 觸發"
    echo "   - 改為通知 Codespaces 部署就緒"
    echo ""
    echo "   CD-Codespaces 工作流程："
    echo "   - 改進了 Docker 鏡像驗證邏輯"
    echo "   - 增強了錯誤處理和容錯性"
    echo "   - 修復了部署報告生成問題"
    echo ""
    echo "📋 預期結果："
    echo "   ✅ CI: 'Notify Codespaces Ready' 步驟應該成功"
    echo "   ✅ CD: 'Verify Codespaces Deployment' 應該更穩定"
    echo "   ✅ CD: 'Create Deployment Report' 應該成功"
    echo "   ✅ 不再出現權限錯誤"
    echo ""
    echo "🔗 查看結果: https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[:/]\([^.]*\).*/\1/')/actions"

# 檢查 CI/CD 狀態
check-ci-status:
    #!/usr/bin/env bash
    echo "📊 檢查 CI/CD 狀態..."
    echo ""
    echo "🔍 GitHub Actions 工作流程："
    echo "  - Feature Branch CI: 功能分支快速檢查"
    echo "  - CI/CD Pipeline: 完整 CI/CD 流程"  
    echo "  - CD - Deploy to GitHub Codespaces: 自動部署"
    echo ""
    echo "📋 本地檢查："
    
    # 檢查工作流程文件
    if [ -f ".github/workflows/feature-ci.yml" ]; then
        echo "  ✅ Feature CI 配置存在"
    else
        echo "  ❌ Feature CI 配置缺失"
    fi
    
    if [ -f ".github/workflows/ci.yml" ]; then
        echo "  ✅ 主要 CI 配置存在"
    else
        echo "  ❌ 主要 CI 配置缺失"
    fi
    
    if [ -f ".github/workflows/cd-codespaces.yml" ]; then
        echo "  ✅ CD 配置存在"
    else
        echo "  ❌ CD 配置缺失"
    fi
    
    # 檢查測試腳本
    if [ -f "scripts/test_ci_cd.sh" ]; then
        echo "  ✅ CI/CD 測試腳本存在"
    else
        echo "  ❌ CI/CD 測試腳本缺失"
    fi
    
    echo ""
    echo "🚀 快速測試命令："
    echo "  just trigger-ci      # 快速觸發 CI"
    echo "  just test-feature-ci # 測試 Feature CI"
    echo "  just test-ci-cd      # 完整 CI/CD 測試"

# 📚 顯示詳細的幫助信息
help:
    @echo "🚀 FastAPI 項目管理命令完整指南"
    @echo ""
    @echo "📋 基本命令："
    @echo "  just setup          - 創建虛擬環境並安裝依賴"
    @echo "  just run            - 運行 FastAPI 應用"
    @echo "  just dev            - 開發模式運行（熱重載）"
    @echo "  just start          - 一鍵設置並運行"
    @echo "  just status         - 檢查項目狀態"
    @echo ""
    @echo "🧪 測試和品質命令："
    @echo "  just test           - 運行 API 功能測試"
    @echo "  just test-unit      - 運行單元測試"
    @echo "  just test-coverage  - 運行測試並生成覆蓋率報告"
    @echo "  just format         - 格式化 Python 代碼"
    @echo "  just lint           - 檢查代碼品質"
    @echo ""
    @echo "📦 依賴管理："
    @echo "  just install <pkg>  - 安裝新的依賴包"
    @echo "  just freeze         - 更新 requirements 文件"
    @echo "  just reinstall      - 重新安裝所有依賴"
    @echo ""
    @echo "🐳 Docker 命令："
    @echo "  just docker-build   - 構建 Docker 開發鏡像"
    @echo "  just docker-dev     - 啟動 Docker 開發環境"
    @echo "  just docker-dev-bg  - 後台啟動 Docker 開發環境"
    @echo "  just docker-test    - 在 Docker 中運行測試"
    @echo "  just docker-shell   - 進入 Docker 容器 shell"
    @echo "  just docker-logs    - 查看 Docker 服務日誌"
    @echo "  just docker-stop    - 停止 Docker 服務"
    @echo "  just docker-clean   - 停止並清理 Docker 資源"
    @echo "  just docker-start   - Docker 一鍵開發環境"
    @echo ""
    @echo "🌟 GitHub Codespaces 命令："
    @echo "  just codespaces-setup  - 設置 Codespaces 環境"
    @echo "  just codespaces-start  - 在 Codespaces 中啟動應用"
    @echo "  just codespaces-status - 檢查 Codespaces 環境狀態"
    @echo "  just codespaces-reset  - 重置 Codespaces 環境"
    @echo ""
    @echo "🐳 容器引擎管理："
    @echo "  just use-podman       - 設置使用 Podman"
    @echo "  just use-docker       - 設置使用 Docker"
    @echo "  just container-status - 檢查容器引擎狀態"
    @echo ""
    @echo "🧹 清理命令："
    @echo "  just clean          - 清理虛擬環境"
    @echo "  just clean-cache    - 清理 Python 緩存文件"
    @echo "  just clean-all      - 清理所有臨時文件和緩存"
    @echo ""
    @echo "🧪 CI/CD 測試命令："
    @echo "  just trigger-ci          - 快速觸發 CI 測試"
    @echo "  just test-deployment-fix - 測試 Codespaces 部署修復"
    @echo "  just test-feature-ci     - 測試 Feature CI 流程"
    @echo "  just test-ci-cd          - 運行完整 CI/CD 測試"
    @echo "  just check-ci-status     - 檢查 CI/CD 配置狀態"
    @echo ""
    @echo "🚀 快速開始組合命令："
    @echo "  just start          - 一鍵設置並運行應用"
    @echo "  just dev-start      - 一鍵設置並啟動開發模式"
    @echo "  just docker-start   - 一鍵 Docker 開發環境"
    @echo ""
    @echo "💡 提示："
    @echo "  - 運行 'just --list' 查看所有可用命令"
    @echo "  - 運行 'just <command>' 執行特定命令"
    @echo "  - 大部分命令會自動檢查環境並提供有用的錯誤信息"
    @echo ""
    @echo "📖 更多信息："
    @echo "  - API 文檔: http://localhost:8000/docs (啟動應用後)"
    @echo "  - 項目文檔: 查看 docs/ 目錄"
    @echo "  - GitHub: 查看 .github/workflows/ 了解 CI/CD"