# 🚀 FastAPI Codespaces 環境

這個目錄包含了 GitHub Codespaces 的配置文件，用於創建一個完整的 FastAPI 開發環境。

## 📁 文件說明

-   `devcontainer.json` - 主要的 Codespaces 配置文件
-   `devcontainer.codespaces.json` - Codespaces 專用配置（由 CD 工作流程自動生成）
-   `setup.sh` - 環境設置腳本（備用，自定義鏡像中已預安裝）
-   `install-just.sh` - Just 命令工具安裝腳本（備用）
-   `test-codespaces.sh` - 環境測試腳本

## 🔧 配置特點

### 自定義 Docker 鏡像

-   使用 `ghcr.io/genkoko/test_python_fastapi:codespaces-latest`
-   預安裝了 Python、uv、just 等工具
-   包含完整的開發依賴

### 開發工具

-   **Python 3.11** - 主要開發語言
-   **uv** - 快速的 Python 包管理器
-   **just** - 命令運行器（類似 make）
-   **FastAPI** - Web 框架
-   **VS Code 擴展** - Python、Docker、GitHub Copilot 等

### 端口配置

-   **8000** - FastAPI 應用服務器
-   **5678** - Python 調試器

## 🚀 快速開始

### 1. 創建 Codespace

1. 前往 [GitHub Codespaces](https://github.com/GenKoKo/test_python_fastapi/codespaces)
2. 點擊 "Create codespace on master"
3. 等待環境自動配置完成

### 2. 驗證環境

```bash
# 運行環境測試
bash .devcontainer/test-codespaces.sh

# 檢查 just 命令
just --version
just --list
```

### 3. 開始開發

```bash
# 啟動開發服務器
just dev

# 運行測試
just test-unit

# 查看 API 文檔
# 訪問: http://localhost:8000/docs
```

## 🔍 故障排除

### Just 命令不可用

如果 `just` 命令不可用，可能的原因：

1. **使用了錯誤的鏡像**

    ```bash
    # 檢查當前鏡像
    echo $CODESPACES_IMAGE
    # 應該顯示: ghcr.io/genkoko/test_python_fastapi:codespaces-latest
    ```

2. **PATH 問題**

    ```bash
    # 檢查 just 是否存在
    ls -la /usr/local/bin/just

    # 手動添加到 PATH
    export PATH="/usr/local/bin:$PATH"
    ```

3. **使用備用安裝**
    ```bash
    # 運行安裝腳本
    bash .devcontainer/install-just.sh
    source ~/.bashrc
    ```

### Python 環境問題

```bash
# 檢查 Python 解釋器
which python
python --version

# 檢查虛擬環境
ls -la .venv/

# 重新同步依賴
uv sync --dev
```

### 端口訪問問題

1. 確保端口 8000 已轉發
2. 檢查 VS Code 的端口面板
3. 使用 `just dev` 啟動服務器

## 📋 可用命令

運行 `just --list` 查看所有可用命令：

```bash
just dev              # 啟動開發服務器
just test-unit         # 運行單元測試
just test-integration  # 運行整合測試
just lint              # 代碼檢查
just format            # 代碼格式化
just clean             # 清理緩存文件
```

## 🔄 更新環境

當 Docker 鏡像更新時：

1. **自動更新**：推送代碼到 master 分支會自動觸發鏡像構建
2. **手動更新**：重新創建 Codespace 以使用最新鏡像

## 📞 支援

如果遇到問題：

1. 運行 `bash .devcontainer/test-codespaces.sh` 診斷環境
2. 檢查 [GitHub Actions](https://github.com/GenKoKo/test_python_fastapi/actions) 的構建狀態
3. 查看 [Issues](https://github.com/GenKoKo/test_python_fastapi/issues) 或創建新的問題報告
