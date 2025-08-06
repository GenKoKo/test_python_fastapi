# 🐳 Docker 配置說明

## 🎯 **當前 Docker 結構**

```
fastapi_project/
├── 📄 Dockerfile                    # ⭐ 根目錄 - 業界標準
├── 📄 .dockerignore                 # ⭐ 根目錄 - 業界標準
├── 📄 docker-compose                # 快速啟動腳本
│
├── 📁 docker/                       # Docker 配置目錄
│   ├── docker-compose.yml          # 主要 Docker Compose 配置
│   ├── docker-compose.override.yml # 開發環境覆蓋配置
│   └── docker-compose.prod.yml     # 生產環境配置
│
└── 📁 src/                          # 應用源代碼
```

## 💡 **為什麼這樣設計？**

### **✅ 符合業界標準**

#### **1. Dockerfile 在根目錄**

-   **Docker 官方推薦** - 所有 Docker 工具默認在根目錄查找
-   **IDE 支持更好** - VS Code、IntelliJ 等自動識別
-   **CI/CD 兼容** - GitHub Actions、GitLab CI 等默認支持
-   **工具鏈友好** - docker build、docker-compose 等無需額外參數

#### **2. .dockerignore 在根目錄**

-   **Docker 構建需要** - 必須與 Dockerfile 在同一目錄
-   **性能優化** - 減少構建上下文大小
-   **安全考慮** - 防止敏感文件進入鏡像

#### **3. Just 命令整合**

-   **統一管理** - 使用 `just docker-*` 命令
-   **自動路徑處理** - 無需手動指定配置文件路徑
-   **環境切換** - 支持開發/生產環境切換

### **🎯 各種場景的支持**

#### **開發場景**

```bash
# 使用 just 命令（推薦）
just docker-dev

# 後台運行
just docker-dev-bg

# 手動指定路徑
docker-compose -f docker/docker-compose.yml up
```

#### **生產部署**

```bash
# 生產環境
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.prod.yml up

# 使用 just 命令
just docker-prod
```

#### **CI/CD 流程**

```yaml
# GitHub Actions 中
- name: Build Docker image
  run: docker build -t myapp . # 自動找到根目錄的 Dockerfile

- name: Run tests
  run: docker-compose -f docker/docker-compose.yml run test
```

## 🔄 **與其他方案的對比**

### **方案 A: 全部在根目錄**

```
project/
├── Dockerfile
├── docker-compose.yml
├── docker-compose.override.yml
├── docker-compose.prod.yml
└── .dockerignore
```

**優勢**: 簡單直接  
**劣勢**: 根目錄文件過多，不夠整潔

### **方案 B: 全部在子目錄**

```
project/
└── docker/
    ├── Dockerfile
    ├── docker-compose.yml
    └── .dockerignore
```

**優勢**: 結構清晰  
**劣勢**: 工具支持差，需要大量額外參數

### **方案 C: Just 命令方案（當前採用）** ⭐

```
project/
├── Dockerfile              # 業界標準位置
├── .dockerignore           # 必須在根目錄
├── justfile                # 統一命令管理
└── docker/                 # 配置文件
    ├── docker-compose.yml
    ├── docker-compose.override.yml
    └── docker-compose.prod.yml
```

**優勢**: 標準位置 + 統一管理  
**劣勢**: 需要學習 just 命令

## 🛠️ **實際使用指南**

### **日常開發**

```bash
# 最簡單的方式
docker-compose up

# 使用 just 命令（推薦）
just docker-dev
just docker-test
just docker-logs
```

### **生產部署**

```bash
# 生產環境構建
docker build -t myapp:prod .

# 生產環境運行
just docker-prod
# 或
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.prod.yml up
```

### **配置修改**

-   **Dockerfile**: 直接編輯根目錄的 `Dockerfile`
-   **開發環境**: 編輯 `docker/docker-compose.yml` 或 `docker/docker-compose.override.yml`
-   **生產環境**: 編輯 `docker/docker-compose.prod.yml`
-   **忽略規則**: 編輯根目錄的 `.dockerignore`

## 📚 **參考資料**

-   [Docker 官方最佳實踐](https://docs.docker.com/develop/dev-best-practices/)
-   [Docker Compose 文件結構](https://docs.docker.com/compose/compose-file/)
-   [GitHub Actions Docker 支持](https://docs.github.com/en/actions/publishing-packages/publishing-docker-images)

這種結構既符合業界標準，又保持了項目的整潔性！🎊
