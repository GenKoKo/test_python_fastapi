"""
FastAPI 應用配置管理
使用環境變量和 Pydantic Settings 進行配置管理
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """應用配置類"""
    
    # 應用基本配置
    app_name: str = Field(default="FastAPI 初級入門 API", env="APP_NAME")
    app_description: str = Field(
        default="這是一個 FastAPI 的基本入門實作，包含常用的 API 操作", 
        env="APP_DESCRIPTION"
    )
    app_version: str = Field(default="1.0.0", env="APP_VERSION")
    
    # 服務器配置
    host: str = Field(default="127.0.0.1", env="HOST")
    port: int = Field(default=8000, env="PORT")
    reload: bool = Field(default=True, env="RELOAD")
    
    # 日誌配置
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    log_format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        env="LOG_FORMAT"
    )
    log_file: Optional[str] = Field(default=None, env="LOG_FILE")
    
    # 測試配置
    enable_auto_test: bool = Field(default=True, env="ENABLE_AUTO_TEST")
    test_delay: int = Field(default=2, env="TEST_DELAY")
    
    # 數據配置
    populate_sample_data: bool = Field(default=True, env="POPULATE_SAMPLE_DATA")
    
    # API 配置
    api_prefix: str = Field(default="", env="API_PREFIX")
    docs_url: str = Field(default="/docs", env="DOCS_URL")
    redoc_url: str = Field(default="/redoc", env="REDOC_URL")
    
    # 開發模式配置
    debug: bool = Field(default=False, env="DEBUG")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# 創建全局配置實例
settings = Settings()


def get_settings() -> Settings:
    """獲取配置實例"""
    return settings


# 配置驗證函數
def validate_config():
    """驗證配置的有效性"""
    errors = []
    
    if not (1024 <= settings.port <= 65535):
        errors.append(f"端口號必須在 1024-65535 範圍內，當前值: {settings.port}")
    
    if settings.log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        errors.append(f"日誌級別無效: {settings.log_level}")
    
    if settings.test_delay < 0:
        errors.append(f"測試延遲時間不能為負數: {settings.test_delay}")
    
    if errors:
        raise ValueError("配置驗證失敗:\n" + "\n".join(errors))
    
    return True


# 打印配置信息（用於調試）
def print_config():
    """打印當前配置（隱藏敏感信息）"""
    print("📋 當前配置:")
    print(f"  應用名稱: {settings.app_name}")
    print(f"  版本: {settings.app_version}")
    print(f"  服務器: {settings.host}:{settings.port}")
    print(f"  日誌級別: {settings.log_level}")
    print(f"  調試模式: {settings.debug}")
    print(f"  自動測試: {settings.enable_auto_test}")
    print(f"  示例數據: {settings.populate_sample_data}")