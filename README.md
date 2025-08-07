# 🚀 FastAPI 現代化開發項目

[![CI/CD Pipeline](https://github.com/your-username/fastapi-project/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/your-username/fastapi-project/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Codespaces](https://img.shields.io/badge/Codespaces-Ready-181717.svg)](https://github.com/codespaces)
[![Just](https://img.shields.io/badge/Just-1.42.4-FF6B6B.svg)](https://github.com/casey/just)
[![uv](https://img.shields.io/badge/uv-0.8.5-4B8BBE.svg)](https://github.com/astral-sh/uv)

這是一個完全現代化的 FastAPI 項目，展示了 Python Web 開發的最佳實踐、企業級架構設計和完整的 DevOps 流程。項目經過完整重構和優化，採用標準化結構，支持多種開發和部署方式，並解決了 Codespaces 環境中的常見問題。

## ✨ 項目特色

### 🏗️ 現代化架構

-   ✅ **標準化項目結構** - 符合 Python 最佳實踐
-   ✅ **模塊化設計** - 清晰的分層架構
-   ✅ **無符號連結** - 跨平台完美兼容
-   ✅ **現代配置管理** - pyproject.toml + uv 包管理
-   ✅ **環境配置優化** - Pydantic Settings + 環境變數管理

### 🚀 核心功能

-   ✅ **完整的 CRUD API** - 商品和用戶管理
-   ✅ **自動 API 文檔** - Swagger/OpenAPI 支持
-   ✅ **數據驗證** - Pydantic 模型驗證
-   ✅ **中間件支持** - 請求追蹤和日誌記錄
-   ✅ **線程安全** - 內存數據庫實現

### 🛠️ 開發體驗

-   ✅ **Just 命令管理** - 統一的項目管理工具，解決 Codespaces 安裝問題
-   ✅ **多種開發方式** - 本地/Docker/Codespaces，完全優化
-   ✅ **代碼品質工具** - Black/Flake8/MyPy 集成
-   ✅ **完整測試套件** - 單元測試 + 覆蓋率報告
-   ✅ **智能環境檢測** - 自動適配不同開發環境

### 🚀 DevOps 就緒

-   ✅ **CI/CD 流程** - GitHub Actions 自動化
-   ✅ **Docker 支持** - 開發/生產環境容器化
-   ✅ **Codespaces 優化** - 解決權限和 PATH 問題，一鍵雲端開發
-   ✅ **多容器引擎** - Docker/Podman 支持
-   ✅ **自動化腳本** - 簡化的安裝和配置流程

## 🚀 快速開始

### 方法一：GitHub Codespaces（推薦）⭐

最簡單的方式，無需本地安裝任何工具，已完全優化解決常見問題：

1. 點擊 GitHub 倉庫頁面的 **"Code"** 按鈕
2. 選擇 **"Codespaces"** 標籤
3. 點擊 **"Create codespace on main"**
4. 等待環境自動設置完成（約 2-3 分鐘）
5. 如果 Just 命令無法使用，執行：`source ~/.bashrc` 或 `bash scripts/fix-just-install.sh`
6. 運行 `just dev` 啟動開發服務器
7. 訪問 API 文檔：`https://your-codespace-8000.app.github.dev/docs`

#### 🔧 Codespaces 故障排除

如果遇到 `just: command not found` 錯誤：

```bash
# 方法 1: 重新載入環境
source ~/.bashrc

# 方法 2: 使用修復腳本
bash scripts/fix-just-install.sh

# 方法 3: 手動安裝
bash .devcontainer/install-just.sh
```

### 方法二：使用 Just 命令（本地開發）

#### 1. 安裝必要工具

```bash
# 安裝 uv (Python 包管理器)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安裝 Just 工具
# macOS (使用 Homebrew)
brew install just

# Linux (使用 cargo)
cargo install just

# Windows (使用 Scoop)
scoop install just
```

#### 2. 一鍵設置並運行

```bash
# 查看所有可用命令
just help

# 設置環境（使用 uv）
just setup

# 開發模式（熱重載）
just dev

# 一鍵設置並運行
just start
```

### 方法三：Docker 開發

```bash
# 一鍵 Docker 開發環境
just docker-start

# 或分步執行
just docker-build    # 構建鏡像
just docker-dev      # 啟動開發環境
```

### 方法四：傳統方式

```bash
# 使用 uv (推薦)
uv sync --dev
uv run python run.py

# 或使用傳統 venv
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# 或 .venv\Scripts\activate  # Windows

# 安裝依賴
pip install -r requirements/base.txt

# 運行應用
python run.py
## 📁 項目結構

```

fastapi-project/
├── 📁 src/ # 源代碼
│ ├── core/ # 核心配置和工具
│ │ ├── config.py # 環境配置管理
│ │ └── logger.py # 日誌系統
│ └── app/ # FastAPI 應用
│ ├── main.py # 應用入口
│ ├── models/ # 數據模型
│ ├── routers/ # API 路由
│ ├── services/ # 業務邏輯
│ └── utils/ # 工具函數
├── 📁 tests/ # 測試文件
├── 📁 scripts/ # 開發腳本
│ ├── fix-just-install.sh # Just 修復腳本
│ ├── test_api.py # API 測試腳本
│ └── ... # 其他開發腳本
├── 📁 docker/ # Docker 配置
├── 📁 docs/ # 項目文檔
├── 📁 requirements/ # 分層依賴管理
│ ├── base.txt # 基礎依賴
│ ├── dev.txt # 開發依賴
│ └── prod.txt # 生產依賴
├── 📁 .github/workflows/ # CI/CD 流程
├── 📁 .devcontainer/ # Codespaces 配置 (已優化)
│ ├── devcontainer.json # 主要容器配置
│ ├── setup.sh # 主要安裝腳本
│ ├── install-just.sh # Just 專用安裝腳本
│ ├── api-tests.http # API 測試文件
│ └── README.md # Codespaces 說明
├── 📄 pyproject.toml # 現代項目配置
├── 📄 uv.lock # uv 依賴鎖定文件
├── 📄 justfile # Just 命令定義
├── 📄 Dockerfile # Docker 鏡像

└── 📄 README.md # 項目文檔

````

## 🧪 測試和代碼品質

### 運行測試

```bash
# 單元測試
just test-unit

# 測試覆蓋率
just test-coverage

# API 功能測試
just test
````

### 代碼品質檢查

```bash
# 代碼格式化
just format

# 代碼檢查
just lint

# 完整品質檢查
just format && just lint && just test-unit
```

## 🔧 開發工具

### Just 命令概覽

```bash
# 基本命令
just setup          # 設置開發環境
just dev            # 開發模式運行
just test-unit      # 運行測試
just help           # 查看所有命令

# Docker 命令
just docker-build   # 構建 Docker 鏡像
just docker-dev     # 啟動 Docker 開發環境
just docker-test    # Docker 中運行測試

# Codespaces 命令
just codespaces-setup   # 設置 Codespaces 環境
just codespaces-status  # 檢查環境狀態
```

### 依賴管理 (使用 uv)

```bash
# 安裝新依賴
just install <package-name>
# 或直接使用 uv
uv add <package-name>

# 安裝開發依賴
just install-dev <package-name>
# 或直接使用 uv
uv add --dev <package-name>

# 更新依賴鎖定文件
just freeze
# 或直接使用 uv
uv lock

# 重新安裝所有依賴
just reinstall
# 或直接使用 uv
uv sync --dev
```

## � API 文檔

### 訪問方式

-   **Swagger UI**: http://localhost:8000/docs
-   **ReDoc**: http://localhost:8000/redoc
-   **OpenAPI JSON**: http://localhost:8000/openapi.json

### 主要端點

#### 商品管理

-   `GET /items/` - 獲取所有商品
-   `POST /items/` - 創建新商品
-   `GET /items/{item_id}` - 獲取特定商品
-   `PUT /items/{item_id}` - 更新商品
-   `DELETE /items/{item_id}` - 刪除商品
-   `GET /items/search/` - 搜索商品

#### 用戶管理

-   `GET /users/` - 獲取所有用戶
-   `POST /users/` - 創建新用戶
-   `GET /users/{user_id}` - 獲取特定用戶
-   `PUT /users/{user_id}` - 更新用戶
-   `DELETE /users/{user_id}` - 刪除用戶

#### 系統端點

-   `GET /` - 歡迎頁面
-   `GET /stats/health` - 健康檢查
-   `GET /stats/` - 系統統計

## 🚀 部署

### GitHub Codespaces（推薦）

項目支持自動部署到 GitHub Codespaces：

1. 推送代碼到 `main` 分支自動觸發 CD 流程
2. 自動構建 Codespaces 專用鏡像
3. 更新 devcontainer 配置
4. 觸發預構建優化

📖 **詳細指南**:

-   [GitHub Codespaces 完整部署指南](docs/CODESPACES_DEPLOYMENT_GUIDE.md)
-   [CI/CD 通知系統說明](docs/NOTIFICATION_SYSTEM.md)

### Docker 部署

```bash
# 生產環境部署
just docker-build-prod
docker-compose -f docker/docker-compose.prod.yml up -d
```

### 傳統部署

```bash
# 設置生產環境
pip install -r requirements/prod.txt
gunicorn src.app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 🔧 故障排除

### 常見問題和解決方案

#### 1. Codespaces 中 `just: command not found`

**問題**: 在 GitHub Codespaces 中無法使用 just 命令

**解決方案**:

```bash
# 方法 1: 重新載入環境配置
source ~/.bashrc

# 方法 2: 使用修復腳本
bash scripts/fix-just-install.sh

# 方法 3: 手動安裝
bash .devcontainer/install-just.sh

# 方法 4: 檢查 PATH
echo $PATH
export PATH="$HOME/.local/bin:$PATH"
```

#### 2. Pydantic 配置驗證錯誤

**問題**: `ValidationError: Extra inputs are not permitted`

**解決方案**:

```bash
# 檢查 .env 文件格式
cat .env

# 確保日誌級別使用大寫
LOG_LEVEL=INFO  # 不是 info

# 確保日誌格式正確
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

#### 3. 端口被占用

**問題**: `Address already in use` 錯誤

**解決方案**:

```bash
# 查找占用端口的進程
lsof -i :8000

# 終止進程
kill -9 <PID>

# 或使用不同端口
PORT=8001 just dev
```

#### 4. uv 同步失敗

**問題**: `uv sync` 命令失敗

**解決方案**:

```bash
# 清理並重新同步
rm -rf .venv
uv sync --dev

# 或使用傳統方式
pip install -r requirements/base.txt
```

#### 5. 測試失敗

**問題**: 單元測試執行失敗

**解決方案**:

```bash
# 檢查環境配置
just status

# 重新安裝依賴
just reinstall

# 清理緩存
just clean-cache

# 重新運行測試
just test-unit
```

### 🆘 獲取幫助

如果遇到其他問題：

1. **檢查項目狀態**: `just status`
2. **查看所有命令**: `just help`
3. **檢查環境配置**: `cat .env`
4. **查看日誌**: `tail -f logs/app.log`
5. **重置環境**: `just clean-all && just setup`

## 🤝 貢獻指南

### 開發流程

1. Fork 項目
2. 創建功能分支：`git checkout -b feature/amazing-feature`
3. 提交變更：`git commit -m 'Add amazing feature'`
4. 推送分支：`git push origin feature/amazing-feature`
5. 創建 Pull Request

### 代碼標準

```bash
# 代碼格式化
just format

# 代碼檢查
just lint

# 運行測試
just test-unit
```

### 提交規範

-   `feat:` 新功能
-   `fix:` 修復 bug
-   `docs:` 文檔更新
-   `style:` 代碼格式調整
-   `refactor:` 代碼重構
-   `test:` 測試相關
-   `chore:` 其他雜項

## 📚 學習資源

### 官方文檔

-   [FastAPI 官方文檔](https://fastapi.tiangolo.com/)
-   [Pydantic 文檔](https://pydantic-docs.helpmanual.io/)
-   [Uvicorn 文檔](https://www.uvicorn.org/)

### 進階學習

-   數據庫集成（SQLAlchemy）
-   用戶認證和授權
-   中間件開發
-   文件上傳處理
-   WebSocket 支持
-   背景任務處理

## 🛠️ 技術棧

### 核心框架

-   **FastAPI 0.115.0** - 現代 Python Web 框架
-   **Pydantic 2.9.2** - 數據驗證和序列化
-   **Uvicorn 0.30.6** - ASGI 服務器
-   **Python 3.11+** - 現代 Python 版本

### 開發工具

-   **uv 0.8.5** - 現代 Python 包管理器
-   **Just 1.42.4** - 現代命令執行器
-   **Black** - 代碼格式化
-   **Flake8** - 代碼檢查
-   **MyPy** - 類型檢查
-   **Pytest** - 測試框架

### DevOps

-   **Docker** - 容器化
-   **GitHub Actions** - CI/CD
-   **GitHub Codespaces** - 雲端開發環境

## 📄 許可證

本項目採用 MIT 許可證 - 查看 [LICENSE](LICENSE) 文件了解詳情。

## 🙏 致謝

-   [FastAPI](https://fastapi.tiangolo.com/) - 優秀的 Python Web 框架
-   [Just](https://github.com/casey/just) - 現代化的命令執行器
-   [GitHub Codespaces](https://github.com/features/codespaces) - 雲端開發環境

---

## 📊 項目狀態

-   ✅ **完全重構完成** - 標準化項目結構
-   ✅ **CI/CD 就緒** - 完整的自動化流程
-   ✅ **多環境支持** - 本地/Docker/Codespaces，完全優化
-   ✅ **文檔完整** - 詳細的使用指南和故障排除
-   ✅ **測試覆蓋** - 完整的測試套件
-   ✅ **Codespaces 優化** - 解決 Just 安裝和配置問題
-   ✅ **現代化工具鏈** - uv + Just + Pydantic Settings

## 🔧 最新改進 (2025-08-07)

### ✅ 已修復的問題

-   **Codespaces Just 安裝問題** - 權限和 PATH 環境變數問題
-   **Pydantic 配置驗證錯誤** - 環境變數和設定檔案衝突
-   **日誌格式錯誤** - 無效的日誌格式字串
-   **腳本結構優化** - 移除多餘的重複腳本

### 🚀 新增功能

-   **智能安裝腳本** - 自動檢測和修復環境問題
-   **故障排除指南** - 完整的問題解決方案
-   **簡化的腳本結構** - 清理多餘文件，提升維護性
-   **環境配置優化** - 更好的 Pydantic Settings 整合

**最後更新**: 2025-08-07  
**版本**: 1.1.0  
**狀態**: 生產就緒，Codespaces 完全優化 🚀
