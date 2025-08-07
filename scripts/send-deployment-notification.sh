#!/bin/bash

# 🔔 部署通知腳本
# 
# 此腳本用於發送 Codespaces 部署完成的通知

set -e

# 顏色輸出
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 配置
REPO_URL="${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}"
CODESPACES_URL="${REPO_URL}/codespaces"
ACTIONS_URL="${REPO_URL}/actions"

# 日誌函數
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# 創建通知內容
create_notification_content() {
    cat << EOF
🚀 **FastAPI Codespaces 部署完成！**

📦 **部署信息**:
- 鏡像: ${REGISTRY}/${IMAGE_NAME}:latest
- 時間: $(date -u '+%Y-%m-%d %H:%M:%S UTC')
- Commit: ${GITHUB_SHA:0:7}
- 分支: ${GITHUB_REF_NAME}

🎯 **快速開始**:
1. 前往 Codespaces: ${CODESPACES_URL}
2. 創建新的 Codespace 或重啟現有的
3. 運行 \`just codespaces-start\` 啟動應用
4. 訪問 API 文檔: https://\${CODESPACE_NAME}-8000.app.github.dev/docs

🔗 **相關連結**:
- 部署狀態: ${ACTIONS_URL}
- Container Registry: ${REPO_URL}/pkgs/container/${GITHUB_REPOSITORY##*/}

✅ 你的開發環境已準備就緒！
EOF
}

# 發送到 GitHub Issue（可選）
send_github_issue_notification() {
    if [ -n "$GITHUB_TOKEN" ] && [ "$CREATE_ISSUE_NOTIFICATION" = "true" ]; then
        log_info "創建 GitHub Issue 通知..."
        
        local issue_body
        issue_body=$(create_notification_content)
        
        # 使用 GitHub CLI 創建 issue（如果可用）
        if command -v gh >/dev/null 2>&1; then
            gh issue create \
                --title "🚀 Codespaces 部署完成 - $(date '+%Y-%m-%d %H:%M')" \
                --body "$issue_body" \
                --label "deployment,codespaces" \
                --assignee "@me" || log_info "無法創建 Issue（可能是權限問題）"
        fi
    fi
}

# 發送到 Slack（可選）
send_slack_notification() {
    if [ -n "$SLACK_WEBHOOK_URL" ]; then
        log_info "發送 Slack 通知..."
        
        local slack_payload
        slack_payload=$(cat << EOF
{
    "text": "🚀 FastAPI Codespaces 部署完成！",
    "blocks": [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🚀 Codespaces 部署完成"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*鏡像:*\n\`${REGISTRY}/${IMAGE_NAME}:latest\`"
                },
                {
                    "type": "mrkdwn",
                    "text": "*分支:*\n\`${GITHUB_REF_NAME}\`"
                },
                {
                    "type": "mrkdwn",
                    "text": "*Commit:*\n\`${GITHUB_SHA:0:7}\`"
                },
                {
                    "type": "mrkdwn",
                    "text": "*時間:*\n$(date -u '+%Y-%m-%d %H:%M:%S UTC')"
                }
            ]
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "打開 Codespaces"
                    },
                    "url": "${CODESPACES_URL}"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "查看部署"
                    },
                    "url": "${ACTIONS_URL}"
                }
            ]
        }
    ]
}
EOF
)
        
        curl -X POST -H 'Content-type: application/json' \
            --data "$slack_payload" \
            "$SLACK_WEBHOOK_URL" || log_info "Slack 通知發送失敗"
    fi
}

# 發送到 Discord（可選）
send_discord_notification() {
    if [ -n "$DISCORD_WEBHOOK_URL" ]; then
        log_info "發送 Discord 通知..."
        
        local discord_payload
        discord_payload=$(cat << EOF
{
    "embeds": [
        {
            "title": "🚀 Codespaces 部署完成",
            "description": "FastAPI 開發環境已準備就緒！",
            "color": 5763719,
            "fields": [
                {
                    "name": "📦 鏡像",
                    "value": "\`${REGISTRY}/${IMAGE_NAME}:latest\`",
                    "inline": true
                },
                {
                    "name": "🌿 分支",
                    "value": "\`${GITHUB_REF_NAME}\`",
                    "inline": true
                },
                {
                    "name": "📝 Commit",
                    "value": "\`${GITHUB_SHA:0:7}\`",
                    "inline": true
                }
            ],
            "footer": {
                "text": "GitHub Actions"
            },
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)"
        }
    ]
}
EOF
)
        
        curl -X POST -H 'Content-type: application/json' \
            --data "$discord_payload" \
            "$DISCORD_WEBHOOK_URL" || log_info "Discord 通知發送失敗"
    fi
}

# 創建本地通知文件
create_local_notification() {
    log_info "創建本地通知文件..."
    
    local notification_file="deployment-notification-$(date +%Y%m%d-%H%M%S).md"
    
    {
        echo "# 🚀 Codespaces 部署通知"
        echo ""
        create_notification_content
        echo ""
        echo "---"
        echo "生成時間: $(date)"
        echo "工作流程: ${GITHUB_RUN_ID}"
    } > "$notification_file"
    
    log_success "通知文件已創建: $notification_file"
}

# 主函數
main() {
    log_info "🔔 開始發送部署通知..."
    
    # 顯示基本信息
    log_info "部署信息："
    echo "  鏡像: ${REGISTRY}/${IMAGE_NAME}:latest"
    echo "  分支: ${GITHUB_REF_NAME}"
    echo "  Commit: ${GITHUB_SHA:0:7}"
    echo "  時間: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
    
    # 發送各種通知
    send_github_issue_notification
    send_slack_notification
    send_discord_notification
    create_local_notification
    
    log_success "🎉 通知發送完成！"
    
    echo ""
    echo "📋 你可以在以下位置查看部署狀態："
    echo "  - GitHub Actions: ${ACTIONS_URL}"
    echo "  - Codespaces: ${CODESPACES_URL}"
    echo "  - Container Registry: ${REPO_URL}/pkgs/container/${GITHUB_REPOSITORY##*/}"
}

# 執行主函數
main "$@"