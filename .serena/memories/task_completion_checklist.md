# 任務完成後的檢查清單

## 代碼質量檢查

### 語法和格式檢查
```bash
# Python 語法檢查
python -m py_compile main.py

# 檢查所有 Python 文件
find . -name "*.py" -exec python -m py_compile {} \;
```

### 功能測試
```bash
# 運行自動測試
./run_app.sh
# 觀察終端輸出，確保所有測試通過

# 手動測試
./test_in_venv.sh

# 虛擬環境驗證
python test_venv.py
```

### API 文檔檢查
1. 啟動服務器: `./run_app.sh`
2. 訪問 Swagger UI: http://127.0.0.1:8000/docs
3. 確保所有端點都有正確的文檔
4. 測試關鍵 API 端點

## 部署前檢查

### 依賴管理
```bash
# 更新依賴文件
source fastapi_env/bin/activate
pip freeze > requirements.txt

# 檢查依賴版本
pip list --outdated
```

### 安全檢查
- 確保沒有硬編碼的敏感信息
- 檢查 .gitignore 是否包含虛擬環境
- 驗證錯誤處理不會洩露敏感信息

### 性能檢查
- 測試 API 響應時間
- 檢查內存使用情況
- 驗證並發請求處理

## 文檔更新

### README.md 檢查
- 確保安裝說明是最新的
- 驗證所有示例代碼可以運行
- 更新 API 端點列表

### 代碼註釋
- 檢查所有函數都有適當的文檔字符串
- 確保複雜邏輯有註釋說明
- 驗證類型提示的準確性

## 版本控制

### Git 檢查
```bash
# 檢查狀態
git status

# 添加文件
git add .

# 提交更改
git commit -m "描述性提交信息"

# 檢查歷史
git log --oneline
```

### 分支管理
- 確保在正確的分支上工作
- 合併前進行代碼審查
- 標記重要版本