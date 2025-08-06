# 🚀 遷移到 uv 包管理器

## 📋 遷移概述

本專案已從傳統的 `pip + requirements.txt` 遷移到現代的 `uv` 包管理器。

## ✅ 已完成的遷移步驟

### 1. 依賴管理遷移

-   ✅ 更新 `pyproject.toml` 配置
-   ✅ 生成 `uv.lock` 鎖定文件
-   ✅ 添加所有必要的開發依賴
-   ✅ 清理舊的 `fastapi_env` 虛擬環境

### 2. 工具配置更新

-   ✅ 更新 `justfile` 使用 `uv run` 命令
-   ✅ 更新所有開發命令（test, format, lint 等）
-   ✅ 更新 CI/CD 配置使用 uv
-   ✅ 更新 GitHub Codespaces 配置

### 3. 環境清理

-   ✅ 移除舊的 `fastapi_env/` 目錄
-   ✅ 保留 `requirements/` 目錄作為參考（可選擇刪除）

## 🔧 新的開發工作流程

### 環境設置

```bash
# 安裝 uv（如果尚未安裝）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 設置開發環境
just setup
# 或直接使用 uv
uv sync --dev
```

### 日常開發命令

```bash
# 啟動開發服務器
just dev
# 或
uv run uvicorn src.app.main:app --reload

# 運行測試
just test-unit
# 或
uv run pytest tests/ -v

# 格式化代碼
just format
# 或
uv run black .

# 安裝新依賴
just install requests
# 或
uv add requests

# 安裝開發依賴
just install-dev pytest-mock
# 或
uv add --dev pytest-mock
```

## 📊 遷移優勢

### 🚀 性能提升

-   **10-100x 更快**的依賴解析和安裝
-   **更快的虛擬環境創建**
-   **並行下載和安裝**

### 🔒 更好的依賴管理

-   **精確的依賴鎖定** (`uv.lock`)
-   **更好的依賴衝突解決**
-   **統一的工具鏈**

### 🛠️ 開發體驗改善

-   **單一工具**管理所有 Python 需求
-   **與 pyproject.toml 完美整合**
-   **現代化的命令行界面**

## 🔄 向後兼容性

### 保留的文件

-   `requirements/` 目錄（作為參考，可選擇保留）
-   所有現有的 `just` 命令仍然可用
-   CI/CD 流程保持不變

### 環境變數

舊的 `VIRTUAL_ENV` 環境變數可能會顯示警告，這是正常的。uv 會自動管理虛擬環境。

## 🚨 注意事項

### 1. 環境變數警告

你可能會看到這樣的警告：

```
warning: `VIRTUAL_ENV=fastapi_env` does not match the project environment path `.venv` and will be ignored
```

這是正常的，uv 會使用 `.venv` 作為新的虛擬環境路徑。

### 2. IDE 配置

如果你的 IDE 還指向舊的 `fastapi_env`，請更新為 `.venv`：

-   **VS Code**: 更新 Python 解釋器路徑
-   **PyCharm**: 更新項目解釋器設置

### 3. 清理舊環境變數

如果需要，可以清理舊的環境變數：

```bash
unset VIRTUAL_ENV
```

## 🔧 故障排除

### 問題：uv 命令未找到

```bash
# 安裝 uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc  # 或 ~/.zshrc
```

### 問題：依賴衝突

```bash
# 重新同步依賴
uv sync --dev
```

### 問題：舊環境干擾

```bash
# 清理並重新設置
just clean
just setup
```

## 📚 更多資源

-   [uv 官方文檔](https://docs.astral.sh/uv/)
-   [uv GitHub 倉庫](https://github.com/astral-sh/uv)
-   [Python 包管理最佳實踐](https://packaging.python.org/)

## 🎯 下一步

1. **測試新環境**：運行 `just test-unit` 確保一切正常
2. **更新 IDE 設置**：指向新的 `.venv` 環境
3. **清理舊文件**：可選擇刪除 `requirements/` 目錄
4. **團隊同步**：確保團隊成員都安裝了 uv

---

**遷移完成！** 🎉 現在你可以享受更快、更現代的 Python 開發體驗了。
