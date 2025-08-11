# Docker Hub Integration for Jenkins Pipeline

## 🐳 **Docker Hub Setup for anrahmani007**

Your Docker Hub account: `https://hub.docker.com/repositories/anrahmani007`

### **1. Docker Hub Credentials in Jenkins**

Add these credentials in Jenkins:

**Type**: Username with password
**ID**: `docker-hub-creds`
**Username**: `anrahmani007`
**Password**: [Your Docker Hub password or access token]
**Description**: Docker Hub credentials for anrahmani007

### **2. Create Docker Hub Access Token (Recommended)**

1. Go to Docker Hub → Account Settings → Security
2. Click "New Access Token"
3. Name: `jenkins-calculator-app`
4. Permissions: Read, Write, Delete
5. Copy the token and use it as password in Jenkins

### **3. Build and Push Commands**

Manual build and push:
```bash
# Build the image
docker build -t anrahmani007/calculator-app:v1.0.0 -f docker/Dockerfile .

# Tag for latest
docker tag anrahmani007/calculator-app:v1.0.0 anrahmani007/calculator-app:latest

# Push to Docker Hub
docker push anrahmani007/calculator-app:v1.0.0
docker push anrahmani007/calculator-app:latest
```

### **4. Test Docker Image**

Pull and run your image:
```bash
# Pull from Docker Hub
docker pull anrahmani007/calculator-app:latest

# Run locally
docker run -d \
  --name calculator-test \
  -p 5000:5000 \
  -e FLASK_ENV=development \
  anrahmani007/calculator-app:latest

# Test the application
curl http://localhost:5000/health

# View logs
docker logs calculator-test

# Stop and remove
docker stop calculator-test && docker rm calculator-test
```

### **5. Updated Pipeline Features**

The Jenkins pipeline now:
- ✅ Builds images with your Docker Hub namespace
- ✅ Pushes to `anrahmani007/calculator-app`
- ✅ Tags images with build numbers and `latest`
- ✅ Uses stable tags for main branch
- ✅ Pulls images during deployment if not local

### **6. Image Tagging Strategy**

| Build Type | Tags Created |
|------------|--------------|
| Feature Branch | `anrahmani007/calculator-app:feature-123` |
| Develop Branch | `anrahmani007/calculator-app:develop-123` |
| Main Branch | `anrahmani007/calculator-app:123`, `latest`, `stable` |
| Release | `anrahmani007/calculator-app:v1.0.0`, `latest` |

### **7. Deployment Commands**

The deployment script now automatically:
```bash
# Pulls image if not available locally
docker pull anrahmani007/calculator-app:v1.0.0

# Runs with your image
docker run -d \
  --name calculator-app-dev \
  -p 5000:5000 \
  anrahmani007/calculator-app:v1.0.0
```

### **8. Docker Compose Usage**

Updated docker-compose.yml uses your image:
```yaml
services:
  calculator-app:
    image: anrahmani007/calculator-app:latest
    # ... rest of configuration
```

Run with:
```bash
cd docker/
docker-compose up -d
```

### **9. Security Best Practices**

1. **Use Access Tokens**: More secure than passwords
2. **Limit Token Scope**: Only give necessary permissions
3. **Rotate Tokens**: Change tokens periodically
4. **Monitor Usage**: Check Docker Hub for pull statistics

### **10. Troubleshooting**

#### Issue: "Authentication required"
```bash
# Login to Docker Hub
docker login
# Enter username: anrahmani007
# Enter password: [your-token]
```

#### Issue: "Image not found"
```bash
# Check if image exists
docker search anrahmani007/calculator-app

# List your images
docker images anrahmani007/calculator-app
```

#### Issue: "Push denied"
```bash
# Check you're logged in
docker info | grep Username

# Verify repository name
docker images | grep anrahmani007
```

### **11. Monitoring Your Images**

Track your Docker Hub usage:
- **Repository**: https://hub.docker.com/r/anrahmani007/calculator-app
- **Pull Statistics**: Monitor download counts
- **Vulnerability Scanning**: Enable Docker Hub security scanning
- **Webhooks**: Set up notifications for pushes

### **12. Next Steps**

1. **Set up Jenkins credentials** for Docker Hub
2. **Test manual build and push** to verify access
3. **Run Jenkins pipeline** to automate the process
4. **Monitor Docker Hub** for successful pushes
5. **Set up notifications** for failed builds

Your Docker Hub integration is now ready for enterprise CI/CD! 🚀
