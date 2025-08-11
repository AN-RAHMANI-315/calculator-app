# Jenkins CI/CD Pipeline Tutorial for Python Calculator App

## Table of Contents
1. [Pipeline Overview](#pipeline-overview)
2. [Jenkins Setup](#jenkins-setup)
3. [Pipeline Stages Explained](#pipeline-stages-explained)
4. [DevOps Best Practices](#devops-best-practices)
5. [Quality Gates](#quality-gates)
6. [Deployment Strategies](#deployment-strategies)
7. [Monitoring and Alerts](#monitoring-and-alerts)
8. [Troubleshooting](#troubleshooting)

## Pipeline Overview

Our Jenkins pipeline implements a comprehensive CI/CD workflow with the following key features:

### 🏗️ **Multi-Environment Support**
- **Development**: Fast feedback loop with auto-formatting
- **Staging**: Full testing with blue-green deployment simulation
- **Production**: Comprehensive quality gates with rollback capabilities

### 🔍 **Quality Assurance**
- **Code Quality**: Linting (Flake8), formatting (Black)
- **Security**: Vulnerability scanning (Bandit, Safety)
- **Testing**: Unit, integration, and performance tests
- **Coverage**: Code coverage analysis with threshold enforcement

### 🚀 **Deployment Automation**
- **Containerized**: Docker-based deployments
- **Multi-environment**: Automated deployment to dev/staging/production
- **Blue-Green**: Zero-downtime production deployments
- **Rollback**: Automatic rollback on failure

## Jenkins Setup

### 1. Jenkins Installation

```bash
# Install Jenkins using Docker (recommended)
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts

# Get initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### 2. Required Jenkins Plugins

Install these plugins through Jenkins Plugin Manager:

```
Pipeline plugins:
- Pipeline: Stage View
- Pipeline: Groovy
- Blue Ocean (optional, for better UI)

SCM plugins:
- Git
- GitHub Integration

Build tools:
- Docker Pipeline
- Docker Commons

Testing & Quality:
- JUnit
- Coverage (Cobertura)
- HTML Publisher
- Test Results Analyzer

Notifications:
- Slack Notification
- Email Extension

Security:
- Credentials Binding
- Role-based Authorization Strategy
```

### 3. Global Tool Configuration

Configure these tools in Jenkins Global Tool Configuration:

```
Git: 
- Name: Default
- Path: git (or full path)

Docker:
- Name: docker
- Installation root: /usr/local/bin/docker

Python:
- Name: python3
- Installation root: /usr/bin/python3
```

### 4. Credentials Setup

Add these credentials in Jenkins Credentials Manager:

```
1. GitHub Token (for repository access)
   - Kind: Secret text
   - ID: github-token
   - Secret: <your-github-token>

2. Docker Hub Credentials (for image registry)
   - Kind: Username with password
   - ID: docker-hub-creds
   - Username: <docker-username>
   - Password: <docker-password>

3. Deployment SSH Keys (for server access)
   - Kind: SSH Username with private key
   - ID: deployment-ssh-key
   - Private Key: <your-private-key>

4. Production Secrets
   - Kind: Secret text
   - ID: production-secret-key
   - Secret: <production-secret>

5. Slack Token (for notifications)
   - Kind: Secret text
   - ID: slack-token
   - Secret: <slack-webhook-url>
```

## Pipeline Stages Explained

### Stage 1: Checkout & Setup
```groovy
stage('Checkout & Setup') {
    steps {
        // Clean workspace and checkout code
        deleteDir()
        checkout scm
        
        // Set build information
        currentBuild.displayName = "#${BUILD_NUMBER} - ${env.BRANCH_NAME}"
        
        // Create directory structure
        sh 'mkdir -p reports artifacts'
    }
}
```

**Purpose**: Prepare clean environment and download source code

**DevOps Best Practices**:
- Clean workspace prevents contamination between builds
- Consistent directory structure
- Build metadata for traceability

### Stage 2: Python Environment Setup
```groovy
stage('Python Environment Setup') {
    steps {
        sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements-dev.txt
        '''
    }
}
```

**Purpose**: Create isolated Python environment with dependencies

**DevOps Best Practices**:
- Virtual environments ensure consistency
- Dependency management with requirements files
- Reproducible builds across environments

### Stage 3: Code Quality Analysis (Parallel)
```groovy
stage('Code Quality Analysis') {
    parallel {
        stage('Linting (Flake8)') { /* ... */ }
        stage('Code Formatting (Black)') { /* ... */ }
        stage('Security Scanning (Bandit)') { /* ... */ }
        stage('Dependency Security (Safety)') { /* ... */ }
    }
}
```

**Purpose**: Ensure code quality and security standards

**DevOps Best Practices**:
- Parallel execution for faster feedback
- Multiple quality dimensions (style, security, dependencies)
- Fail fast approach - catch issues early

### Stage 4: Testing (Parallel)
```groovy
stage('Testing') {
    parallel {
        stage('Unit Tests') { /* pytest unit tests */ }
        stage('Integration Tests') { /* pytest integration tests */ }
        stage('Performance Tests') { /* pytest slow tests */ }
    }
}
```

**Purpose**: Validate functionality at multiple levels

**DevOps Best Practices**:
- Test pyramid: unit → integration → performance
- Parallel execution for efficiency
- Test coverage tracking and enforcement

### Stage 5: Build Application
```groovy
stage('Build Application') {
    steps {
        sh '''
            python setup.py sdist bdist_wheel
            docker build -t calculator-app:${BUILD_NUMBER} .
        '''
    }
}
```

**Purpose**: Create deployable artifacts

**DevOps Best Practices**:
- Immutable artifacts with version tags
- Container-based packaging
- Artifact archiving for traceability

### Stage 6: Quality Gates
```groovy
stage('Quality Gates') {
    steps {
        script {
            // Check coverage threshold
            // Verify security scan results
            // Validate test results
            if (!qualityPassed && !params.FORCE_DEPLOY) {
                error("Quality gates failed")
            }
        }
    }
}
```

**Purpose**: Automated go/no-go decision for deployment

**DevOps Best Practices**:
- Objective quality criteria
- Automatic enforcement with override option
- Clear failure feedback

### Stage 7: Deploy
```groovy
stage('Deploy') {
    when {
        anyOf {
            expression { params.DEPLOY_ENVIRONMENT != 'none' }
            expression { env.BRANCH_NAME == 'main' }
        }
    }
    steps {
        sh "./jenkins/deploy-scripts/deploy.sh ${targetEnv} ${version}"
    }
}
```

**Purpose**: Automated deployment to target environments

**DevOps Best Practices**:
- Environment-specific deployment logic
- Conditional deployment based on branch/parameters
- Standardized deployment scripts

## DevOps Best Practices Implemented

### 1. Infrastructure as Code
```groovy
// Pipeline configuration in version control
pipeline {
    agent any
    // All pipeline logic defined in code
}
```

### 2. Configuration Management
```bash
# Environment-specific configs in deploy-scripts/config/
dev.env
staging.env
production.env
```

### 3. Security Best Practices
```groovy
environment {
    // Sensitive data through environment variables
    SECRET_KEY = credentials('production-secret-key')
}
```

### 4. Monitoring and Observability
```groovy
post {
    always {
        // Archive artifacts
        archiveArtifacts artifacts: 'reports/**'
        
        // Publish test results
        publishTestResults testResultsPattern: 'reports/junit*.xml'
        
        // Coverage reporting
        publishCoverage adapters: [coberturaAdapter('reports/coverage.xml')]
    }
}
```

### 5. Automated Notifications
```groovy
post {
    failure {
        slackSend(
            channel: '#devops-alerts',
            color: 'danger',
            message: "Pipeline failed: ${env.JOB_NAME} #${BUILD_NUMBER}"
        )
    }
}
```

## Quality Gates

### 1. Code Coverage Threshold
```groovy
def coverage = sh(
    script: 'coverage report | grep TOTAL | awk \'{print $4}\' | sed \'s/%//\'',
    returnStdout: true
).trim() as Integer

if (coverage < 85) {
    currentBuild.result = 'UNSTABLE'
    error("Code coverage ${coverage}% below threshold 85%")
}
```

### 2. Security Scanning
```groovy
def banditOutput = readFile("reports/bandit-report.txt")
if (banditOutput.contains("SEVERITY: HIGH")) {
    error("High severity security issues found")
}
```

### 3. Test Results
```groovy
// Automatic test result publication
publishTestResults testResultsPattern: 'reports/junit*.xml'

// Fail build on test failures
if (currentBuild.result == 'UNSTABLE') {
    error("Tests failed")
}
```

## Deployment Strategies

### 1. Development Environment
```bash
# Fast deployment for rapid iteration
docker run -d \
  --name calculator-app-dev \
  -p 5000:5000 \
  -e FLASK_ENV=development \
  calculator-app:${VERSION}
```

### 2. Staging Environment
```bash
# Production-like environment with load balancer
docker-compose -f docker-compose.staging.yml up -d
```

### 3. Production Environment (Blue-Green)
```bash
# Deploy to green environment
docker run -d \
  --name calculator-app-prod-green \
  -p 5001:5000 \
  calculator-app:${VERSION}

# Health check new deployment
curl -f http://localhost:5001/health

# Switch traffic (update load balancer)
# Remove old blue deployment
```

## Monitoring and Alerts

### 1. Pipeline Metrics
- Build success/failure rates
- Build duration trends
- Test coverage over time
- Security vulnerability counts

### 2. Application Metrics
- Response times
- Error rates
- CPU/Memory usage
- Request volume

### 3. Alert Channels
```groovy
// Slack notifications
slackSend(
    channel: '#devops-alerts',
    message: "Deployment successful: ${env.JOB_NAME}"
)

// Email notifications
emailext(
    to: 'devops-team@company.com',
    subject: "Pipeline Status: ${env.JOB_NAME}",
    body: "Build ${BUILD_NUMBER} completed with status: ${currentBuild.result}"
)
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Python Virtual Environment Issues
```bash
# Error: ModuleNotFoundError
# Solution: Ensure virtual environment is activated
. venv/bin/activate
pip install -r requirements-dev.txt
```

#### 2. Docker Build Failures
```bash
# Error: Docker daemon not accessible
# Solution: Ensure Jenkins user has Docker permissions
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

#### 3. Test Failures
```bash
# Error: Import errors in tests
# Solution: Set PYTHONPATH correctly
export PYTHONPATH="${WORKSPACE}/src:${PYTHONPATH}"
```

#### 4. Deployment Failures
```bash
# Error: Permission denied during deployment
# Solution: Check SSH key permissions and sudo access
chmod 600 ~/.ssh/deployment_key
```

### Debug Commands

```bash
# Check Jenkins agent status
docker exec jenkins jenkins-cli list-computer

# View pipeline logs
curl -u admin:password http://localhost:8080/job/calculator-app/lastBuild/consoleText

# Check workspace contents
docker exec jenkins ls -la /var/jenkins_home/workspace/calculator-app

# Validate Jenkinsfile syntax
jenkins-cli declarative-linter < Jenkinsfile
```

### Performance Optimization

#### 1. Parallel Execution
```groovy
// Run independent stages in parallel
parallel {
    stage('Unit Tests') { /* ... */ }
    stage('Integration Tests') { /* ... */ }
    stage('Security Scan') { /* ... */ }
}
```

#### 2. Caching Strategies
```groovy
// Cache dependencies
sh '''
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        . venv/bin/activate
        pip install -r requirements-dev.txt
    fi
'''
```

#### 3. Workspace Management
```groovy
// Clean specific directories only
cleanWs(
    patterns: [
        [pattern: 'venv/', type: 'EXCLUDE'],
        [pattern: 'reports/', type: 'EXCLUDE']
    ]
)
```

## Next Steps

1. **Set up Jenkins**: Follow the installation and configuration steps
2. **Create Pipeline Job**: Use the provided Jenkinsfile
3. **Configure Webhooks**: Enable automatic builds on code changes
4. **Set up Environments**: Configure dev/staging/production environments
5. **Monitor and Iterate**: Continuously improve pipeline based on metrics

## Conclusion

This Jenkins pipeline demonstrates enterprise-grade DevOps practices including:

- ✅ **Automated Testing**: Comprehensive test coverage with multiple test types
- ✅ **Quality Gates**: Objective quality criteria enforcement
- ✅ **Security**: Vulnerability scanning and dependency checks
- ✅ **Multi-Environment**: Consistent deployment across environments
- ✅ **Monitoring**: Comprehensive logging and alerting
- ✅ **Rollback**: Automated rollback capabilities
- ✅ **Documentation**: Clear documentation and troubleshooting guides

The pipeline provides fast feedback for developers while ensuring production deployments meet quality and security standards.
