# 🚀 FastAPI 現代化開發項目

[![CI/CD Pipeline](https://github.com/your-username/fastapi-project/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/your-username/fastapi-project/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Codespaces](https://img.shields.io/badge/Codespaces-Ready-181717.svg)](https://github.com/codespaces)

這是一個完全現代化的 FastAPI 項目，展示了 Python Web 開發的最佳實踐、企業級架構設計和完整的 DevOps 流程。項目經過完整重構，採用標準化結構，支持多種開發和部署方式。

## ✨ 項目特色

### 🏗️ 現代化架構

-   ✅ **標準化項目結構** - 符合 Python 最佳實踐
-   ✅ **模塊化設計** - 清晰的分層架構
-   ✅ **無符號連結** - 跨平台完美兼容
-   ✅ **現代配置管理** - pyproject.toml + 分層依賴

### 🚀 核心功能

-   ✅ **完整的 CRUD API** - 商品和用戶管理
-   ✅ **自動 API 文檔** - Swagger/OpenAPI 支持
-   ✅ **數據驗證** - Pydantic 模型驗證
-   ✅ **中間件支持** - 請求追蹤和日誌記錄
-   ✅ **線程安全** - 內存數據庫實現

### 🛠️ 開發體驗

-   ✅ **Just 命令管理** - 統一的項目管理工具
-   ✅ **多種開發方式** - 本地/Docker/Codespaces
-   ✅ **代碼品質工具** - Black/Flake8/MyPy 集成
-   ✅ **完整測試套件** - 單元測試 + 覆蓋率報告

### 🚀 DevOps 就緒

-   ✅ **CI/CD 流程** - GitHub Actions 自動化
-   ✅ **Docker 支持** - 開發/生產環境容器化
-   ✅ **Codespaces 部署** - 一鍵雲端開發環境
-   ✅ **多容器引擎** - Docker/Podman 支持

## 🚀 快速開始

### 方法一：GitHub Codespaces（推薦）⭐

最簡單的方式，無需本地安裝任何工具：

1. 點擊 GitHub 倉庫頁面的 **"Code"** 按鈕
2. 選擇 **"Codespaces"** 標籤
3. 點擊 **"Create codespace on main"**
4. 等待環境自動設置完成（約 2-3 分鐘）
5. 運行 `just dev` 啟動開發服務器
6. 訪問 API 文檔：`https://your-codespace-8000.app.github.dev/docs`

### 方法二：使用 Just 命令（本地開發）

#### 1. 安裝 Just 工具

```bash
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

# 設置環境並運行應用
just start

# 開發模式（熱重載）
just dev
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
# 創建虛擬環境
python -m venv fastapi_env
source fastapi_env/bin/activate  # Linux/macOS
# 或 fastapi_env\Scripts\activate  # Windows

# 安裝依賴
pip install -r requirements/base.txt

# 運行應用
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
├── 📁 docker/ # Docker 配置
├── 📁 docs/ # 項目文檔
├── 📁 requirements/ # 分層依賴管理
│ ├── base.txt # 基礎依賴
│ ├── dev.txt # 開發依賴
│ └── prod.txt # 生產依賴
├── 📁 .github/workflows/ # CI/CD 流程
├── 📁 .devcontainer/ # Codespaces 配置
├── 📄 pyproject.toml # 現代項目配置
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

### 依賴管理

```bash
# 安裝新依賴
just install <package-name>

# 更新 requirements 文件
just freeze

# 重新安裝所有依賴
just reinstall
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

### 開發工具

-   **Just** - 現代命令執行器
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
-   ✅ **多環境支持** - 本地/Docker/Codespaces
-   ✅ **文檔完整** - 詳細的使用指南
-   ✅ **測試覆蓋** - 完整的測試套件

**最後更新**: 2025-08-06  
**版本**: 1.0.0  
**狀態**: 生產就緒 🚀
