# FastAPI Docker 多階段構建
FROM python:3.11-slim as base

# 設置工作目錄
WORKDIR /app

# 設置環境變數
ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 開發階段
FROM base as development

# Codespaces 和預構建支持
ARG CODESPACES=false
ARG INSTALL_DEV_TOOLS=false
ARG PREBUILD=false

# 安裝額外的系統工具（Codespaces 需要）
RUN if [ "$CODESPACES" = "true" ]; then \
    apt-get update && apt-get install -y \
        git \
        zsh \
        curl \
        wget \
        vim \
        nano \
        htop \
        tree \
        jq \
        && rm -rf /var/lib/apt/lists/*; \
    fi

# 安裝 Just 命令工具（Codespaces 需要）
RUN if [ "$CODESPACES" = "true" ]; then \
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin; \
    fi

# 複製依賴文件
COPY requirements/ requirements/

# 安裝 Python 依賴
RUN pip install --upgrade pip && \
    pip install -r requirements/dev.txt

# 安裝開發工具
RUN pip install pytest pytest-cov black flake8 mypy

# Codespaces 特定的預安裝
RUN if [ "$PREBUILD" = "true" ]; then \
    echo "🔨 Running prebuild optimizations..." && \
    pip install ipython jupyter && \
    echo "✅ Prebuild optimizations completed"; \
    fi

# 複製源代碼
COPY . .

# 暴露端口
EXPOSE 8000

# 開發模式啟動命令
CMD ["python", "run.py"]

# 生產階段
FROM base as production

# 創建非 root 用戶
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 複製依賴文件
COPY requirements.txt .

# 安裝生產依賴
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

# 複製源代碼
COPY --chown=appuser:appuser . .

# 切換到非 root 用戶
USER appuser

# 暴露端口
EXPOSE 8000

# 健康檢查
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/stats/health || exit 1

# 生產模式啟動命令
CMD ["gunicorn", "src.app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]