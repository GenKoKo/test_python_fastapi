"""
日誌配置模組
提供統一的日誌記錄功能
"""

import logging
import logging.handlers
import sys
from pathlib import Path
from typing import Optional
from config import settings


class ColoredFormatter(logging.Formatter):
    """彩色日誌格式化器"""
    
    # ANSI 顏色代碼
    COLORS = {
        'DEBUG': '\033[36m',      # 青色
        'INFO': '\033[32m',       # 綠色
        'WARNING': '\033[33m',    # 黃色
        'ERROR': '\033[31m',      # 紅色
        'CRITICAL': '\033[35m',   # 紫色
        'RESET': '\033[0m'        # 重置
    }
    
    def format(self, record):
        # 添加顏色
        if record.levelname in self.COLORS:
            record.levelname = (
                f"{self.COLORS[record.levelname]}"
                f"{record.levelname}"
                f"{self.COLORS['RESET']}"
            )
        
        return super().format(record)


def setup_logger(
    name: str = "fastapi_app",
    level: Optional[str] = None,
    log_file: Optional[str] = None,
    format_string: Optional[str] = None
) -> logging.Logger:
    """
    設置日誌記錄器
    
    Args:
        name: 日誌記錄器名稱
        level: 日誌級別
        log_file: 日誌文件路徑
        format_string: 日誌格式字符串
    
    Returns:
        配置好的日誌記錄器
    """
    
    # 使用配置中的默認值
    level = level or settings.log_level
    log_file = log_file or settings.log_file
    format_string = format_string or settings.log_format
    
    # 創建日誌記錄器
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # 清除現有的處理器
    logger.handlers.clear()
    
    # 控制台處理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, level.upper()))
    
    # 使用彩色格式化器
    if sys.stdout.isatty():  # 如果是終端，使用彩色
        console_formatter = ColoredFormatter(format_string)
    else:  # 如果是重定向，使用普通格式
        console_formatter = logging.Formatter(format_string)
    
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # 文件處理器（如果指定了日誌文件）
    if log_file:
        # 確保日誌目錄存在
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 使用輪轉文件處理器
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setLevel(getattr(logging, level.upper()))
        
        # 文件日誌不使用顏色
        file_formatter = logging.Formatter(format_string)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    
    return logger


def get_logger(name: str = "fastapi_app") -> logging.Logger:
    """獲取日誌記錄器"""
    return logging.getLogger(name)


# 創建應用日誌記錄器
app_logger = setup_logger("fastapi_app")


# 日誌記錄裝飾器
def log_function_call(logger: Optional[logging.Logger] = None):
    """
    函數調用日誌裝飾器
    
    Args:
        logger: 日誌記錄器，如果為 None 則使用默認記錄器
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            log = logger or app_logger
            log.debug(f"調用函數: {func.__name__}")
            try:
                result = func(*args, **kwargs)
                log.debug(f"函數 {func.__name__} 執行成功")
                return result
            except Exception as e:
                log.error(f"函數 {func.__name__} 執行失敗: {e}")
                raise
        return wrapper
    return decorator


# API 請求日誌中間件輔助函數
def log_request(method: str, url: str, status_code: int, duration: float):
    """記錄 API 請求日誌"""
    app_logger.info(
        f"API 請求 - {method} {url} - 狀態碼: {status_code} - 耗時: {duration:.3f}s"
    )


def log_error(error: Exception, context: str = ""):
    """記錄錯誤日誌"""
    app_logger.error(f"錯誤發生 {context}: {type(error).__name__}: {error}")


def log_startup():
    """記錄應用啟動日誌"""
    app_logger.info("🚀 FastAPI 應用正在啟動...")
    app_logger.info(f"📋 配置 - 主機: {settings.host}, 端口: {settings.port}")
    app_logger.info(f"📋 配置 - 日誌級別: {settings.log_level}")
    if settings.debug:
        app_logger.warning("⚠️  調試模式已啟用")


def log_shutdown():
    """記錄應用關閉日誌"""
    app_logger.info("👋 FastAPI 應用正在關閉...")


# 測試日誌功能
if __name__ == "__main__":
    # 測試日誌記錄
    test_logger = setup_logger("test", level="DEBUG")
    
    test_logger.debug("這是調試信息")
    test_logger.info("這是信息")
    test_logger.warning("這是警告")
    test_logger.error("這是錯誤")
    test_logger.critical("這是嚴重錯誤")