"""
FastAPI 應用配置管理
使用環境變量和 Pydantic Settings 進行配置管理
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Annotated


class Settings(BaseSettings):
    """應用配置類"""

    # 應用基本配置
    app_name: Annotated[str, Field(alias="APP_NAME")] = "FastAPI 初級入門 API"
    app_description: Annotated[str, Field(alias="APP_DESCRIPTION")] = (
        "這是一個 FastAPI 的基本入門實作，包含常用的 API 操作"
    )
    app_version: Annotated[str, Field(alias="APP_VERSION")] = "1.0.0"

    # 服務器配置
    host: Annotated[str, Field(alias="HOST")] = "127.0.0.1"
    port: Annotated[int, Field(alias="PORT")] = 8000
    reload: Annotated[bool, Field(alias="RELOAD")] = True

    # 日誌配置
    log_level: Annotated[str, Field(alias="LOG_LEVEL")] = "INFO"
    log_format: Annotated[str, Field(alias="LOG_FORMAT")] = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    log_file: Annotated[Optional[str], Field(alias="LOG_FILE")] = None

    # 測試配置
    enable_auto_test: Annotated[bool, Field(alias="ENABLE_AUTO_TEST")] = True
    test_delay: Annotated[int, Field(alias="TEST_DELAY")] = 2

    # 數據配置
    populate_sample_data: Annotated[bool, Field(alias="POPULATE_SAMPLE_DATA")] = True

    # API 配置
    api_prefix: Annotated[str, Field(alias="API_PREFIX")] = ""
    docs_url: Annotated[str, Field(alias="DOCS_URL")] = "/docs"
    redoc_url: Annotated[str, Field(alias="REDOC_URL")] = "/redoc"

    # 開發模式配置
    debug: Annotated[bool, Field(alias="DEBUG")] = False

    # 環境配置 (從 .env 文件中讀取的額外配置)
    environment: Annotated[Optional[str], Field(alias="ENVIRONMENT")] = None
    pythonpath: Annotated[Optional[str], Field(alias="PYTHONPATH")] = None

    # API 版本配置
    api_v1_str: Annotated[str, Field(alias="API_V1_STR")] = "/api/v1"
    project_name: Annotated[str, Field(alias="PROJECT_NAME")] = "FastAPI Development"
    version: Annotated[str, Field(alias="VERSION")] = "1.0.0"

    # 文檔配置
    enable_docs: Annotated[bool, Field(alias="ENABLE_DOCS")] = True
    enable_redoc: Annotated[bool, Field(alias="ENABLE_REDOC")] = True
    enable_openapi: Annotated[bool, Field(alias="ENABLE_OPENAPI")] = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "ignore"  # 忽略額外的環境變數


# 創建全局配置實例
settings = Settings()


def get_settings() -> Settings:
    """獲取配置實例"""
    return settings


# 配置驗證函數
def validate_config() -> bool:
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
def print_config() -> None:
    """打印當前配置（隱藏敏感信息）"""
    print("📋 當前配置:")
    print(f"  應用名稱: {settings.app_name}")
    print(f"  版本: {settings.app_version}")
    print(f"  服務器: {settings.host}:{settings.port}")
    print(f"  日誌級別: {settings.log_level}")
    print(f"  調試模式: {settings.debug}")
    print(f"  自動測試: {settings.enable_auto_test}")
    print(f"  示例數據: {settings.populate_sample_data}")
