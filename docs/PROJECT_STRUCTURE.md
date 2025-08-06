# 📁 FastAPI 項目結構說明

## 🎯 當前項目結構

```
fastapi_project/
├── .github/                    # GitHub 配置
│   ├── workflows/
│   │   ├── ci.yml             # 主要 CI/CD 流程
│   │   └── feature-ci.yml     # 功能分支 CI
├── .devcontainer/             # GitHub Codespaces 配置
├── .kiro/                     # Kiro IDE 配置
│   ├── steering/              # 開發指導規則
│   └── specs/                 # 規格文件
├── src/                       # 源代碼目錄
│   ├── __init__.py
│   ├── core/                  # 核心配置和工具
│   │   ├── __init__.py
│   │   ├── config.py          # 配置管理
│   │   └── logger.py          # 日誌系統
│   └── app/                   # 主應用
│       ├── __init__.py
│       ├── main.py            # FastAPI 應用入口
│       ├── models/            # 數據模型
│       ├── routers/           # API 路由
│       ├── services/          # 業務邏輯
│       ├── database/          # 數據庫層
│       └── utils/             # 工具函數
├── tests/                     # 測試文件
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_items.py
│   └── test_users.py
├── scripts/                   # 開發腳本（原 tools/）
│   ├── test_config.py         # 配置測試
│   ├── test_api.py            # API 測試
│   ├── test_venv.py           # 環境測試
│   └── test_*.py              # 其他測試工具
├── docker/                    # Docker 配置
│   ├── docker-compose.yml     # 主要配置
│   ├── docker-compose.override.yml # 開發環境
│   └── docker-compose.prod.yml # 生產環境
├── docs/                      # 文檔目錄
├── requirements/              # 分層依賴管理
│   ├── base.txt              # 基礎依賴
│   ├── dev.txt               # 開發依賴
│   └── prod.txt              # 生產依賴
├── run.py                     # 應用啟動器
├── pyproject.toml            # 現代 Python 項目配置
├── justfile                  # Just 命令定義
├── Dockerfile                # Docker 鏡像定義
├── .dockerignore            # Docker 忽略文件
├── .env.example             # 環境變量範本
├── .gitignore               # Git 忽略文件
└── README.md                # 項目說明
```

## 🏗️ 目錄說明

### `src/` - 源代碼目錄

所有的應用源代碼都放在這個目錄下，便於管理和部署。

#### `src/core/` - 核心模組

-   **config.py**: 環境變量配置管理
-   **logger.py**: 統一的日誌記錄系統

#### `src/app/` - 主應用

-   **main.py**: FastAPI 應用入口和配置
-   **models/**: Pydantic 數據模型定義
-   **routers/**: API 路由處理
-   **services/**: 業務邏輯實現
-   **database/**: 數據庫操作抽象
-   **utils/**: 通用工具函數和中間件

### `tests/` - 測試目錄

包含所有的單元測試和集成測試。

### `scripts/` - 開發腳本

包含各種開發和測試工具腳本（原 tools/ 目錄）。

### `docker/` - Docker 配置

包含所有 Docker 相關的配置文件。

### `requirements/` - 分層依賴管理

-   **base.txt**: 核心依賴
-   **dev.txt**: 開發工具依賴
-   **prod.txt**: 生產環境依賴

### `docs/` - 文檔目錄

包含項目相關的所有文檔。

## 🎯 整理的優勢

### 1. 清晰的分層結構

-   **源代碼集中**: 所有源代碼在 `src/` 目錄下
-   **功能分離**: 核心配置、應用邏輯、測試、工具分別管理
-   **文檔集中**: 所有文檔在 `docs/` 目錄下

### 2. 現代化配置

-   **pyproject.toml**: 現代 Python 項目配置
-   **分層依賴**: 開發/生產環境分離
-   **工具配置統一**: Black、pytest、mypy 等配置集中

### 3. 企業級標準

-   **符合 Python 包結構標準**
-   **無符號連結**: 跨平台兼容
-   **便於 CI/CD 集成**
-   **支持容器化部署**

## 🚀 使用方式

### 啟動應用

```bash
python run.py
```

### 運行測試

```bash
# 單元測試
python -m pytest tests/ -v

# 工具測試
python tools/test_new_structure.py
```

### 使用 Just 命令

```bash
# 設置環境
just setup

# 開發模式運行
just dev

# 運行測試
just test-unit

# Docker 開發
just docker-dev
```

### 開發工具

```bash
# 配置測試
python scripts/test_config.py

# API 測試
python scripts/test_api.py
```

## 📦 部署考慮

這個結構便於：

-   **Docker 容器化**: `src/` 目錄可以直接複製到容器中
-   **包管理**: 可以將 `src/` 打包為 Python 包
-   **CI/CD**: 清晰的測試和構建流程
