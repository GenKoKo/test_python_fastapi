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

# 安裝系統依賴（包含 Codespaces 必需的基本工具）
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    bash \
    coreutils \
    procps \
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
        zsh \
        vim \
        nano \
        htop \
        tree \
        jq \
        sudo \
        && rm -rf /var/lib/apt/lists/*; \
    fi

# 安裝 Just 命令工具（總是安裝，不僅限於 Codespaces）
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin

# 創建 vscode 用戶（Codespaces 需要）
RUN if [ "$CODESPACES" = "true" ]; then \
    groupadd -r vscode && \
    useradd -r -g vscode -m -s /bin/bash vscode && \
    echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers; \
    fi

# 安裝 uv
RUN pip install uv

# 首先複製依賴文件
COPY pyproject.toml uv.lock ./
COPY requirements/ requirements/

# 複製 README.md（pyproject.toml 中引用）
COPY README.md ./

# 創建 src 目錄並複製源代碼（setuptools 需要）
RUN mkdir -p src
COPY src/ src/

# 安裝 Python 依賴（包括開發依賴）
# 現在 setuptools 可以找到 src 目錄和 README.md
RUN uv sync --dev

# 複製其餘文件（如果需要）
COPY tests/ tests/
COPY scripts/ scripts/
COPY docs/ docs/

# 設置 Codespaces 權限
RUN if [ "$CODESPACES" = "true" ]; then \
    chown -R vscode:vscode /app && \
    mkdir -p /workspaces && \
    chown -R vscode:vscode /workspaces; \
    fi

# Codespaces 特定的預安裝
RUN if [ "$PREBUILD" = "true" ]; then \
    echo "🔨 Running prebuild optimizations..." && \
    uv add --dev ipython jupyter && \
    echo "✅ Prebuild optimizations completed"; \
    fi

# 暴露端口
EXPOSE 8000

# 開發模式啟動命令
CMD ["uv", "run", "python", "run.py"]

# 生產階段
FROM base as production

# 創建非 root 用戶
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 安裝 uv
RUN pip install uv

# 複製依賴文件和基本專案結構
COPY --chown=appuser:appuser pyproject.toml uv.lock ./
COPY --chown=appuser:appuser requirements/ requirements/
COPY --chown=appuser:appuser README.md ./

# 創建 src 目錄並複製源代碼
RUN mkdir -p src
COPY --chown=appuser:appuser src/ src/

# 安裝生產依賴
RUN uv sync --no-dev

# 複製其餘文件
COPY --chown=appuser:appuser . .

# 切換到非 root 用戶
USER appuser

# 暴露端口
EXPOSE 8000

# 健康檢查
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/stats/health || exit 1

# 生產模式啟動命令
CMD ["uv", "run", "gunicorn", "src.app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]