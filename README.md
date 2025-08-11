# Calculator App with Jenkins CI/CD Pipeline

A comprehensive Python calculator application demonstrating DevOps best practices with Jenkins automation.

## Project Structure

```
calculator-app/
├── src/
│   ├── __init__.py
│   ├── calculator.py          # Core calculator logic
│   ├── cli.py                 # Command line interface
│   └── web_app.py            # Flask web interface
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py     # Unit tests
│   └── test_integration.py   # Integration tests
├── jenkins/
│   ├── Jenkinsfile           # Main pipeline
│   ├── Jenkinsfile.dev       # Development pipeline
│   └── deploy-scripts/       # Deployment automation
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── requirements.txt          # Python dependencies
├── requirements-dev.txt      # Development dependencies
├── setup.py                 # Package configuration
├── pytest.ini              # Test configuration
├── .flake8                  # Linting configuration
└── .gitignore
```

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Power, square root, percentage
- **Multiple Interfaces**: CLI and Web UI
- **Comprehensive Testing**: Unit and integration tests
- **CI/CD Pipeline**: Automated testing, building, and deployment
- **Code Quality**: Linting, formatting, and security scanning

## Jenkins Pipeline Stages

1. **Checkout**: Source code retrieval
2. **Environment Setup**: Python virtual environment
3. **Code Quality**: Linting and formatting checks
4. **Testing**: Unit and integration tests with coverage
5. **Security Scanning**: Vulnerability detection
6. **Build**: Package creation
7. **Deploy**: Environment-specific deployments

## Quick Start

### Local Development
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Start CLI calculator
python src/cli.py

# Start web application
python src/web_app.py
```

### Docker
```bash
# Build and run
docker-compose up --build
```

### Jenkins Setup
1. Create new Pipeline job
2. Point to this repository
3. Set Pipeline script path to `jenkins/Jenkinsfile`
4. Configure webhooks for automatic builds

## CI/CD Workflow

- **Feature branches** → Development environment
- **Release branches** → Staging environment  
- **Main branch** → Production environment (with approval)

## DevOps Best Practices Demonstrated

- Infrastructure as Code
- Automated testing and quality gates
- Multi-environment deployments
- Security scanning integration
- Artifact management
- Notification systems
- Rollback capabilities
