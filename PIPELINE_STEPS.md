# Step-by-Step Jenkins Pipeline Implementation

## Phase 1: Basic Setup ✅
- [x] Install Jenkins
- [x] Install required plugins
- [x] Configure credentials
- [x] Create simple pipeline job
- [x] Run first build

## Phase 2: Enhanced Pipeline (Next Steps)

### 1. Update Pipeline Configuration
- Change Script Path to: `jenkins/Jenkinsfile`
- This uses the full-featured pipeline we created

### 2. Add Quality Gates
The main Jenkinsfile includes:
- Code coverage analysis
- Security scanning
- Linting and formatting checks
- Multi-stage testing

### 3. Set Up Notifications
Configure Slack or email notifications:
```groovy
post {
    failure {
        slackSend(
            channel: '#alerts',
            color: 'danger',
            message: "Build failed: ${env.JOB_NAME} #${BUILD_NUMBER}"
        )
    }
}
```

### 4. Multi-Environment Deployment
- Development: Automatic deployment
- Staging: Manual approval required
- Production: Full quality gates + approval

### 5. Add Build Parameters
In Pipeline configuration, enable:
- "This project is parameterized"
- Add choice parameters for deployment environment
- Add boolean parameters for skipping tests

## Phase 3: Production Ready

### 1. Set Up Webhooks
In GitHub repository:
- Settings → Webhooks → Add webhook
- URL: `http://your-jenkins-url:8080/github-webhook/`
- Content type: `application/json`
- Events: Push events

### 2. Branch Strategy
- `main` → Production pipeline
- `develop` → Staging pipeline  
- `feature/*` → Development pipeline

### 3. Monitoring
- Set up build trend monitoring
- Configure email notifications for failures
- Add Slack integration for team updates

## Troubleshooting Common Issues

### Issue 1: Permission Denied
```bash
# Fix Jenkins user permissions
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

### Issue 2: Python Module Not Found
```groovy
environment {
    PYTHONPATH = "${WORKSPACE}/src:${PYTHONPATH}"
}
```

### Issue 3: Build Timeout
```groovy
options {
    timeout(time: 30, unit: 'MINUTES')
}
```

## Quick Commands Reference

### Jenkins CLI Commands
```bash
# Download Jenkins CLI
wget http://localhost:8080/jnlpJars/jenkins-cli.jar

# List jobs
java -jar jenkins-cli.jar -s http://localhost:8080 list-jobs

# Build job
java -jar jenkins-cli.jar -s http://localhost:8080 build calculator-app-pipeline

# Get build log
java -jar jenkins-cli.jar -s http://localhost:8080 console calculator-app-pipeline
```

### Docker Commands
```bash
# View Jenkins logs
docker logs jenkins-calculator

# Access Jenkins container
docker exec -it jenkins-calculator bash

# Backup Jenkins
docker exec jenkins-calculator tar czf - /var/jenkins_home > jenkins-backup.tar.gz
```
