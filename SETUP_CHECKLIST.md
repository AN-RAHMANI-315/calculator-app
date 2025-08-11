# 🚀 Jenkins Pipeline Setup Checklist

## ✅ **Quick Start Checklist**

### Step 1: Jenkins Installation
- [ ] Install Jenkins (Docker/Homebrew/WAR file)
- [ ] Access Jenkins at http://localhost:8080
- [ ] Complete initial setup wizard
- [ ] Create admin user

### Step 2: Plugin Installation  
- [ ] Install Pipeline plugins
- [ ] Install Git plugin
- [ ] Install Docker plugins (if using Docker)
- [ ] Install testing plugins (JUnit, Coverage)
- [ ] Install notification plugins (Slack, Email)

### Step 3: Global Configuration
- [ ] Configure Git tool
- [ ] Configure Docker tool (if applicable)
- [ ] Set up email server (optional)

### Step 4: Credentials Setup
- [ ] Add GitHub token (if using GitHub)
- [ ] Add Docker Hub credentials (optional)
- [ ] Add Slack webhook (optional)
- [ ] Add email credentials (optional)

### Step 5: Create Pipeline Job
- [ ] New Item → Pipeline
- [ ] Name: `calculator-app-pipeline`
- [ ] Configure source (SCM or script)
- [ ] Set script path: `jenkins/Jenkinsfile.simple` (for testing)
- [ ] Save configuration

### Step 6: First Build
- [ ] Click "Build Now"
- [ ] Monitor build in console output
- [ ] Verify all stages complete successfully
- [ ] Check build artifacts

### Step 7: Advanced Setup (Optional)
- [ ] Switch to full Jenkinsfile
- [ ] Configure build triggers
- [ ] Set up webhooks
- [ ] Add build parameters
- [ ] Configure notifications

## 🎯 **What Happens During Build**

1. **Setup Stage**: Environment preparation
2. **Install Dependencies**: Python packages installation
3. **Code Quality**: Syntax and style checks
4. **Run Tests**: Execute test suite
5. **Build Info**: Display build summary

## 🐛 **Common Issues & Solutions**

### Issue: "python3 not found"
**Solution**: 
```bash
# In Jenkins job configuration, add build step:
which python3
# or use full path: /usr/bin/python3
```

### Issue: "Permission denied"
**Solution**: 
```bash
# Fix file permissions
chmod +x jenkins/deploy-scripts/deploy.sh
```

### Issue: "Module not found"
**Solution**: 
```groovy
// Add to pipeline environment
environment {
    PYTHONPATH = "${WORKSPACE}/src"
}
```

### Issue: "Docker not found"
**Solution**: 
- Ensure Docker is running
- Check Jenkins has Docker permissions
- Verify Docker plugin is installed

## 📊 **Expected Results**

After successful setup, you should see:
- ✅ Green build status
- ✅ All pipeline stages completed
- ✅ Test results published
- ✅ Build artifacts archived
- ✅ Console output showing progress

## 🔧 **Quick Commands**

### Start Jenkins (Docker)
```bash
docker run -d --name jenkins-calculator -p 8080:8080 jenkins/jenkins:lts
```

### View Jenkins Logs
```bash
docker logs jenkins-calculator
```

### Get Initial Password
```bash
docker exec jenkins-calculator cat /var/jenkins_home/secrets/initialAdminPassword
```

### Access Jenkins
```
URL: http://localhost:8080
```

## 🎉 **Success Criteria**

You'll know the setup is successful when:
1. Jenkins dashboard loads without errors
2. Pipeline job runs without failures
3. All stages show green checkmarks
4. Console output shows "Pipeline completed!"
5. Build history shows successful builds

## 📞 **Need Help?**

If you encounter issues:
1. Check the console output for error details
2. Verify all plugins are installed
3. Ensure credentials are configured correctly
4. Check file permissions in workspace
5. Review the troubleshooting section above

## 🚀 **Next Steps**

Once basic pipeline works:
1. Implement full CI/CD pipeline
2. Add deployment stages
3. Set up monitoring and alerts
4. Configure multi-environment deployments
5. Add security scanning

---

**You're ready to build enterprise-grade CI/CD pipelines! 🎊**
