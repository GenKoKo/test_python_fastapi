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

### 方法一：使用自動化腳本（推薦）

#### 1. 設置虛擬環境

```bash
./scripts/setup_venv.sh
```

#### 2. 運行應用

```bash
./scripts/run_app.sh
```

### 方法二：手動設置虛擬環境

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

### 3. 訪問 API

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

## 📁 項目結構

```
fastapi_project/
├── src/                     # 源代碼目錄
│   ├── __init__.py
│   ├── core/               # 核心配置和工具
│   │   ├── __init__.py
│   │   ├── config.py       # 配置管理
│   │   └── logger.py       # 日誌系統
│   └── app/                # 主應用
│       ├── __init__.py
│       ├── main.py         # FastAPI 應用入口
│       ├── models/         # 數據模型
│       │   ├── __init__.py
│       │   ├── item.py     # 商品模型
│       │   └── user.py     # 用戶模型
│       ├── routers/        # API 路由
│       │   ├── __init__.py
│       │   ├── items.py    # 商品路由
│       │   ├── users.py    # 用戶路由
│       │   └── stats.py    # 統計路由
│       ├── services/       # 業務邏輯層
│       │   ├── __init__.py
│       │   ├── item_service.py # 商品服務
│       │   └── user_service.py # 用戶服務
│       ├── database/       # 數據庫層
│       │   ├── __init__.py
│       │   └── memory_db.py # 內存數據庫
│       └── utils/          # 工具函數
│           ├── __init__.py
│           ├── helpers.py  # 輔助函數
│           └── middleware.py # 中間件
├── tests/                  # 測試文件
│   ├── __init__.py
│   ├── conftest.py         # pytest 配置
│   ├── test_items.py       # 商品測試
│   └── test_users.py       # 用戶測試
├── tools/                  # 開發工具和測試腳本
│   ├── test_config.py      # 配置測試
│   ├── test_import.py      # 導入測試
│   ├── test_new_structure.py # 結構測試
│   └── test_*.py          # 其他測試工具
├── scripts/                # 部署和運行腳本
│   ├── setup_venv.sh       # 環境設置
│   ├── run_app.sh          # 應用運行
│   └── test_in_venv.sh     # 測試腳本
├── docs/                   # 文檔目錄
│   ├── PROJECT_STRUCTURE.md
│   └── MIGRATION.md
├── run.py                  # 應用啟動器
├── requirements.txt        # 依賴管理
├── .env.example           # 環境變量範本
└── README.md              # 項目文檔
```

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

### 自動測試（推薦）

服務器啟動時會自動運行測試，無需額外操作。

### 手動測試

```bash
# 在虛擬環境中運行獨立測試
./scripts/test_in_venv.sh

# 或者手動激活虛擬環境後運行
source fastapi_env/bin/activate
python test_api.py
```

### 單元測試

```bash
# 運行所有測試
source fastapi_env/bin/activate
python -m pytest tests/ -v

# 運行特定測試文件
python -m pytest tests/test_items.py -v

# 運行測試並顯示覆蓋率
python -m pytest tests/ --cov=app --cov-report=html
```

### 結構測試

```bash
# 測試模塊化結構
python test_new_structure.py
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

-   **FastAPI**: 現代、快速的 Web 框架
-   **Pydantic**: 數據驗證和設置管理
-   **Pydantic Settings**: 環境變數配置管理
-   **Uvicorn**: ASGI 服務器
-   **Python Dotenv**: 環境變數加載
-   **Python 3.7+**: 編程語言
-   **虛擬環境**: 依賴隔離和管理
-   **結構化日誌**: 彩色終端日誌和文件日誌
