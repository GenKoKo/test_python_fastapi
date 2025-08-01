# FastAPI 初級快速入門實作

這是一個使用 FastAPI 框架構建的基本 API 項目，適合初學者學習和實踐。

## 功能特色

-   ✅ 基本的 CRUD 操作（創建、讀取、更新、刪除）
-   ✅ 商品管理系統
-   ✅ 用戶管理系統
-   ✅ 查詢參數和過濾功能
-   ✅ 數據驗證（使用 Pydantic）
-   ✅ 自動生成的 API 文檔
-   ✅ 錯誤處理和統計功能
-   ✅ **環境變量配置管理**
-   ✅ **結構化日誌記錄**
-   ✅ **請求追蹤中間件**
-   ✅ **彩色終端日誌**

## 安裝和運行

### 方法一：使用自動化腳本（推薦）

#### 1. 設置虛擬環境

```bash
./setup_venv.sh
```

#### 2. 運行應用

```bash
./run_app.sh
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
# 方法 1: 使用 Python 直接運行
python main.py

# 方法 2: 使用 uvicorn 命令
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# 方法 3: 使用 FastAPI CLI（如果已安裝）
fastapi dev main.py
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

## API 端點說明

### 基本端點

-   `GET /` - 歡迎頁面
-   `GET /health` - 健康檢查
-   `GET /stats` - 獲取統計信息

### 商品管理

-   `GET /items` - 獲取所有商品
-   `GET /items/{item_id}` - 獲取特定商品
-   `POST /items` - 創建新商品
-   `PUT /items/{item_id}` - 更新商品
-   `DELETE /items/{item_id}` - 刪除商品
-   `GET /search/items` - 搜索商品（支持查詢參數）

### 用戶管理

-   `GET /users` - 獲取所有用戶
-   `GET /users/{user_id}` - 獲取特定用戶
-   `POST /users` - 創建新用戶

## 測試選項

### 自動測試（推薦）

服務器啟動時會自動運行測試，無需額外操作。

### 手動測試

```bash
# 在虛擬環境中運行獨立測試
./test_in_venv.sh

# 或者手動激活虛擬環境後運行
source fastapi_env/bin/activate
python test_api.py
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
curl "http://127.0.0.1:8000/search/items?q=筆記本&min_price=20000&max_price=30000"
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
