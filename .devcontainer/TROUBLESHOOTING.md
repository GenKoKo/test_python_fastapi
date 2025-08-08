# 🔧 Codespaces 故障排除指南

## 🚨 常見問題和解決方案

### 問題 1: Container creation failed

**症狀**: Codespaces 創建失敗，使用 recovery container (Alpine)

**原因**:

-   自定義 Docker 鏡像啟動失敗
-   缺少基本系統工具（如 `sleep`）
-   用戶權限配置問題

**解決方案**:

```bash
# 1. 檢查最新的鏡像是否構建成功
# 查看 GitHub Actions: https://github.com/GenKoKo/test_python_fastapi/actions

# 2. 驗證環境
bash .devcontainer/validate-fix.sh

# 3. 如果仍有問題，使用簡化配置
cp .devcontainer/devcontainer.simple.json .devcontainer/devcontainer.json
```

### 問題 2: just 命令不可用

**症狀**: `just: command not found`

**診斷**:

```bash
# 檢查 just 是否安裝
which just
ls -la /usr/local/bin/just

# 檢查 PATH
echo $PATH
```

**解決方案**:

```bash
# 方案 1: 重新載入環境
source ~/.bashrc

# 方案 2: 手動添加到 PATH
export PATH="/usr/local/bin:$PATH"

# 方案 3: 使用完整路徑
/usr/local/bin/just --version

# 方案 4: 重新安裝
bash .devcontainer/install-just.sh
```

### 問題 3: Python 環境問題

**症狀**: Python 或 uv 不可用

**診斷**:

```bash
# 檢查 Python
python --version
which python

# 檢查 uv
uv --version
which uv

# 檢查虛擬環境
ls -la .venv/
```

**解決方案**:

```bash
# 重新同步依賴
uv sync --dev

# 如果 uv 不可用，使用 pip
pip install -r requirements/base.txt
```

### 問題 4: 權限問題

**症狀**: Permission denied 錯誤

**診斷**:

```bash
# 檢查當前用戶
whoami
id

# 檢查目錄權限
ls -la /app
ls -la /workspaces
```

**解決方案**:

```bash
# 如果是權限問題，使用 sudo
sudo chown -R vscode:vscode /app
sudo chown -R vscode:vscode /workspaces
```

## 🧪 診斷工具

### 完整環境檢查

```bash
bash .devcontainer/validate-fix.sh
```

### 快速檢查

```bash
bash .devcontainer/test-codespaces.sh
```

### 手動驗證步驟

```bash
# 1. 基本命令
sleep 1 && echo "sleep 工作正常"
curl --version
git --version

# 2. Just 命令
just --version
just --list

# 3. Python 環境
python --version
uv --version

# 4. 啟動應用
just dev
```

## 🔄 重置環境

如果所有方法都失敗，可以嘗試：

### 方案 1: 重新創建 Codespace

1. 刪除當前 Codespace
2. 等待 5-10 分鐘
3. 創建新的 Codespace

### 方案 2: 使用備用配置

```bash
# 使用簡化配置
cp .devcontainer/devcontainer.simple.json .devcontainer/devcontainer.json

# 或使用基礎 Python 鏡像
# 編輯 .devcontainer/devcontainer.json:
# "image": "mcr.microsoft.com/devcontainers/python:3.11"
```

### 方案 3: 手動設置

```bash
# 如果使用基礎鏡像，手動安裝工具
curl -LsSf https://astral.sh/uv/install.sh | sh
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
export PATH="$HOME/.local/bin:$PATH"
```

## 📞 獲取幫助

如果問題仍然存在：

1. **檢查 GitHub Actions**: 確認 Docker 鏡像構建成功
2. **查看 Creation Log**: 在 Codespaces 中查看詳細錯誤信息
3. **運行診斷腳本**: `bash .devcontainer/validate-fix.sh`
4. **創建 Issue**: 在 GitHub 倉庫中報告問題

## 📋 檢查清單

在報告問題前，請確認：

-   [ ] 最新的 commit 已推送到 master 分支
-   [ ] GitHub Actions 中的 CD 工作流程成功完成
-   [ ] 已運行 `validate-fix.sh` 診斷腳本
-   [ ] 已嘗試重新創建 Codespace
-   [ ] 已檢查 Codespaces creation log 中的錯誤信息

## 🎯 預期的正常狀態

修復成功後，你應該能夠：

-   ✅ 成功創建 Codespace（不使用 recovery container）
-   ✅ 運行 `just --version` 查看版本
-   ✅ 運行 `just --list` 查看可用命令
-   ✅ 運行 `just dev` 啟動開發服務器
-   ✅ 訪問 http://localhost:8000/docs 查看 API 文檔
-   ✅ 運行 `just test-unit` 執行測試
