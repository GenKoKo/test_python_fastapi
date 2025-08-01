# 開發命令和工作流程

## 環境設置命令

### 初始設置
```bash
# macOS/Linux
./setup_venv.sh

# Windows
setup_venv.bat

# 手動設置
python3 -m venv fastapi_env
source fastapi_env/bin/activate  # macOS/Linux
# fastapi_env\Scripts\activate.bat  # Windows
pip install -r requirements.txt
```

## 運行命令

### 啟動應用
```bash
# 推薦方式（自動激活虛擬環境）
./run_app.sh

# 手動方式
source fastapi_env/bin/activate
python main.py

# 使用 uvicorn 直接運行
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# 使用 FastAPI CLI（如果已安裝）
fastapi dev main.py
```

### 測試命令
```bash
# 自動測試（服務器啟動時自動運行）
./run_app.sh

# 手動測試
./test_in_venv.sh

# 虛擬環境驗證
python test_venv.py

# 直接運行測試（需要服務器運行）
source fastapi_env/bin/activate
python test_api.py
```

## 開發工具命令

### 虛擬環境管理
```bash
# 激活虛擬環境
source fastapi_env/bin/activate

# 退出虛擬環境
deactivate

# 檢查當前環境
which python

# 查看已安裝包
pip list

# 更新依賴文件
pip freeze > requirements.txt
```

### 系統命令（macOS）
```bash
# 文件操作
ls -la                    # 列出文件
find . -name "*.py"       # 查找 Python 文件
grep -r "pattern" .       # 搜索文本

# 權限管理
chmod +x *.sh            # 給腳本執行權限

# 進程管理
ps aux | grep python     # 查看 Python 進程
kill -9 <pid>           # 終止進程
```

## 訪問地址
- **API 根路徑**: http://127.0.0.1:8000/
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc