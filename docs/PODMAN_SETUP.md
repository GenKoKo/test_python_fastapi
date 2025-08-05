# 🐳 Podman 配置指南

## 🎯 **Podman vs Docker**

你的系統使用 **Podman** 而不是 Docker。Podman 是一個無守護程序的容器引擎，與 Docker 命令兼容。

## ✅ **當前配置狀態**

### **已完成的配置**：
- ✅ Podman 5.5.2 已安裝並運行
- ✅ Podman machine 正在運行
- ✅ Docker socket 已連結到 Podman
- ✅ Just 命令已配置支援 Podman
- ✅ Docker Compose 文件已調整路徑

## 🚀 **使用方式**

### **推薦使用 Just 命令**：
```bash
# 構建鏡像
just docker-build

# 啟動開發環境
just docker-dev

# 後台啟動
just docker-dev-bg

# 查看日誌
just docker-logs

# 停止服務
just docker-stop
```

### **直接使用 Podman 命令**：
```bash
# 使用 podman-compose
podman-compose -f docker/docker-compose.yml up

# 使用 docker 命令（通過兼容層）
DOCKER_HOST=unix:///var/run/docker.sock docker-compose -f docker/docker-compose.yml up
```

## 🔧 **環境變數設置**

### **自動設置（推薦）**：
```bash
# 設置 Podman 為默認
just use-podman

# 檢查狀態
just container-status
```

### **手動設置**：
```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
export CONTAINER_ENGINE=podman
export DOCKER_HOST=unix:///var/run/docker.sock
```

## 🎯 **Just 命令支援**

### **容器引擎管理**：
- `just use-podman` - 設置使用 Podman
- `just use-docker` - 設置使用 Docker（如果安裝了）
- `just container-status` - 檢查容器引擎狀態

### **自動檢測**：
Just 命令會自動檢測你設置的容器引擎：
- 如果設置 `CONTAINER_ENGINE=podman`，使用 `podman-compose`
- 如果設置 `CONTAINER_ENGINE=docker`，使用 `docker-compose`
- 默認使用 `docker`（通過 Podman 兼容層）

## 🐛 **故障排除**

### **問題 1: "Cannot connect to Docker daemon"**
```bash
# 解決方案：設置 Docker socket
export DOCKER_HOST=unix:///var/run/docker.sock

# 或者直接使用 podman-compose
podman-compose -f docker/docker-compose.yml up
```

### **問題 2: "Dockerfile not found"**
```bash
# 確保 Docker Compose 文件中的路徑正確
# context: .. (指向上級目錄)
# dockerfile: Dockerfile (在根目錄)
```

### **問題 3: Podman machine 未運行**
```bash
# 啟動 Podman machine
podman machine start

# 檢查狀態
podman machine list
```

## 📊 **性能對比**

| 特性 | Docker | Podman |
|------|--------|--------|
| **守護程序** | 需要 | 無需 |
| **Root 權限** | 需要 | 可選 |
| **安全性** | 好 | 更好 |
| **資源使用** | 較高 | 較低 |
| **兼容性** | 標準 | Docker 兼容 |

## 🎉 **成功測試**

你的 Podman 配置已經成功！剛才的構建輸出顯示：
- ✅ 成功拉取 Python 3.11 基礎鏡像
- ✅ 成功安裝所有依賴
- ✅ 成功構建 FastAPI 開發鏡像
- ✅ 鏡像標籤：`localhost/docker_fastapi-app:latest`

## 💡 **使用建議**

1. **日常開發**：使用 `just docker-dev` 啟動開發環境
2. **測試**：使用 `just docker-test` 在容器中運行測試
3. **調試**：使用 `just docker-shell` 進入容器
4. **監控**：使用 `just docker-logs` 查看日誌

你的 Podman 環境已經完美配置，可以正常使用所有 Docker 功能！🎊