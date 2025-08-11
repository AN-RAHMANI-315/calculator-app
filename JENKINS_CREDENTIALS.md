## Jenkins Credentials Setup Guide

### 1. GitHub Access Token
**Type**: Secret text
**ID**: `github-token`
**Description**: GitHub Personal Access Token
**Secret**: [Your GitHub token]

**To create GitHub token**:
1. Go to GitHub.com → Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` and `admin:repo_hook` permissions
3. Copy the token and paste in Jenkins

### 2. Docker Hub Credentials (Optional)
**Type**: Username with password
**ID**: `docker-hub-creds`
**Username**: [Your Docker Hub username]
**Password**: [Your Docker Hub password]

### 3. Slack Integration (Optional)
**Type**: Secret text
**ID**: `slack-token`
**Description**: Slack Webhook URL
**Secret**: [Your Slack webhook URL]

**To get Slack webhook**:
1. Go to your Slack workspace
2. Apps → Add apps → Jenkins CI
3. Copy webhook URL

### 4. Email Configuration (Optional)
**Type**: Username with password
**ID**: `email-creds`
**Username**: [Your email]
**Password**: [Your email app password]

## Adding Credentials in Jenkins:
1. Manage Jenkins → Manage Credentials
2. Click on "System" → "Global credentials (unrestricted)"
3. Click "Add Credentials"
4. Select appropriate type
5. Fill in the details
6. Click "OK"
