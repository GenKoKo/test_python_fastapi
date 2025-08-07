# 🚀 Codespaces 開發環境設置

## 📋 自動安裝流程

當您創建 Codespace 時，以下流程會自動執行：

### 1. **devcontainer.json 配置**

```json
{
    "postCreateCommand": "bash .devcontainer/setup.sh",
    "containerEnv": {
        "PATH": "/home/vscode/.local/bin:${containerEnv:PATH}"
    }
}
```

### 2. **setup.sh 主要安裝腳本**

-   安裝 uv 包管理器
-   調用 `install-just.sh` 安裝 Just
-   同步 Python 依賴
-   驗證環境設置

### 3. **install-just.sh 專用 Just 安裝**

-   創建 `~/.local/bin` 目錄
-   下載並安裝 Just 到用戶目錄
-   設定 PATH 環境變數
-   添加到 shell 配置文件

## 🔧 手動修復方法

如果自動安裝失敗，您可以手動執行：

### 方法 1: 使用修復腳本

```bash
bash scripts/fix-just-install.sh
```

### 方法 2: 使用專用安裝腳本

```bash
bash .devcontainer/install-just.sh
source ~/.bashrc
```

### 方法 3: 手動安裝

```bash
mkdir -p ~/.local/bin
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## 🧪 驗證安裝

```bash
# 檢查 Just 是否可用
just --version

# 查看所有可用命令
just --list

# 啟動開發服務器
just dev
```

## ⚠️ 常見問題

### 問題 1: `just: command not found`

**解決方案**:

```bash
source ~/.bashrc
# 或
export PATH="$HOME/.local/bin:$PATH"
```

### 問題 2: 權限被拒絕

**原因**: 嘗試安裝到 `/usr/local/bin`
**解決方案**: 使用用戶目錄 `~/.local/bin`

### 問題 3: PATH 沒有生效

**解決方案**:

```bash
echo $PATH  # 檢查 PATH
source ~/.bashrc  # 重新載入配置
```

## 📁 相關文件

-   `devcontainer.json` - 容器配置
-   `setup.sh` - 主要設置腳本
-   `install-just.sh` - Just 專用安裝腳本
-   `../scripts/fix-just-install.sh` - 修復腳本（scripts 目錄）

## 🎯 預期結果

安裝完成後，您應該能夠：

-   ✅ 執行 `just --version` 查看版本
-   ✅ 執行 `just --list` 查看命令列表
-   ✅ 執行 `just dev` 啟動開發服務器
-   ✅ 在新的終端 session 中使用 just 命令
