# FastAPI 項目管理 - Just 命令集合
# 使用 just <command> 來執行各種項目任務

# 設定變數
python := "python3"
venv_dir := "fastapi_env"
venv_python := venv_dir + "/bin/python"
venv_pip := venv_dir + "/bin/pip"

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
    echo ""
    echo "🎯 接下來可以使用的命令："
    echo "  just run    - 運行應用"
    echo "  just test   - 運行測試"
    echo "  just dev    - 開發模式運行"
    echo "  just clean  - 清理環境"

# 🏃 運行應用
# 在虛擬環境中啟動 FastAPI 應用
run:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🚀 啟動 FastAPI 應用..."
    echo "📖 API 文檔將在 http://127.0.0.1:8000/docs 可用"
    echo "🧪 服務器啟動後會自動運行 API 測試"
    echo "🛑 按 Ctrl+C 停止服務器"
    echo ""
    {{venv_python}} run.py

# 🔧 開發模式運行
# 使用 uvicorn 直接運行，支援熱重載
dev:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🔧 開發模式啟動 FastAPI 應用..."
    echo "🔄 已啟用熱重載功能"
    echo "📖 API 文檔: http://127.0.0.1:8000/docs"
    {{venv_dir}}/bin/uvicorn src.app.main:app --reload --host 127.0.0.1 --port 8000

# 🧪 測試相關命令
# 運行 API 功能測試
test:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🧪 運行 API 功能測試..."
    echo "📝 注意: 請確保 FastAPI 服務器正在運行"
    {{venv_python}} tools/test_api.py

# 運行單元測試
test-unit:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🧪 運行單元測試..."
    {{venv_python}} -m pytest tests/ -v

# 運行測試並生成覆蓋率報告
test-coverage:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "📊 運行測試並生成覆蓋率報告..."
    {{venv_python}} -m pytest tests/ --cov=src --cov-report=html --cov-report=term

# 測試項目結構
test-structure:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🏗️ 測試項目結構..."
    {{venv_python}} tools/test_new_structure.py

# 測試配置系統
test-config:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "⚙️ 測試配置系統..."
    {{venv_python}} tools/test_config.py

# 📦 依賴管理
# 安裝新的依賴包
install package:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "📦 安裝依賴包: {{package}}"
    {{venv_pip}} install {{package}}
    echo "💾 更新 requirements.txt..."
    {{venv_pip}} freeze > requirements.txt

# 更新所有依賴
update-deps:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🔄 更新所有依賴..."
    {{venv_pip}} install --upgrade pip
    {{venv_pip}} install -r requirements.txt --upgrade

# 生成 requirements.txt
freeze:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "💾 生成 requirements.txt..."
    {{venv_pip}} freeze > requirements.txt
    echo "✅ requirements.txt 已更新"

# 🧹 清理和維護
# 清理虛擬環境
clean:
    #!/usr/bin/env bash
    echo "🧹 清理虛擬環境..."
    if [ -d "{{venv_dir}}" ]; then
        rm -rf {{venv_dir}}
        echo "✅ 虛擬環境已刪除"
    else
        echo "ℹ️ 虛擬環境不存在，無需清理"
    fi

# 清理 Python 緩存文件
clean-cache:
    #!/usr/bin/env bash
    echo "🧹 清理 Python 緩存文件..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    find . -type f -name "*.pyo" -delete 2>/dev/null || true
    find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
    echo "✅ Python 緩存文件已清理"

# 完全重置環境
reset: clean clean-cache setup
    echo "🔄 環境重置完成！"

# 📋 信息查看
# 顯示虛擬環境狀態
status:
    #!/usr/bin/env bash
    echo "📋 FastAPI 項目狀態："
    echo ""
    if [ -d "{{venv_dir}}" ]; then
        echo "✅ 虛擬環境: 已創建"
        echo "📍 Python 版本: $({{venv_python}} --version)"
        echo "📦 已安裝套件數量: $({{venv_pip}} list | wc -l)"
    else
        echo "❌ 虛擬環境: 未創建"
        echo "💡 運行 'just setup' 來創建虛擬環境"
    fi
    echo ""
    echo "📁 項目文件："
    echo "  - 源代碼: src/"
    echo "  - 測試文件: tests/"
    echo "  - 工具腳本: tools/"
    echo "  - 文檔: docs/"

# 顯示已安裝的套件
list-packages:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "📦 已安裝的套件："
    {{venv_pip}} list

# 🔍 開發工具
# 代碼格式化 (需要安裝 black)
format:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🎨 格式化 Python 代碼..."
    if {{venv_pip}} show black > /dev/null 2>&1; then
        {{venv_python}} -m black src/ tests/ tools/
        echo "✅ 代碼格式化完成"
    else
        echo "⚠️ black 未安裝，運行 'just install black' 來安裝"
    fi

# 代碼風格檢查 (需要安裝 flake8)
lint:
    #!/usr/bin/env bash
    if [ ! -d "{{venv_dir}}" ]; then
        echo "❌ 虛擬環境不存在，請先運行: just setup"
        exit 1
    fi
    echo "🔍 檢查代碼風格..."
    if {{venv_pip}} show flake8 > /dev/null 2>&1; then
        {{venv_python}} -m flake8 src/ tests/ tools/
        echo "✅ 代碼風格檢查完成"
    else
        echo "⚠️ flake8 未安裝，運行 'just install flake8' 來安裝"
    fi

# 🚀 快速開始命令
# 一鍵設置並運行
start: setup run

# 開發者快速開始
dev-start: setup dev

# 📚 幫助信息
# 顯示詳細幫助
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
    @echo "  just test-structure - 測試項目結構"
    @echo "  just test-config    - 測試配置系統"
    @echo ""
    @echo "📦 依賴管理："
    @echo "  just install <pkg>  - 安裝新的依賴包"
    @echo "  just update-deps    - 更新所有依賴"
    @echo "  just freeze         - 生成 requirements.txt"
    @echo "  just list-packages  - 顯示已安裝套件"
    @echo ""
    @echo "🧹 清理命令："
    @echo "  just clean          - 清理虛擬環境"
    @echo "  just clean-cache    - 清理 Python 緩存"
    @echo "  just reset          - 完全重置環境"
    @echo ""
    @echo "🔍 開發工具："
    @echo "  just format         - 代碼格式化"
    @echo "  just lint           - 代碼風格檢查"
    @echo "  just status         - 顯示項目狀態"
    @echo ""
    @echo "💡 提示: 運行 'just --list' 查看所有可用命令"