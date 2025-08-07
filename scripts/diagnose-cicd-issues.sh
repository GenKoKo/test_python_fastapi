#!/bin/bash

# 🔍 CI/CD 問題診斷腳本
# 
# 此腳本用於診斷 CI/CD 流程中的常見問題

set -e

# 顏色輸出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日誌函數
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 檢查 CI/CD 配置文件
check_workflow_files() {
    log_info "🔍 檢查 CI/CD 工作流程文件..."
    
    local files=(
        ".github/workflows/ci.yml"
        ".github/workflows/cd-codespaces.yml"
        ".github/workflows/feature-ci.yml"
    )
    
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            log_success "✅ $file 存在"
            
            # 檢查語法錯誤
            if python -c "import yaml; yaml.safe_load(open('$file'))" 2>/dev/null; then
                log_success "✅ $file YAML 語法正確"
            else
                log_error "❌ $file YAML 語法錯誤"
            fi
        else
            log_error "❌ $file 不存在"
        fi
    done
}

# 檢查權限配置
check_permissions() {
    log_info "🔍 檢查權限配置..."
    
    # 檢查 security scan 權限
    if grep -q "security-events: write" .github/workflows/ci.yml; then
        log_success "✅ Security Scan 權限配置正確"
    else
        log_warning "⚠️ Security Scan 可能缺少權限配置"
    fi
    
    # 檢查 build-and-push 權限
    if grep -q "packages: write" .github/workflows/ci.yml; then
        log_success "✅ Build & Push 權限配置正確"
    else
        log_warning "⚠️ Build & Push 可能缺少權限配置"
    fi
}

# 檢查腳本語法
check_script_syntax() {
    log_info "🔍 檢查腳本語法..."
    
    # 檢查 CI 工作流程中的 shell 腳本
    if grep -q "console.log" .github/workflows/ci.yml; then
        log_error "❌ CI 工作流程中發現 JavaScript 代碼在 shell 腳本中"
    else
        log_success "✅ CI 工作流程腳本語法正確"
    fi
    
    # 檢查 CD 工作流程中的 shell 腳本
    if grep -q "console.log" .github/workflows/cd-codespaces.yml; then
        log_error "❌ CD 工作流程中發現 JavaScript 代碼在 shell 腳本中"
    else
        log_success "✅ CD 工作流程腳本語法正確"
    fi
}

# 檢查環境變數
check_environment_variables() {
    log_info "🔍 檢查環境變數配置..."
    
    # 檢查必要的環境變數
    local env_vars=("REGISTRY" "IMAGE_NAME")
    
    for var in "${env_vars[@]}"; do
        if grep -q "$var:" .github/workflows/ci.yml; then
            log_success "✅ 環境變數 $var 已配置"
        else
            log_warning "⚠️ 環境變數 $var 可能未配置"
        fi
    done
}

# 檢查 Docker 配置
check_docker_config() {
    log_info "🔍 檢查 Docker 配置..."
    
    if [ -f "Dockerfile" ]; then
        log_success "✅ Dockerfile 存在"
        
        # 檢查多階段構建
        if grep -q "FROM.*as.*development" Dockerfile; then
            log_success "✅ Dockerfile 包含開發階段"
        else
            log_warning "⚠️ Dockerfile 可能缺少開發階段"
        fi
        
        if grep -q "FROM.*as.*production" Dockerfile; then
            log_success "✅ Dockerfile 包含生產階段"
        else
            log_warning "⚠️ Dockerfile 可能缺少生產階段"
        fi
    else
        log_error "❌ Dockerfile 不存在"
    fi
    
    if [ -f "docker/docker-compose.yml" ]; then
        log_success "✅ Docker Compose 配置存在"
    else
        log_warning "⚠️ Docker Compose 配置不存在"
    fi
}

# 檢查 Codespaces 配置
check_codespaces_config() {
    log_info "🔍 檢查 Codespaces 配置..."
    
    if [ -f ".devcontainer/devcontainer.json" ]; then
        log_success "✅ Devcontainer 配置存在"
        
        # 檢查 JSON 語法
        if python -c "import json; json.load(open('.devcontainer/devcontainer.json'))" 2>/dev/null; then
            log_success "✅ Devcontainer JSON 語法正確"
        else
            log_error "❌ Devcontainer JSON 語法錯誤"
        fi
    else
        log_warning "⚠️ Devcontainer 配置不存在"
    fi
}

# 檢查常見問題
check_common_issues() {
    log_info "🔍 檢查常見問題..."
    
    # 檢查是否有混合的引號
    if grep -r "'" .github/workflows/ | grep -q '"'; then
        log_warning "⚠️ 工作流程文件中可能有混合的引號"
    fi
    
    # 檢查是否有未閉合的括號
    if ! python -c "
import re
import glob
for file in glob.glob('.github/workflows/*.yml'):
    with open(file) as f:
        content = f.read()
        if content.count('{{') != content.count('}}'):
            print(f'Unmatched braces in {file}')
            exit(1)
" 2>/dev/null; then
        log_warning "⚠️ 工作流程文件中可能有未匹配的大括號"
    fi
}

# 生成修復建議
generate_fix_suggestions() {
    log_info "💡 生成修復建議..."
    
    echo ""
    echo "🔧 常見問題修復建議："
    echo ""
    echo "1. 權限問題："
    echo "   - 確保 Security Scan 有 'security-events: write' 權限"
    echo "   - 確保 Build & Push 有 'packages: write' 權限"
    echo ""
    echo "2. 語法錯誤："
    echo "   - 檢查 shell 腳本中是否有 JavaScript 代碼"
    echo "   - 確保 YAML 縮進正確"
    echo "   - 檢查引號匹配"
    echo ""
    echo "3. 容錯性："
    echo "   - 在可能失敗的步驟添加 'continue-on-error: true'"
    echo "   - 使用 'if: always()' 確保清理步驟執行"
    echo ""
    echo "4. 測試建議："
    echo "   - 運行 'just test-deployment-fix' 測試修復"
    echo "   - 檢查 GitHub Actions 日誌獲取詳細錯誤信息"
    echo ""
}

# 主函數
main() {
    log_info "🚀 開始 CI/CD 問題診斷..."
    echo ""
    
    check_workflow_files
    echo ""
    
    check_permissions
    echo ""
    
    check_script_syntax
    echo ""
    
    check_environment_variables
    echo ""
    
    check_docker_config
    echo ""
    
    check_codespaces_config
    echo ""
    
    check_common_issues
    echo ""
    
    generate_fix_suggestions
    
    log_success "🎉 診斷完成！"
}

# 執行主函數
main "$@"