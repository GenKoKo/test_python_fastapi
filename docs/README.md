# 📚 FastAPI 項目文檔

## 📋 文檔索引

### 🏗️ 項目結構

-   **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - 項目目錄結構說明

### 🔄 遷移指南

-   **[MIGRATION.md](MIGRATION.md)** - 項目重構遷移指南

### 🐳 Docker 配置

-   **[DOCKER_STRUCTURE.md](DOCKER_STRUCTURE.md)** - Docker 配置說明
-   **[PODMAN_SETUP.md](PODMAN_SETUP.md)** - Podman 配置指南

### 🚀 部署指南

-   **[CODESPACES_DEPLOYMENT.md](CODESPACES_DEPLOYMENT.md)** - GitHub Codespaces 自動部署
-   **[CD_DEPLOYMENT_SUMMARY.md](CD_DEPLOYMENT_SUMMARY.md)** - CD 部署配置總結

### 📊 項目狀態

-   **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - 完整項目總結報告
-   **[PROJECT_STATUS.md](PROJECT_STATUS.md)** - 項目重構完成報告

## 🚀 快速開始

### 1. 環境設置

```bash
# 使用 Just 命令（推薦）
just setup

# 或手動設置
python -m venv fastapi_env
source fastapi_env/bin/activate  # Linux/macOS
pip install -r requirements/base.txt
```

### 2. 運行應用

```bash
# 開發模式
just dev

# 或直接運行
python run.py
```

### 3. Docker 開發

```bash
# 構建並運行
just docker-dev

# 查看日誌
just docker-logs
```

## 📖 更多信息

-   **API 文檔**: 運行應用後訪問 http://localhost:8000/docs
-   **項目主文檔**: 查看根目錄的 [README.md](../README.md)
-   **配置說明**: 查看 [pyproject.toml](../pyproject.toml)

## 🛠️ 開發工具

### Just 命令

```bash
just --list          # 查看所有可用命令
just help            # 詳細幫助信息
just status          # 檢查項目狀態
```

### 測試

```bash
just test-unit       # 單元測試
just test-coverage   # 測試覆蓋率
python scripts/test_api.py  # API 功能測試
```

### Docker

```bash
just docker-build    # 構建鏡像
just docker-dev      # 開發環境
just docker-test     # 容器測試
just container-status # 檢查容器引擎
```

---

💡 **提示**: 所有文檔都會隨著項目更新而保持同步。如有疑問，請查看對應的文檔文件。
