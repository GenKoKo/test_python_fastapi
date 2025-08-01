# 項目架構和代碼結構

## 文件結構
```
test_python_fastapi/
├── main.py                 # 主應用文件
├── requirements.txt        # Python 依賴
├── README.md              # 項目文檔
├── .gitignore             # Git 忽略文件
├── setup_venv.sh          # Linux/macOS 虛擬環境設置
├── setup_venv.bat         # Windows 虛擬環境設置
├── run_app.sh             # 應用運行腳本
├── test_api.py            # API 測試腳本
├── test_in_venv.sh        # 虛擬環境測試腳本
├── test_venv.py           # 虛擬環境驗證腳本
└── fastapi_env/           # 虛擬環境目錄（運行時創建）
```

## 核心組件

### main.py 架構
- **FastAPI 應用實例**: 配置了標題、描述和版本
- **Pydantic 模型**: Item 和 User 數據模型
- **內存數據庫**: 使用 Python 列表模擬數據庫
- **API 路由**: 分為商品管理、用戶管理、搜索和統計功能
- **生命週期事件**: 啟動時自動填充數據和運行測試
- **自動測試**: 後台線程運行 API 測試

### API 端點組織
1. **基本端點**: `/`, `/health`, `/stats`
2. **商品管理**: `/items/*` 的 CRUD 操作
3. **用戶管理**: `/users/*` 的基本操作
4. **搜索功能**: `/search/items` 支持多參數查詢

### 數據模型
- **Item**: id, name, description, price, is_available
- **User**: id, username, email, full_name
- 使用 Pydantic 進行數據驗證和序列化