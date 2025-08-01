"""
中間件
提供請求處理中間件
"""

import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from src.core.logger import app_logger, log_request, log_error


class LoggingMiddleware(BaseHTTPMiddleware):
    """API 請求日誌中間件"""
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # 記錄請求開始
        app_logger.debug(f"📥 收到請求: {request.method} {request.url}")
        
        try:
            response = await call_next(request)
            
            # 計算處理時間
            process_time = time.time() - start_time
            
            # 記錄請求完成
            log_request(
                method=request.method,
                url=str(request.url),
                status_code=response.status_code,
                duration=process_time
            )
            
            # 添加處理時間到響應頭
            response.headers["X-Process-Time"] = str(process_time)
            
            return response
            
        except Exception as e:
            process_time = time.time() - start_time
            log_error(e, f"處理請求 {request.method} {request.url}")
            
            # 記錄錯誤請求
            app_logger.error(
                f"❌ 請求失敗 - {request.method} {request.url} - 耗時: {process_time:.3f}s"
            )
            raise


class CORSMiddleware(BaseHTTPMiddleware):
    """CORS 中間件（簡單實現）"""
    
    def __init__(self, app, allow_origins=None, allow_methods=None, allow_headers=None):
        super().__init__(app)
        self.allow_origins = allow_origins or ["*"]
        self.allow_methods = allow_methods or ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
        self.allow_headers = allow_headers or ["*"]
    
    async def dispatch(self, request: Request, call_next):
        if request.method == "OPTIONS":
            # 處理預檢請求
            response = Response()
            response.headers["Access-Control-Allow-Origin"] = ", ".join(self.allow_origins)
            response.headers["Access-Control-Allow-Methods"] = ", ".join(self.allow_methods)
            response.headers["Access-Control-Allow-Headers"] = ", ".join(self.allow_headers)
            return response
        
        response = await call_next(request)
        
        # 添加 CORS 頭
        response.headers["Access-Control-Allow-Origin"] = ", ".join(self.allow_origins)
        response.headers["Access-Control-Allow-Methods"] = ", ".join(self.allow_methods)
        response.headers["Access-Control-Allow-Headers"] = ", ".join(self.allow_headers)
        
        return response