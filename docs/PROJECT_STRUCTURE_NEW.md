# 📁 項目結構說明

## 🎯 整理後的項目結構

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
│   ├── conftest.py                 # pytest 配置
│   ├── test_items.py               # 商品測試
│   └── test_users.py               # 用戶測試
│
├── 📁 tools/                        # 開發工具和測試腳本
│   ├── test_config.py              # 配置測試
│   ├── test_api.py                 # API 測試
│   └── test_*.py                   # 其他測試工具
│
├── 📁 docs/                         # 文檔目錄
│   ├── PROJECT_STRUCTURE.md        # 項目結構說明
│   └── MIGRATION.md                # 遷移指南
│
├── 📁 config/                       # 配置文件目錄 ⭐ 新增
│   ├── docker/                     # Docker 相關配置
│   │   ├── Dockerfile              # Docker 鏡像定義
│   │   ├── docker-compose.yml      # 主要 Docker Compose 配置
│   │   ├── docker-compose.override.yml # 開發環境覆蓋
│   │   ├── docker-compose.prod.yml # 生產環境配置
│   │   └── .dockerignore           # Docker 忽略文件
│   ├── env/                        # 環境變數配置
│   │   ├── .env.example            # 環境變數範本
│   │   └── .env.docker             # Docker 環境變數
│   ├── .devcontainer/              # GitHub Codespaces 配置
│   │   ├── devcontainer.json       # 主要配置
│   │   ├── setup.sh                # 設置腳本
│   │   ├── start.sh                # 啟動腳本
│   │   ├── api-tests.http          # REST Client 測試
│   │   └── README.md               # Codespaces 使用說明
│   └── github/                     # GitHub 相關配置
│       ├── workflows/              # GitHub Actions
│       │   └── ci.yml              # CI/CD 流程
│       └── codespaces/             # Codespaces 預設配置
│           └── devcontainer.json   # 預設配置
│
├── 📁 deploy/                       # 部署相關文件 ⭐ 新增
│   └── scripts/                    # 部署腳本
│       ├── setup_venv.sh           # 環境設置
│       ├── run_app.sh              # 應用運行
│       └── test_in_venv.sh         # 測試腳本
│
├── 📄 run.py                        # 應用啟動器
├── 📄 requirements.txt              # 依賴管理
├── 📄 justfile                     # Just 命令定義
├── 📄 README.md                    # 項目文檔
├── 📄 .gitignore                   # Git 忽略文件
│
└── 🔗 符號連結 (保持兼容性)
    ├── docker-compose.yml → config/docker/docker-compose.yml
    ├── Dockerfile → config/docker/Dockerfile
    ├── .dockerignore → config/docker/.dockerignore
    ├── .devcontainer → config/.devcontainer
    ├── .github → config/github/.github
    └── .env.example → config/env/.env.example
```

## 🎯 整理的目標

### ✅ **已完成的整理**

1. **配置文件集中化**
   - 所有 Docker 相關文件移到 `config/docker/`
   - 環境變數文件移到 `config/env/`
   - GitHub 配置移到 `config/github/`
   - Codespaces 配置移到 `config/.devcontainer/`

2. **部署文件整理**
   - 部署腳本移到 `deploy/scripts/`
   - 保持邏輯分組

3. **符號連結保持兼容性**
   - 重要文件保持原位置的符號連結
   - 確保現有工具和 CI/CD 正常工作

4. **更新相關引用**
   - 更新 `justfile` 中的路徑引用
   - 更新 `devcontainer.json` 配置

## 🚀 **優勢**

### **1. 更清晰的結構** 📋
- 配置文件按類型分組
- 減少根目錄的文件數量
- 更容易找到相關文件

### **2. 更好的維護性** 🔧
- 相關文件集中管理
- 減少配置文件散亂
- 更容易進行批量修改

### **3. 保持兼容性** ✅
- 符號連結確保現有工具正常工作
- GitHub Actions 和 Docker 命令無需修改
- 團隊成員無需改變工作習慣

### **4. 擴展性** 🚀
- 新的配置類型可以輕鬆添加
- 環境特定配置有明確的位置
- 更容易添加新的部署環境

## 📝 **使用說明**

### **開發者使用**
- 所有 `just` 命令保持不變
- Docker 命令自動使用新的路徑
- Codespaces 配置自動生效

### **配置修改**
- Docker 配置: 編輯 `config/docker/` 下的文件
- 環境變數: 編輯 `config/env/` 下的文件
- CI/CD 配置: 編輯 `config/github/workflows/` 下的文件

### **新環境添加**
- 新的 Docker 環境: 在 `config/docker/` 添加新的 compose 文件
- 新的環境變數: 在 `config/env/` 添加新的 .env 文件
- 新的部署腳本: 在 `deploy/scripts/` 添加新的腳本

## 🔍 **文件對應關係**

| 原位置 | 新位置 | 符號連結 |
|--------|--------|----------|
| `docker-compose.yml` | `config/docker/docker-compose.yml` | ✅ |
| `Dockerfile` | `config/docker/Dockerfile` | ✅ |
| `.dockerignore` | `config/docker/.dockerignore` | ✅ |
| `.devcontainer/` | `config/.devcontainer/` | ✅ |
| `.github/` | `config/github/.github/` | ✅ |
| `.env.example` | `config/env/.env.example` | ✅ |
| `scripts/` | `deploy/scripts/` | ❌ |

## 💡 **最佳實踐**

1. **配置修改**: 直接編輯 `config/` 目錄下的文件
2. **新增配置**: 在對應的 `config/` 子目錄添加
3. **部署腳本**: 在 `deploy/scripts/` 目錄管理
4. **文檔更新**: 及時更新 `docs/` 目錄下的文檔

這樣的結構讓項目更加專業和易於維護！🎊