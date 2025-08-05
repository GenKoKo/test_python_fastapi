# FastAPI 項目管理 - Just 命令集合
# 使用 just <command> 來執行各種項目任務

# 設定變數
python := "python3"
venv_dir := "fastapi_env"
venv_python := venv_dir + "/bin/python"
venv_pip := venv_dir + "/bin/pip"
# 容器引擎設定 (支援 Docker 和 Podman)
# 使用 Podman 作為默認容器引擎
docker_compose := "DOCKER_HOST=unix:///var/run/docker.sock docker-compose -f docker/docker-compose.yml"

# 預設命令：顯示所有可用命令
default:
    @just --list

# 🚀 開發環境設置
# 創建並設置虛擬環境
setup:
    #!/usr/bin/env bash
    echo "🚀 開始設置 FastAPI 虛擬環境..."
    echo "📋 檢查 Python 版本..."
    {{python}} --version
    echo "📦 創建虛擬環境..."
    {{python}} -m venv {{venv_dir}}
    echo "🔄 升級 pip..."
    {{venv_pip}} install --upgrade pip
    echo "📚 安裝項目依賴..."
    {{venv_pip}} install -r requirements.txt
    echo "✅ 虛擬環境設置完成！"

# 🏃 運行應用
run:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🚀 啟動 FastAPI 應用..."
    {{venv_python}} run.py

# 🔧 開發模式運行
dev:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🔧 開發模式啟動 FastAPI 應用..."
    {{venv_dir}}/bin/uvicorn src.app.main:app --reload --host 127.0.0.1 --port 8000

# 🧪 測試相關命令
test:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🧪 運行 API 功能測試..."
    {{venv_python}} tools/test_api.py

test-unit:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🧪 運行單元測試..."
    {{venv_python}} -m pytest tests/ -v

test-coverage:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "📊 運行測試並生成覆蓋率報告..."
    {{venv_python}} -m pytest tests/ --cov=src --cov-report=html --cov-report=term

# 🐳 Docker 開發命令
docker-build:
    #!/usr/bin/env bash
    echo "🐳 構建 Docker 開發鏡像..."
    {{docker_compose}} build fastapi-app

docker-build-prod:
    #!/usr/bin/env bash
    echo "🐳 構建 Docker 生產鏡像..."
    {{docker_compose}} -f docker/docker-compose.prod.yml build fastapi-prod

docker-dev:
    #!/usr/bin/env bash
    echo "🐳 啟動 Docker 開發環境..."
    echo "📖 API 文檔: http://localhost:8000/docs"
    {{docker_compose}} -f docker/docker-compose.override.yml up fastapi-app

docker-dev-bg:
    #!/usr/bin/env bash
    echo "🐳 後台啟動 Docker 開發環境..."
    {{docker_compose}} -f docker/docker-compose.override.yml up -d fastapi-app
    echo "✅ 服務已在後台啟動"
    echo "📖 API 文檔: http://localhost:8000/docs"

docker-test:
    #!/usr/bin/env bash
    echo "🧪 在 Docker 中運行測試..."
    {{docker_compose}} --profile testing run --rm fastapi-test

docker-shell:
    #!/usr/bin/env bash
    echo "🐚 進入 Docker 容器..."
    {{docker_compose}} exec fastapi-app bash

docker-logs:
    #!/usr/bin/env bash
    echo "📋 查看 Docker 服務日誌..."
    {{docker_compose}} logs -f fastapi-app

docker-stop:
    #!/usr/bin/env bash
    echo "🛑 停止 Docker 服務..."
    {{docker_compose}} down

docker-clean:
    #!/usr/bin/env bash
    echo "🧹 停止並清理 Docker 資源..."
    {{docker_compose}} down --volumes --remove-orphans
    echo "🗑️ 清理未使用的 Docker 鏡像..."
    docker image prune -f

# 🌟 GitHub Codespaces 命令
codespaces-setup:
    #!/usr/bin/env bash
    echo "🚀 設置 FastAPI Codespaces 開發環境..."
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install black flake8 mypy pytest-cov
    mkdir -p logs
    if [ ! -f .env ]; then
        cp config/env/.env.docker .env
    fi
    echo "✅ FastAPI Codespaces 環境設置完成！"

codespaces-start:
    #!/usr/bin/env bash
    if [ "$CODESPACES" = "true" ]; then
        echo "🌟 在 GitHub Codespaces 中啟動 FastAPI..."
        python run.py
    else
        echo "⚠️ 這個命令只能在 GitHub Codespaces 中使用"
    fi

# 📋 信息查看
status:
    #!/usr/bin/env bash
    echo "📋 FastAPI 項目狀態："
    if [ -d "{{venv_dir}}" ]; then
        echo "✅ 虛擬環境: 已創建"
        echo "📍 Python 版本: $({{venv_python}} --version)"
    else
        echo "❌ 虛擬環境: 未創建"
    fi

# 🧹 清理和維護
clean:
    #!/usr/bin/env bash
    echo "🧹 清理虛擬環境..."
    if [ -d "{{venv_dir}}" ]; then
        rm -rf {{venv_dir}}
        echo "✅ 虛擬環境已刪除"
    fi

clean-cache:
    #!/usr/bin/env bash
    echo "🧹 清理 Python 緩存文件..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    echo "✅ Python 緩存文件已清理"

# 🚀 快速開始命令
start: setup run
dev-start: setup dev
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

# 📚 幫助信息
help:
    @echo "🚀 FastAPI 項目管理命令"
    @echo ""
    @echo "📋 基本命令："
    @echo "  just setup          - 創建虛擬環境並安裝依賴"
    @echo "  just run            - 運行 FastAPI 應用"
    @echo "  just dev            - 開發模式運行（熱重載）"
    @echo "  just start          - 一鍵設置並運行"
    @echo ""
    @echo "🧪 測試命令："
    @echo "  just test           - 運行 API 功能測試"
    @echo "  just test-unit      - 運行單元測試"
    @echo "  just test-coverage  - 運行測試並生成覆蓋率報告"
    @echo ""
    @echo "🐳 Docker 命令："
    @echo "  just docker-build   - 構建 Docker 開發鏡像"
    @echo "  just docker-dev     - 啟動 Docker 開發環境"
    @echo "  just docker-test    - 在 Docker 中運行測試"
    @echo "  just docker-start   - Docker 一鍵開發環境"
    @echo ""
    @echo "🌟 GitHub Codespaces 命令："
    @echo "  just codespaces-setup - 設置 Codespaces 環境"
    @echo "  just codespaces-start - 在 Codespaces 中啟動應用"
    @echo ""
    @echo "🐳 容器引擎管理："
    @echo "  just use-podman       - 設置使用 Podman"
    @echo "  just use-docker       - 設置使用 Docker"
    @echo "  just container-status - 檢查容器引擎狀態"
    @echo ""
    @echo "💡 提示: 運行 'just --list' 查看所有可用命令"