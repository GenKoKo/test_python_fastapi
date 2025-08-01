# 代碼風格和約定

## Python 代碼風格

### 命名約定
- **變量和函數**: snake_case (例: `next_item_id`, `get_all_items`)
- **類名**: PascalCase (例: `Item`, `User`)
- **常量**: UPPER_SNAKE_CASE
- **私有變量**: 以下劃線開頭 (例: `_private_var`)

### 類型提示
- 使用 Python 類型提示 (typing module)
- 函數參數和返回值都有類型註解
- 使用 `Optional[type]` 表示可選參數
- 使用 `List[type]` 表示列表類型

### 文檔字符串
- 使用三引號 `"""` 格式
- 簡潔描述函數功能
- 中文註釋，便於理解

### FastAPI 特定約定
- 路由函數使用 `async def` 或 `def`
- Pydantic 模型繼承 `BaseModel`
- 使用裝飾器定義 HTTP 方法 (`@app.get`, `@app.post` 等)
- 響應模型使用 `response_model` 參數

## 代碼組織

### 文件結構
- 單文件應用 (main.py) 適合小型項目
- 按功能分組路由 (商品、用戶、搜索、統計)
- 模型定義在文件頂部
- 全局變量集中管理

### 錯誤處理
- 使用 `HTTPException` 處理 HTTP 錯誤
- 提供有意義的錯誤消息
- 使用適當的 HTTP 狀態碼

### 數據驗證
- 使用 Pydantic 模型進行自動驗證
- 設置合理的默認值
- 使用 Optional 處理可選字段

## 測試約定

### 測試文件命名
- 測試文件以 `test_` 開頭
- 功能描述性命名

### 測試結構
- 使用 requests 庫進行 HTTP 測試
- 測試覆蓋所有主要 API 端點
- 包含正面和負面測試案例