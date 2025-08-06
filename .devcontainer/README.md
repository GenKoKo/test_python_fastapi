# GitHub Codespaces 開發環境

## 🌟 快速開始

### 1. 啟動 Codespace

1. 在 GitHub 倉庫頁面點擊 **Code** 按鈕
2. 選擇 **Codespaces** 標籤
3. 點擊 **Create codespace on main**

### 2. 等待環境設置

-   Codespace 會自動安裝基礎工具
-   執行 `just codespaces-setup` 完成完整設置
-   配置開發環境和依賴

### 3. 啟動 FastAPI 應用

```bash
# 方法 1: 前台運行（推薦用於開發）
just codespaces-start

# 方法 2: 後台運行
just codespaces-start-bg

# 方法 3: 使用 Docker
just docker-dev
```

### 4. 訪問 API

-   點擊 VS Code 底部的端口轉發通知
-   或者在 **PORTS** 標籤中點擊端口 8000 的連結
-   添加 `/docs` 查看 Swagger UI 文檔

## 🔧 可用命令

### 基本命令

```bash
just --list                 # 查看所有命令
just codespaces-info        # 顯示環境信息
just test                   # 運行測試
just help                   # 查看詳細幫助
```

### Codespaces 專用命令

```bash
just codespaces-setup       # 設置 Codespaces 環境
just codespaces-start       # 啟動應用（前台）
just codespaces-start-bg    # 啟動應用（後台）
just codespaces-logs        # 查看應用日誌
just codespaces-stop        # 停止後台應用
just codespaces-doctor      # 診斷環境問題
just codespaces-reset       # 重置環境
just codespaces-test        # 快速測試環境
```

### Docker 命令

```bash
just docker-dev             # 使用 Docker 啟動
just docker-test            # 在 Docker 中測試
just docker-logs            # 查看 Docker 日誌
```

## 📖 API 測試

### 1. 使用 Swagger UI

-   訪問 `/docs` 端點
-   直接在瀏覽器中測試所有 API

### 2. 使用 REST Client

-   打開 `.devcontainer/api-tests.http`
-   使用 VS Code 的 REST Client 擴展測試

### 3. 使用 curl

```bash
# 健康檢查
curl http://localhost:8000/stats/health

# 獲取所有商品
curl http://localhost:8000/items/

# 創建商品
curl -X POST http://localhost:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name":"測試商品","price":99.99,"is_available":true}'
```

## 🔍 開發工具

### VS Code 擴展

已預裝的擴展：

-   Python 開發套件
-   Docker 支援
-   REST Client
-   GitHub Copilot
-   代碼格式化工具

### 調試功能

-   設置斷點直接調試
-   使用端口 5678 進行遠程調試
-   集成的測試運行器

## 🌐 端口配置

| 端口 | 用途          | 訪問方式       |
| ---- | ------------- | -------------- |
| 8000 | FastAPI 應用  | 公開，自動轉發 |
| 5678 | Python 調試器 | 私有           |

## 💡 使用技巧

### 1. 自動端口轉發

-   Codespaces 會自動檢測並轉發端口 8000
-   點擊通知或在 PORTS 標籤中查看

### 2. 分享你的應用

-   在 PORTS 標籤中右鍵點擊端口
-   選擇 "Port Visibility" > "Public"
-   分享生成的 URL

### 3. 持久化數據

-   代碼變更會自動保存
-   安裝的套件在 Codespace 重啟後保留
-   日誌文件存儲在 `logs/` 目錄

### 4. 性能優化

-   使用 `just codespaces-start-bg` 後台運行
-   定期檢查 `just codespaces-logs` 查看狀態

## 🚨 故障排除

### 應用無法啟動

```bash
# 檢查日誌
just codespaces-logs

# 重新啟動
just codespaces-stop
just codespaces-start
```

### 端口無法訪問

1. 檢查 PORTS 標籤中的端口狀態
2. 確保應用正在運行
3. 嘗試刷新端口轉發

### 依賴問題

```bash
# 重新安裝依賴
pip install -r requirements/base.txt

# 或重建環境
just clean
just setup
```

## 📚 更多資源

-   [GitHub Codespaces 文檔](https://docs.github.com/en/codespaces)
-   [FastAPI 文檔](https://fastapi.tiangolo.com/)
-   [項目 README](../README.md)
