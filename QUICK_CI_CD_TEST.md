# 🚀 CI/CD 快速測試指南

## 📋 一鍵測試方案

### 方法一：使用自動化腳本（推薦）

```bash
# 執行完整 CI/CD 測試
./scripts/test_ci_cd.sh

# 或分階段測試
./scripts/test_ci_cd.sh feature    # Feature CI 測試
./scripts/test_ci_cd.sh ci         # 主要 CI 測試
./scripts/test_ci_cd.sh cd         # CD 部署測試
./scripts/test_ci_cd.sh codespaces # Codespaces 驗證
```

### 方法二：手動快速測試

#### 1️⃣ Feature CI 測試（3 分鐘）

```bash
# 創建測試分支
git checkout -b feature/quick-test
echo "# Quick CI Test" > test.md
git add test.md
git commit -m "feat: quick CI test"
git push origin feature/quick-test

# ✅ 檢查 GitHub Actions 中的 Feature Branch CI
```

#### 2️⃣ 完整 CI 測試（5 分鐘）

```bash
# 創建 Pull Request（在 GitHub 網頁上）
# feature/quick-test -> main

# ✅ 檢查 GitHub Actions 中的 CI/CD Pipeline
```

#### 3️⃣ CD 部署測試（8 分鐘）

```bash
# 合併 PR 到 main 分支

# ✅ 檢查以下 Actions 是否執行：
# - CI/CD Pipeline
# - CD - Deploy to GitHub Codespaces
```

#### 4️⃣ Codespaces 驗證（3 分鐘）

```bash
# 在 GitHub 上創建新的 Codespace
# 1. Code -> Codespaces -> Create codespace
# 2. 等待環境設置完成
# 3. 運行: just dev
# 4. 檢查 API 文檔: https://your-codespace-8000.app.github.dev/docs
```

## 🎯 預期結果檢查

### Feature CI 應該顯示：

-   ✅ Quick Quality Check (通過)
-   ✅ Code formatting check
-   ✅ Quick lint check
-   ✅ Fast unit tests
-   ✅ Notify Results

### 完整 CI 應該顯示：

-   ✅ Code Quality Checks
-   ✅ Unit Tests (Python 3.9, 3.10, 3.11)
-   ✅ Docker Build & Test
-   ✅ Security Scan
-   ✅ Build and push Docker image

### CD 部署應該顯示：

-   ✅ Build Codespaces Image
-   ✅ Update Codespaces Configuration
-   ✅ Trigger Prebuild
-   ✅ Verify Deployment
-   ✅ Create Deployment Report

### Codespaces 應該能夠：

-   ✅ 自動設置環境
-   ✅ 運行 `just dev` 成功
-   ✅ 訪問 API 文檔
-   ✅ 所有功能正常

## ⚡ 超快速測試（1 分鐘）

如果你只想快速驗證 CI/CD 是否工作：

```bash
# 觸發 Feature CI
git checkout -b feature/test-$(date +%s)
git commit --allow-empty -m "feat: trigger CI test"
git push origin feature/test-$(date +%s)

# 檢查 GitHub Actions 是否有新的工作流程執行
```

## 🛠️ 故障排除

### 如果 Feature CI 失敗：

```bash
# 本地檢查
just format  # 修復格式問題
just lint    # 檢查代碼問題
just test-unit # 運行測試
```

### 如果 Docker 構建失敗：

```bash
# 本地測試
just docker-build
```

### 如果 CD 部署失敗：

-   檢查 GitHub Token 權限
-   確保在 main 分支
-   檢查文件路徑觸發條件

### 如果 Codespaces 有問題：

```bash
# 在 Codespace 中
just codespaces-status
just codespaces-reset  # 重置環境
```

## 📊 測試完成檢查清單

-   [ ] Feature CI 執行成功
-   [ ] 完整 CI 流程通過
-   [ ] CD 部署流程完成
-   [ ] Codespaces 環境可用
-   [ ] API 應用正常運行
-   [ ] 所有自動化觸發正確

## 🎉 成功標準

當你看到以下情況時，說明 CI/CD 流程完全正常：

1. **綠色的 GitHub Actions 徽章** ✅
2. **Codespace 可以正常創建和使用** 🌟
3. **API 文檔可以正常訪問** 📖
4. **所有測試都通過** 🧪
5. **部署報告顯示成功** 📊

---

💡 **提示**: 使用自動化腳本 `./scripts/test_ci_cd.sh` 可以獲得最佳的測試體驗！
