# 🚀 CI/CD 流程完整測試指南

## 🎯 測試策略概覽

本指南將幫你完整測試項目的 CI/CD 流程，包括 Feature CI、主要 CI 和 CD 部署流程。

## 📋 測試流程規劃

### 階段 1: Feature CI 測試

### 階段 2: 主要 CI 測試

### 階段 3: CD 部署測試

### 階段 4: 完整流程驗證

---

## 🔧 階段 1: Feature CI 測試

### 目標

測試功能分支的快速品質檢查流程

### 步驟

#### 1.1 創建測試分支

```bash
# 創建 feature 分支
git checkout -b feature/ci-testing

# 做一個小改動來觸發 CI
echo "# CI Testing" >> docs/CI_TESTING.md
git add docs/CI_TESTING.md
git commit -m "feat: add CI testing documentation"

# 推送分支觸發 Feature CI
git push origin feature/ci-testing
```

#### 1.2 預期結果

-   ✅ Quick Quality Check 作業執行
-   ✅ 代碼格式檢查通過
-   ✅ 快速 lint 檢查通過
-   ✅ 單元測試執行通過
-   ✅ 通知結果顯示成功

#### 1.3 測試 Docker 構建觸發

```bash
# 測試 Docker 構建觸發條件
git commit --allow-empty -m "feat: test docker build [docker]"
git push origin feature/ci-testing
```

#### 1.4 預期結果

-   ✅ Quick Quality Check 執行
-   ✅ Build Verification 作業執行
-   ✅ Docker 鏡像構建成功

---

## 🏗️ 階段 2: 主要 CI 測試

### 目標

測試完整的 CI 流程，包括多 Python 版本測試和 Docker 構建

### 步驟

#### 2.1 創建 Pull Request

```bash
# 在 GitHub 上創建 PR: feature/ci-testing -> main
# 這將觸發完整的 CI 流程
```

#### 2.2 預期結果

-   ✅ Code Quality Checks 執行
-   ✅ Unit Tests (Python 3.9, 3.10, 3.11) 執行
-   ✅ Docker Build & Test 執行
-   ✅ Security Scan 執行
-   ✅ 所有檢查通過

#### 2.3 手動觸發完整測試

```bash
# 在 GitHub Actions 頁面手動觸發 CI/CD Pipeline
# 選擇 "Run full test suite including Docker builds" = true
```

#### 2.4 預期結果

-   ✅ 所有 CI 作業執行
-   ✅ 完整的測試套件運行
-   ✅ Docker 構建和測試完成

---

## 🚀 階段 3: CD 部署測試

### 目標

測試自動部署到 GitHub Codespaces 的流程

### 步驟

#### 3.1 合併到主分支

```bash
# 合併 PR 到 main 分支
# 這將觸發 CI 和 CD 流程
```

#### 3.2 預期結果

-   ✅ 完整 CI 流程執行
-   ✅ Docker 鏡像構建和推送
-   ✅ 觸發 Codespaces 部署
-   ✅ CD 流程自動執行

#### 3.3 驗證 CD 流程

檢查以下作業是否成功：

-   ✅ Build Codespaces Image
-   ✅ Update Codespaces Configuration
-   ✅ Trigger Prebuild
-   ✅ Verify Deployment
-   ✅ Create Deployment Report

#### 3.4 手動觸發 CD

```bash
# 在 GitHub Actions 頁面手動觸發 CD - Deploy to GitHub Codespaces
# 選擇 "Force rebuild of Codespaces prebuilds" = true
```

---

## 🔄 階段 4: 完整流程驗證

### 目標

驗證整個 CI/CD 流程的端到端功能

### 步驟

#### 4.1 創建新功能分支

```bash
git checkout main
git pull origin main
git checkout -b feature/complete-test

# 做一個實際的功能改動
echo 'print("Hello CI/CD!")' >> src/app/test_endpoint.py
git add src/app/test_endpoint.py
git commit -m "feat: add test endpoint for CI/CD validation"
git push origin feature/complete-test
```

#### 4.2 完整流程測試

1. **Feature CI 觸發** - 推送分支後自動執行
2. **創建 PR** - 觸發完整 CI 流程
3. **代碼審查** - 檢查 CI 結果
4. **合併到 main** - 觸發 CI + CD 流程
5. **驗證部署** - 檢查 Codespaces 部署

#### 4.3 Codespaces 驗證

```bash
# 創建新的 Codespace 驗證部署
# 1. 前往 GitHub 倉庫頁面
# 2. 點擊 "Code" -> "Codespaces"
# 3. 創建新的 Codespace
# 4. 驗證環境自動設置
# 5. 運行 just dev 測試應用
```

---

## 📊 測試檢查清單

### Feature CI 檢查項目

-   [ ] 分支推送觸發 Feature CI
-   [ ] 代碼格式檢查執行
-   [ ] Lint 檢查執行
-   [ ] 單元測試執行
-   [ ] Docker 構建觸發條件正確
-   [ ] 通知結果正確顯示

### 主要 CI 檢查項目

-   [ ] PR 創建觸發完整 CI
-   [ ] 多 Python 版本測試
-   [ ] Docker 構建和測試
-   [ ] 安全掃描執行
-   [ ] 覆蓋率報告生成
-   [ ] 手動觸發功能正常

### CD 檢查項目

-   [ ] main 分支推送觸發 CD
-   [ ] Codespaces 鏡像構建
-   [ ] 配置文件自動更新
-   [ ] 預構建觸發成功
-   [ ] 部署驗證通過
-   [ ] 部署報告生成

### 端到端檢查項目

-   [ ] 完整開發流程順暢
-   [ ] 所有自動化觸發正確
-   [ ] Codespaces 環境可用
-   [ ] 應用正常運行
-   [ ] 文檔和配置同步

---

## 🛠️ 故障排除指南

### 常見問題和解決方案

#### 1. Feature CI 失敗

```bash
# 檢查代碼格式
just format

# 檢查 lint 問題
just lint

# 運行本地測試
just test-unit
```

#### 2. Docker 構建失敗

```bash
# 本地測試 Docker 構建
just docker-build

# 檢查 Dockerfile 語法
docker build -t test-image .
```

#### 3. CD 部署失敗

```bash
# 檢查 GitHub Token 權限
# 確保 GITHUB_TOKEN 有足夠權限

# 手動觸發 CD 流程
# 在 Actions 頁面手動運行
```

#### 4. Codespaces 環境問題

```bash
# 在 Codespace 中檢查環境
just codespaces-status

# 重置環境
just codespaces-reset
```

---

## 📈 性能監控

### CI/CD 執行時間基準

-   **Feature CI**: ~3-5 分鐘
-   **完整 CI**: ~8-12 分鐘
-   **CD 部署**: ~5-8 分鐘
-   **Codespace 創建**: ~2-3 分鐘

### 優化建議

-   使用 GitHub Actions 緩存
-   並行執行獨立作業
-   優化 Docker 層緩存
-   預構建 Codespaces 鏡像

---

## 🎯 最佳實踐

### 分支策略

```
main (生產)
├── develop (開發)
├── feature/* (功能)
├── bugfix/* (修復)
└── hotfix/* (熱修復)
```

### 提交訊息格式

```
feat: 新功能
fix: 修復 bug
docs: 文檔更新
style: 格式調整
refactor: 重構
test: 測試相關
chore: 其他雜項

# 觸發特殊構建
feat: add new feature [docker]
fix: critical bug [build]
docs: update guide [prebuild]
```

### 測試頻率建議

-   **每次推送**: Feature CI
-   **每個 PR**: 完整 CI
-   **每次合併**: CI + CD
-   **每週**: 完整流程驗證

---

## 📋 測試執行計劃

### 建議執行順序

#### 第一天: 基礎測試

1. 執行 Feature CI 測試
2. 修復發現的問題
3. 驗證基本功能

#### 第二天: 完整 CI 測試

1. 創建 PR 測試完整 CI
2. 測試多 Python 版本
3. 驗證 Docker 構建

#### 第三天: CD 部署測試

1. 合併到 main 觸發 CD
2. 驗證 Codespaces 部署
3. 測試端到端流程

#### 第四天: 優化和文檔

1. 分析性能指標
2. 優化慢速步驟
3. 更新文檔和指南

---

## 🎉 成功標準

### 完成標準

-   ✅ 所有 CI/CD 流程正常執行
-   ✅ 測試覆蓋率達到預期
-   ✅ 部署流程自動化完成
-   ✅ Codespaces 環境可用
-   ✅ 文檔和配置同步

### 品質標準

-   ✅ CI 執行時間在合理範圍
-   ✅ 錯誤處理和通知完善
-   ✅ 安全掃描無重大問題
-   ✅ 部署驗證通過
-   ✅ 用戶體驗良好

恭喜！完成所有測試後，你將擁有一個完全可靠的 CI/CD 流程！🚀
