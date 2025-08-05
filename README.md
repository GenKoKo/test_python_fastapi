# FastAPI 初級快速入門實作（模塊化版本）

這是一個使用 FastAPI 框架構建的模塊化 API 項目，展示了現代 Python Web 開發的最佳實踐和企業級架構設計。

## 功能特色

### 🏗️ 架構特色
-   ✅ **模塊化架構設計** - 清晰的分層結構
-   ✅ **服務層模式** - 業務邏輯與路由分離
-   ✅ **依賴注入** - 鬆耦合的組件設計
-   ✅ **單元測試覆蓋** - 完整的測試套件

### 🚀 核心功能
-   ✅ 基本的 CRUD 操作（創建、讀取、更新、刪除）
-   ✅ 商品管理系統
-   ✅ 用戶管理系統
-   ✅ 查詢參數和過濾功能
-   ✅ 數據驗證（使用 Pydantic）
-   ✅ 自動生成的 API 文檔

### 🔧 技術特色
-   ✅ **環境變量配置管理**
-   ✅ **結構化日誌記錄**
-   ✅ **請求追蹤中間件**
-   ✅ **彩色終端日誌**
-   ✅ **線程安全的內存數據庫**

## 安裝和運行

### 方法一：使用 Just 命令（推薦）⭐

> **新功能**: 現在支援使用 `just` 命令來管理項目！更簡潔、跨平台且功能豐富。

#### 1. 安裝 Just 工具

```bash
# macOS (使用 Homebrew)
brew install just

# Linux (使用 cargo)
cargo install just

# 或者從 GitHub 下載二進制文件
# https://github.com/casey/just/releases
```

#### 2. 查看所有可用命令

```bash
# 顯示所有命令
just --list

# 顯示詳細幫助
just help
```

#### 3. 一鍵設置並運行

```bash
# 設置環境並運行應用
just start

# 或者分步執行
just setup  # 設置虛擬環境
just run    # 運行應用
```

#### 4. 開發模式

```bash
# 開發模式運行（支援熱重載）
just dev

# 或者一鍵開發環境設置
just dev-start
```

### 方法二：使用傳統腳本

#### 1. 設置虛擬環境

```bash
./scripts/setup_venv.sh
```

#### 2. 運行應用

```bash
./scripts/run_app.sh
```

### 方法三：手動設置虛擬環境

#### 1. 創建虛擬環境

```bash
# macOS/Linux
python3 -m venv fastapi_env

# Windows
python -m venv fastapi_env
```

#### 2. 激活虛擬環境

```bash
# macOS/Linux
source fastapi_env/bin/activate

# Windows
fastapi_env\Scripts\activate
```

#### 3. 安裝依賴

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. 運行應用

```bash
# 方法 1: 使用新的啟動腳本（推薦）
python run.py

# 方法 2: 使用 uvicorn 命令
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# 方法 3: 使用 FastAPI CLI（如果已安裝）
fastapi dev app/main.py
```

#### 5. 退出虛擬環境

```bash
deactivate
```

## 🐳 Docker 開發環境（推薦）

> **新功能**: 現在支援完整的 Docker 開發環境！提供一致的跨平台開發體驗。

### 1. 前置需求

確保已安裝：
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Docker 快速開始

```bash
# 一鍵啟動 Docker 開發環境
just docker-start

# 或者分步執行
just docker-build    # 構建鏡像
just docker-dev-bg    # 後台啟動服務
```

### 3. Docker 開發工作流程

```bash
# 查看服務狀態
just docker-status

# 查看服務日誌
just docker-logs

# 進入容器進行調試
just docker-shell

# 在 Docker 中運行測試
just docker-test

# 停止服務
just docker-stop
```

### 4. Docker 環境優勢

✅ **環境一致性**: 所有開發者使用相同的環境  
✅ **快速設置**: 無需手動安裝 Python 依賴  
✅ **隔離性**: 不影響本地系統環境  
✅ **生產就緒**: 開發環境接近生產環境  
✅ **CI/CD 整合**: 與 GitHub Actions 無縫整合  

## 🌟 GitHub Codespaces 雲端開發（推薦）

> **最新功能**: 現在支援 GitHub Codespaces！無需本地安裝，一鍵啟動完整的雲端開發環境。

### 🚀 一鍵啟動

1. **在 GitHub 上啟動**：
   - 點擊倉庫頁面的 **Code** 按鈕
   - 選擇 **Codespaces** 標籤
   - 點擊 **Create codespace on main**

2. **自動設置**：
   - 環境會自動安裝所有依賴
   - 配置開發工具和擴展
   - 準備就緒後顯示歡迎信息

3. **啟動應用**：
   ```bash
   # 在 Codespaces 終端中執行
   just codespaces-start
   ```

4. **訪問 API**：
   - 點擊端口 8000 的轉發連結
   - 添加 `/docs` 查看 Swagger UI

### 🎯 Codespaces 優勢

✅ **零配置**: 無需本地安裝任何工具  
✅ **雲端運行**: 強大的雲端計算資源  
✅ **即時分享**: 可以分享 API 連結給其他人  
✅ **完整工具**: 預裝所有開發工具和擴展  
✅ **自動同步**: 代碼變更自動同步到 GitHub  

### 📋 Codespaces 專用命令

```bash
just codespaces-start       # 啟動應用（前台）
just codespaces-start-bg    # 啟動應用（後台）
just codespaces-logs        # 查看應用日誌
just codespaces-stop        # 停止後台應用
just codespaces-info        # 顯示環境信息
```

### 6. 訪問 API

-   **API 根路徑**: http://127.0.0.1:8000/
-   **交互式文檔 (Swagger UI)**: http://127.0.0.1:8000/docs
-   **替代文檔 (ReDoc)**: http://127.0.0.1:8000/redoc

### 4. 配置管理

🎛️ **新功能**: 支援環境變數配置管理！

#### 配置文件設置
```bash
# 複製環境變數範本
cp .env.example .env

# 編輯配置（可選）
nano .env
```

#### 主要配置項
- **服務器配置**: HOST, PORT, RELOAD
- **日誌配置**: LOG_LEVEL, LOG_FILE
- **功能開關**: ENABLE_AUTO_TEST, POPULATE_SAMPLE_DATA
- **調試模式**: DEBUG

#### 測試配置
```bash
# 測試配置和日誌系統
python test_config.py
```

### 5. 自動測試功能

🎉 **新功能**: 服務器啟動時會自動運行 API 測試！

-   ✅ 服務器啟動後自動填充示例數據
-   ✅ 自動運行 API 功能測試
-   ✅ 測試結果會在終端顯示
-   ✅ 不影響正常的 API 服務

## 🚀 Just 命令快速參考

### 基本命令
```bash
just setup          # 創建虛擬環境並安裝依賴
just run             # 運行 FastAPI 應用
just dev             # 開發模式運行（熱重載）
just start           # 一鍵設置並運行
just status          # 顯示項目狀態
```

### 測試命令
```bash
just test            # 運行 API 功能測試
just test-unit       # 運行單元測試
just test-coverage   # 運行測試並生成覆蓋率報告
just test-structure  # 測試項目結構
just test-config     # 測試配置系統
```

### 依賴管理
```bash
just install <package>  # 安裝新的依賴包
just update-deps        # 更新所有依賴
just freeze             # 生成 requirements.txt
just list-packages      # 顯示已安裝套件
```

### 清理和維護
```bash
just clean           # 清理虛擬環境
just clean-cache     # 清理 Python 緩存
just reset           # 完全重置環境
```

### 開發工具
```bash
just format          # 代碼格式化（需要 black）
just lint            # 代碼風格檢查（需要 flake8）
```

### Docker 命令
```bash
just docker-build    # 構建 Docker 開發鏡像
just docker-dev      # 啟動 Docker 開發環境
just docker-dev-bg   # 後台啟動 Docker 開發環境
just docker-test     # 在 Docker 中運行測試
just docker-shell    # 進入 Docker 容器
just docker-logs     # 查看 Docker 服務日誌
just docker-stop     # 停止 Docker 服務
just docker-clean    # 清理 Docker 資源
just docker-start    # Docker 一鍵開發環境
```

## 📁 項目結構

```
fastapi_project/
├── 📁 src/                          # 源代碼目錄
│   ├── core/                        # 核心配置和工具
│   │   ├── config.py               # 配置管理
│   │   └── logger.py               # 日誌系統
│   └── app/                        # 主應用
│       ├── main.py                 # FastAPI 應用入口
│       ├── models/                 # 數據模型
│       ├── routers/                # API 路由
│       ├── services/               # 業務邏輯層
│       ├── database/               # 數據庫層
│       └── utils/                  # 工具函數
│
├── 📁 tests/                        # 測試文件
├── 📁 tools/                        # 開發工具和測試腳本
├── 📁 docs/                         # 文檔目錄
│
├── 📁 docker/                       # Docker 配置目錄 ⭐ 最佳實踐
│   ├── docker-compose.yml          # 主要 Docker Compose 配置
│   ├── docker-compose.override.yml # 開發環境覆蓋配置
│   └── docker-compose.prod.yml     # 生產環境配置
│
├── 📁 config/                       # 其他配置文件
│   ├── env/                        # 環境變數配置
│   │   ├── .env.example            # 環境變數範本
│   │   └── .env.docker             # Docker 環境變數
│   ├── .devcontainer/              # GitHub Codespaces 配置
│   └── github/                     # GitHub Actions 配置
│       └── .github/workflows/ci.yml # CI/CD 流程
│
├── 📁 deploy/                       # 部署相關文件 ⭐ 整理後
│   └── scripts/                    # 部署腳本
│       ├── setup_venv.sh           # 環境設置
│       ├── run_app.sh              # 應用運行
│       └── test_in_venv.sh         # 測試腳本
│
├── 📄 Dockerfile                    # Docker 鏡像定義 ⭐ 根目錄標準
├── 📄 .dockerignore                # Docker 忽略文件
├── 📄 docker-compose.yml           # 主要 Docker Compose（符號連結）
├── 📄 run.py                       # 應用啟動器
├── 📄 requirements.txt             # 依賴管理
├── 📄 justfile                     # Just 命令定義
└── 📄 README.md                    # 項目文檔
```

> **📋 結構說明**: 為了更好的組織和維護，我們將配置文件整理到 `config/` 目錄，部署腳本移到 `deploy/` 目錄。重要文件通過符號連結保持兼容性。

### 🏗️ 架構說明

- **源代碼集中**: 所有源代碼在 `src/` 目錄下，便於管理和部署
- **核心模組**: `src/core/` 包含配置管理和日誌系統
- **分層架構**: 清晰的分層設計，便於維護和擴展
- **模型層 (Models)**: 使用 Pydantic 定義數據結構和驗證規則
- **服務層 (Services)**: 包含業務邏輯，與路由層分離
- **路由層 (Routers)**: 處理 HTTP 請求和響應
- **數據庫層 (Database)**: 數據存儲和操作的抽象
- **工具層 (Utils)**: 通用工具函數和中間件
- **開發工具**: `tools/` 目錄包含各種開發和測試工具
- **文檔集中**: `docs/` 目錄包含所有項目文檔

## API 端點說明

### 基本端點

-   `GET /` - 歡迎頁面
-   `GET /stats/health` - 健康檢查
-   `GET /stats/` - 獲取統計信息

### 商品管理

-   `GET /items/` - 獲取所有商品
-   `GET /items/{item_id}` - 獲取特定商品
-   `POST /items/` - 創建新商品
-   `PUT /items/{item_id}` - 更新商品
-   `DELETE /items/{item_id}` - 刪除商品
-   `GET /items/search/` - 搜索商品（支持查詢參數）

### 用戶管理

-   `GET /users/` - 獲取所有用戶
-   `GET /users/{user_id}` - 獲取特定用戶
-   `POST /users/` - 創建新用戶
-   `PUT /users/{user_id}` - 更新用戶
-   `DELETE /users/{user_id}` - 刪除用戶

## 測試選項

### 使用 Just 命令（推薦）⭐

```bash
# 運行 API 功能測試
just test

# 運行單元測試
just test-unit

# 運行測試並生成覆蓋率報告
just test-coverage

# 測試項目結構
just test-structure

# 測試配置系統
just test-config
```

### 自動測試

服務器啟動時會自動運行測試，無需額外操作。

### 傳統方式測試

```bash
# 在虛擬環境中運行獨立測試
./scripts/test_in_venv.sh

# 或者手動激活虛擬環境後運行
source fastapi_env/bin/activate
python tools/test_api.py
```

### 手動單元測試

```bash
# 運行所有測試
source fastapi_env/bin/activate
python -m pytest tests/ -v

# 運行特定測試文件
python -m pytest tests/test_items.py -v

# 運行測試並顯示覆蓋率
python -m pytest tests/ --cov=src --cov-report=html
```

## 使用示例

### 創建商品

```bash
curl -X POST "http://127.0.0.1:8000/items" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "筆記本電腦",
       "description": "高性能筆記本電腦",
       "price": 25000.0,
       "is_available": true
     }'
```

### 搜索商品

```bash
curl "http://127.0.0.1:8000/items/search/?q=筆記本&min_price=20000&max_price=30000"
```

### 創建用戶

```bash
curl -X POST "http://127.0.0.1:8000/users" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "john_doe",
       "email": "john@example.com",
       "full_name": "John Doe"
     }'
```

## 數據模型

### Item（商品）

-   `id`: 整數，自動生成
-   `name`: 字符串，必填
-   `description`: 字符串，可選
-   `price`: 浮點數，必填
-   `is_available`: 布爾值，默認為 true

### User（用戶）

-   `id`: 整數，自動生成
-   `username`: 字符串，必填且唯一
-   `email`: 字符串，必填
-   `full_name`: 字符串，可選

## 學習要點

1. **FastAPI 基礎**: 了解如何創建 FastAPI 應用和定義路由
2. **Pydantic 模型**: 學習數據驗證和序列化
3. **HTTP 方法**: 實踐 GET、POST、PUT、DELETE 操作
4. **查詢參數**: 學習如何處理 URL 查詢參數
5. **錯誤處理**: 了解如何拋出和處理 HTTP 異常
6. **自動文檔**: 體驗 FastAPI 的自動 API 文檔生成

## 下一步學習

-   添加數據庫集成（SQLAlchemy）
-   實現用戶認證和授權
-   添加中間件
-   實現文件上傳
-   添加測試用例
-   部署到生產環境

## 虛擬環境管理

### 為什麼使用虛擬環境？

-   🔒 **隔離依賴**: 避免不同項目間的依賴衝突
-   🧹 **保持系統乾淨**: 不污染系統 Python 環境
-   📦 **版本控制**: 精確控制每個項目的依賴版本
-   🚀 **部署一致性**: 確保開發和生產環境一致

### 虛擬環境常用命令

```bash
# 檢查當前是否在虛擬環境中
which python

# 查看已安裝的包
pip list

# 生成依賴文件
pip freeze > requirements.txt

# 檢查虛擬環境狀態
pip show fastapi
```

### 故障排除

-   **權限問題**: 確保腳本有執行權限 `chmod +x *.sh`
-   **Python 版本**: 確保使用 Python 3.7+
-   **依賴衝突**: 刪除虛擬環境重新創建 `rm -rf fastapi_env`

## 技術棧

### 核心技術
-   **FastAPI**: 現代、快速的 Web 框架
-   **Pydantic**: 數據驗證和設置管理
-   **Pydantic Settings**: 環境變數配置管理
-   **Uvicorn**: ASGI 服務器
-   **Python Dotenv**: 環境變數加載
-   **Python 3.7+**: 編程語言

### 開發工具
-   **Just**: 現代化的命令執行器，替代傳統 shell 腳本
-   **虛擬環境**: 依賴隔離和管理
-   **結構化日誌**: 彩色終端日誌和文件日誌
-   **pytest**: 單元測試框架

### 關於 Just

[Just](https://github.com/casey/just) 是一個現代化的命令執行器，類似於 `make` 但更簡潔易用：

✅ **跨平台**: 支援 Windows、macOS、Linux  
✅ **語法簡潔**: 比 Makefile 更易讀易寫  
✅ **功能豐富**: 支援變數、條件、循環等  
✅ **無依賴**: 單一二進制文件，無需額外依賴  
✅ **快速**: 比傳統 shell 腳本啟動更快
