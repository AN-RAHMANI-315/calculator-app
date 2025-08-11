# 🚀 Complete Jenkins Setup Guide

## ✅ **Your Jenkins Installation is Ready!**

### **Step 1: Access Jenkins**
- **URL**: http://localhost:8080
- **Initial Admin Password**: `b2a8b9c63a914fd991039fcac2ee54ac`

### **Step 2: Complete Initial Setup**
1. Open http://localhost:8080 in your browser
2. Enter the password: `b2a8b9c63a914fd991039fcac2ee54ac`
3. Click "Install suggested plugins" 
4. Create your admin user account
5. Keep Jenkins URL as http://localhost:8080
6. Click "Start using Jenkins"

### **Step 3: Install Required Plugins**
Go to "Manage Jenkins" → "Manage Plugins" → "Available" and install:
- [ ] **Pipeline** (should already be installed)
- [ ] **Git** (should already be installed) 
- [ ] **Docker Pipeline** (if you want Docker support)
- [ ] **Blue Ocean** (for better pipeline visualization)

### **Step 4: Configure Docker Hub Credentials**
1. Go to "Manage Jenkins" → "Manage Credentials"
2. Click "System" → "Global credentials"
3. Click "Add Credentials"
4. Fill in:
   - **Kind**: Username with password
   - **Scope**: Global
   - **Username**: `anrahmani007`
   - **Password**: [Your Docker Hub password or access token]
   - **ID**: `docker-hub-creds`
   - **Description**: Docker Hub credentials for anrahmani007

### **Step 5: Create Your First Pipeline**
1. Click "New Item" on Jenkins dashboard
2. Enter name: `calculator-app-pipeline`
3. Select "Pipeline" and click OK
4. In the configuration:
   - **Pipeline Definition**: Pipeline script from SCM
   - **SCM**: Git
   - **Repository URL**: [Your Git repository URL]
   - **Script Path**: `jenkins/Jenkinsfile`
5. Click "Save"

### **Step 6: Test Your Pipeline**
1. Click "Build Now" on your pipeline
2. Watch the build progress in "Console Output"
3. The pipeline will:
   - ✅ Clone your repository
   - ✅ Install dependencies
   - ✅ Run code quality checks
   - ✅ Execute 56 unit tests
   - ✅ Build Docker image
   - ✅ Push to anrahmani007/calculator-app

## 🐳 **Docker Hub Integration**

### **Create Docker Hub Access Token (Recommended)**
1. Go to https://hub.docker.com/settings/security
2. Click "New Access Token"
3. Name: `jenkins-calculator-app`
4. Permissions: Read, Write, Delete
5. Copy the token and use it as password in Jenkins credentials

### **Your Docker Images Will Be:**
- `anrahmani007/calculator-app:latest`
- `anrahmani007/calculator-app:v1.0.0` (tagged builds)
- `anrahmani007/calculator-app:build-123` (build numbers)

## 🔧 **Quick Commands for You**

### **Check Jenkins Status**
```bash
brew services list | grep jenkins
```

### **Restart Jenkins**
```bash
brew services restart jenkins-lts
```

### **Stop Jenkins**
```bash
brew services stop jenkins-lts
```

### **View Jenkins Logs**
```bash
tail -f ~/.jenkins/logs/jenkins.log
```

### **Test Your Calculator App Locally**
```bash
# Run tests
cd /Users/abdulnaseebrahmani/calculator-app
python -m pytest tests/ -v

# Build Docker image
docker build -t anrahmani007/calculator-app:test -f docker/Dockerfile .

# Run the app
docker run -p 5000:5000 anrahmani007/calculator-app:test
```

## 🎯 **What Happens in Your Pipeline**

1. **Checkout**: Gets code from your repository
2. **Setup**: Prepares Python environment
3. **Install**: Installs dependencies from requirements.txt
4. **Quality**: Runs flake8 (linting), black (formatting), bandit (security)
5. **Test**: Executes 56 unit tests with coverage
6. **Build**: Creates Docker image with your namespace
7. **Push**: Uploads to Docker Hub (anrahmani007/calculator-app)
8. **Deploy**: Can deploy to dev/staging/production

## 🚨 **Troubleshooting**

### **If Jenkins won't start:**
```bash
brew services restart jenkins-lts
```

### **If password doesn't work:**
```bash
cat ~/.jenkins/secrets/initialAdminPassword
```

### **If Docker push fails:**
- Check Docker Hub credentials in Jenkins
- Verify Docker is running: `docker version`
- Test manual login: `docker login`

### **If tests fail:**
- Check Python version: `python3 --version`
- Install dependencies: `pip install -r requirements.txt`
- Run tests manually: `python -m pytest tests/ -v`

## 🎉 **Success Indicators**

You'll know everything is working when:
- ✅ Jenkins dashboard loads at http://localhost:8080
- ✅ Pipeline runs without errors
- ✅ All 56 tests pass
- ✅ Docker image appears in your Docker Hub repository
- ✅ Build artifacts are created

## 📞 **Next Steps**

1. **Complete Jenkins setup** using the password above
2. **Add Docker Hub credentials** 
3. **Create your pipeline** using the calculator app repository
4. **Run your first build**
5. **Monitor the results** and check Docker Hub

Your enterprise-grade CI/CD pipeline is ready! 🚀
