# 項目結構說明

## 📁 整理後的項目結構

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
│       ├── routers/        # API 路由
│       ├── services/       # 業務邏輯
│       ├── database/       # 數據庫層
│       └── utils/          # 工具函數
├── tests/                  # 測試文件
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_items.py
│   └── test_users.py
├── tools/                  # 開發工具和測試腳本
│   ├── test_config.py      # 配置測試
│   ├── test_import.py      # 導入測試
│   ├── test_new_structure.py # 結構測試
│   └── test_*.py          # 其他測試工具
├── scripts/                # 部署和運行腳本
│   ├── setup_venv.sh
│   ├── run_app.sh
│   └── test_in_venv.sh
├── docs/                   # 文檔目錄
│   ├── PROJECT_STRUCTURE.md
│   └── MIGRATION.md
├── run.py                  # 應用啟動器
├── requirements.txt        # 依賴管理
├── .env.example           # 環境變量範本
├── .gitignore             # Git 忽略文件
└── README.md              # 項目說明
```

## 🏗️ 目錄說明

### `src/` - 源代碼目錄
所有的應用源代碼都放在這個目錄下，便於管理和部署。

#### `src/core/` - 核心模組
- **config.py**: 環境變量配置管理
- **logger.py**: 統一的日誌記錄系統

#### `src/app/` - 主應用
- **main.py**: FastAPI 應用入口和配置
- **models/**: Pydantic 數據模型定義
- **routers/**: API 路由處理
- **services/**: 業務邏輯實現
- **database/**: 數據庫操作抽象
- **utils/**: 通用工具函數和中間件

### `tests/` - 測試目錄
包含所有的單元測試和集成測試。

### `tools/` - 開發工具
包含各種開發和測試工具腳本。

### `scripts/` - 運行腳本
包含環境設置、應用運行等腳本。

### `docs/` - 文檔目錄
包含項目相關的所有文檔。

## 🎯 整理的優勢

### 1. 清晰的分層結構
- **源代碼集中**: 所有源代碼在 `src/` 目錄下
- **功能分離**: 核心配置、應用邏輯、測試、工具分別管理
- **文檔集中**: 所有文檔在 `docs/` 目錄下

### 2. 更好的可維護性
- **模組化設計**: 每個目錄有明確的職責
- **導入路徑清晰**: 使用 `src.` 前綴的導入路徑
- **依賴關係明確**: 核心模組被應用模組依賴

### 3. 企業級標準
- **符合 Python 包結構標準**
- **便於 CI/CD 集成**
- **支持容器化部署**

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

### 開發工具
```bash
# 配置測試
python tools/test_config.py

# 導入測試
python tools/test_import.py
```

## 📦 部署考慮

這個結構便於：
- **Docker 容器化**: `src/` 目錄可以直接複製到容器中
- **包管理**: 可以將 `src/` 打包為 Python 包
- **CI/CD**: 清晰的測試和構建流程