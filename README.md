# 🧮 Calculator App - Full-Stack DevOps Project

[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)](https://calculator-app-frontend.vercel.app)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)](https://hub.docker.com/r/anrahmani007/calculator-app)
[![CI/CD](https://img.shields.io/badge/Jenkins-Pipeline-orange?style=for-the-badge&logo=jenkins)](./jenkins/)

A **comprehensive calculator application** showcasing modern DevOps practices with multiple deployment options: frontend-only (Vercel), full-stack (Docker), and enterprise CI/CD (Jenkins).

## 🚀 Live Demo

🌐 **Frontend**: [calculator-app-frontend.vercel.app](https://calculator-app-frontend.vercel.app)  
🐳 **Docker**: `docker run -p 5001:5000 anrahmani007/calculator-app:latest`

## ✨ Features

### 🧮 Calculator Operations
- **Basic Math**: Addition, Subtraction, Multiplication, Division
- **Advanced Math**: Power, Square Root, Modulo, Percentage, Factorial
- **Error Handling**: Division by zero, negative square roots, large factorials
- **History Tracking**: Persistent calculation history

### 🎨 Multiple Interfaces
- **Web UI**: Modern responsive interface with gradient design
- **REST API**: JSON endpoints for programmatic access
- **CLI**: Command-line interface for terminal users

### 🛠️ DevOps Ready
- **Frontend Deployment**: Vercel-optimized static site
- **Container Deployment**: Docker with multi-stage builds
- **CI/CD Pipeline**: Jenkins automation with comprehensive testing
- **Monitoring**: Health checks and logging

## 📁 Project Architecture

```
calculator-app/
├── 🌐 public/                 # Frontend (Vercel deployment)
│   ├── index.html            # Client-side calculator
│   └── README.md             # Frontend documentation
├── 🐍 src/                   # Backend (Python/Flask)
│   ├── calculator.py         # Core calculation logic
│   ├── web_app.py           # Flask REST API
│   ├── cli.py               # Command-line interface
│   └── templates/           # Flask templates
├── 🧪 tests/                # Test suites
│   ├── test_calculator.py   # Unit tests (56 tests)
│   └── test_integration.py # Integration tests
├── 🐳 docker/               # Container configuration
│   ├── Dockerfile           # Multi-stage production build
│   └── docker-compose.yml   # Full-stack deployment
├── ⚙️ jenkins/              # CI/CD pipeline
│   ├── Jenkinsfile          # Production pipeline
│   ├── Jenkinsfile.dev      # Development pipeline
│   └── deploy-scripts/      # Deployment automation
├── 📋 package.json          # Node.js configuration
├── 🚀 vercel.json           # Vercel deployment config
└── 📚 Documentation/        # Comprehensive guides
```

## 🚀 Quick Start

### Option 1: Frontend Only (Vercel) ⚡

**Deploy to Vercel in 30 seconds:**

1. **Fork this repository**
2. **Connect to Vercel**: [vercel.com/new](https://vercel.com/new)
3. **Import your fork**
4. **Deploy automatically!**

```bash
# Local development
git clone https://github.com/AN-RAHMANI-315/calculator-app.git
cd calculator-app
python -m http.server 8000 --directory public
# Visit http://localhost:8000
```

### Option 2: Full-Stack (Docker) 🐳

```bash
# Quick start with Docker
docker run -d -p 5001:5000 --name calculator anrahmani007/calculator-app:latest

# Visit http://localhost:5001
```

```bash
# Development with Docker Compose
git clone https://github.com/AN-RAHMANI-315/calculator-app.git
cd calculator-app
docker-compose -f docker/docker-compose.yml up -d

# Includes: Calculator + Redis + Nginx + Monitoring
```

### Option 3: Local Development 🛠️

```bash
# Clone and setup
git clone https://github.com/AN-RAHMANI-315/calculator-app.git
cd calculator-app

# Python virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest --cov=src

# Start Flask app
python src/web_app.py
# Visit http://localhost:5000
```

## 🎯 Usage Examples

### 🌐 Web Interface
```javascript
// Modern calculator with beautiful UI
// ✅ Responsive design
// ✅ Real-time calculations  
// ✅ History persistence
// ✅ Error handling
```

### 🔌 REST API
```bash
# Addition
curl -X POST http://localhost:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "a": 15, "b": 25}'
# Response: {"result": 40.0, "history": ["15.0 + 25.0 = 40.0"]}

# Square root
curl -X POST http://localhost:5000/api/calculate-single \
  -H "Content-Type: application/json" \
  -d '{"operation": "sqrt", "value": 16}'
# Response: {"result": 4.0, "history": ["√16.0 = 4.0"]}
```

### 💻 Command Line
```bash
# Interactive mode
python src/cli.py

# Direct calculations
python src/cli.py add 10 5        # 15.0
python src/cli.py sqrt 25         # 5.0
python src/cli.py factorial 5     # 120
```

## 🧪 Testing & Quality

```bash
# Run full test suite (56 tests)
pytest --cov=src --cov-report=html

# Code quality checks
flake8 src/ tests/                # Style guide
black --check src/ tests/         # Code formatting
bandit -r src/                    # Security analysis

# Performance testing
python -m pytest tests/test_integration.py -v
```

**Test Coverage**: 98% | **Tests**: 56 passing | **Security**: Bandit approved

## 🔄 DevOps Pipeline

### Jenkins CI/CD ⚙️

```yaml
Pipeline Stages:
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│   Checkout  │ -> │  Install     │ -> │   Test      │ -> │   Deploy     │
│   Code      │    │  Dependencies│    │   & Lint    │    │   & Monitor  │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
```

**Features:**
- ✅ Automated testing on every commit
- ✅ Docker image building and pushing
- ✅ Multi-environment deployments
- ✅ Slack/Email notifications
- ✅ Security scanning

### Docker Deployment 🐳

```dockerfile
# Multi-stage optimized build
FROM python:3.9-slim as builder
# ... dependencies installation

FROM python:3.9-slim as production  
# ... production configuration
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1
```

**Container Features:**
- ⚡ Multi-stage builds for optimization
- 🔒 Non-root user security
- 📊 Health checks and monitoring
- 🔄 Rolling updates support

## 📊 Performance & Monitoring

| Metric | Value |
|--------|-------|
| **Load Time** | < 1s |
| **Memory Usage** | < 100MB |
| **Response Time** | < 50ms |
| **Uptime** | 99.9% |

**Monitoring Stack:**
- **Health Checks**: `/health` endpoint
- **Metrics**: Prometheus integration ready
- **Logs**: Structured JSON logging
- **Alerts**: Configurable thresholds

## 🌟 Technology Stack

### Frontend 🎨
- **HTML5**: Semantic markup
- **CSS3**: Modern gradients, animations
- **JavaScript ES6+**: Client-side logic
- **Local Storage**: History persistence

### Backend 🐍
- **Python 3.9+**: Core application
- **Flask**: Web framework
- **Gunicorn**: WSGI server
- **Click**: CLI framework

### DevOps 🛠️
- **Docker**: Containerization
- **Jenkins**: CI/CD automation
- **Vercel**: Frontend hosting
- **GitHub**: Version control

### Testing 🧪
- **pytest**: Testing framework
- **coverage**: Code coverage
- **flake8**: Style guide
- **bandit**: Security analysis

## 🚢 Deployment Options

| Platform | Use Case | Setup Time | Features |
|----------|----------|------------|----------|
| **Vercel** | Frontend showcase | 30 seconds | Auto-scaling, CDN, SSL |
| **Docker** | Full-stack development | 2 minutes | Complete environment |
| **Jenkins** | Enterprise CI/CD | 15 minutes | Full automation |

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-calculator`
3. **Make** your changes with tests
4. **Run** quality checks: `pytest && flake8`
5. **Submit** a pull request

### Development Guidelines
- ✅ Write tests for new features
- ✅ Follow PEP 8 style guide
- ✅ Update documentation
- ✅ Test in multiple environments

## 📝 Documentation

- 📖 [**Vercel Deployment Guide**](./VERCEL_SETUP.md)
- 🐳 [**Docker Desktop Guide**](./DOCKER_DESKTOP_GUIDE.md)
- ⚙️ [**Jenkins Pipeline Setup**](./JENKINS_GUIDE.md)
- 🛠️ [**Development Setup**](./DEVOPS_GUIDE.md)

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Abdul Naseer Ahmani**  
[![GitHub](https://img.shields.io/badge/GitHub-AN--RAHMANI--315-black?style=flat&logo=github)](https://github.com/AN-RAHMANI-315)
[![Email](https://img.shields.io/badge/Email-Contact-blue?style=flat&logo=gmail)](mailto:anrahmani315@gmail.com)

## 🌟 Show Your Support

If this project helped you learn DevOps concepts, please ⭐ star this repository!

---

### 🎯 Perfect for Learning

This project demonstrates:
- ✅ **Frontend Development**: Modern HTML/CSS/JS
- ✅ **Backend Development**: Python/Flask APIs
- ✅ **Testing**: Comprehensive test suites
- ✅ **Containerization**: Docker best practices
- ✅ **CI/CD**: Jenkins pipeline automation
- ✅ **Deployment**: Multiple hosting options
- ✅ **Documentation**: Production-ready docs

**Ready to deploy your calculator? Start with Vercel! 🚀**

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
