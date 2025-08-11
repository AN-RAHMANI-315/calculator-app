# 🐳 Docker Desktop Setup Guide for Calculator App

## ✅ **Your Docker Image is Ready!**

### **Image Details:**
- **Name**: `anrahmani007/calculator-app:latest`
- **Status**: ✅ Built successfully
- **Size**: Optimized Python 3.9 slim base
- **Features**: Web API + CLI calculator

---

## 🚀 **Step-by-Step Guide to Run in Docker Desktop**

### **Step 1: Open Docker Desktop**
1. Open Docker Desktop application on your Mac
2. Make sure Docker is running (whale icon in menu bar)
3. Go to the "Images" tab in Docker Desktop

### **Step 2: Find Your Image**
1. Look for `anrahmani007/calculator-app:latest` in the Images list
2. You should see it with the "latest" tag
3. Click on the image to see details

### **Step 3: Run the Container (Method 1 - Docker Desktop UI)**
1. Click the "Run" button next to your image
2. In the "Run a new container" dialog:
   - **Container name**: `calculator-app`
   - **Host port**: `5000`
   - **Container port**: `5000`
   - Click "Run"

### **Step 4: Run the Container (Method 2 - Terminal)**
```bash
# Simple run
docker run -d --name calculator-app -p 5000:5000 anrahmani007/calculator-app:latest

# Run with environment variables
docker run -d \
  --name calculator-app \
  -p 5000:5000 \
  -e FLASK_ENV=development \
  anrahmani007/calculator-app:latest
```

### **Step 5: Test Your Running Container**

**1. Health Check:**
```bash
curl http://localhost:5000/health
```
**Expected Output:**
```json
{"service":"calculator-app","status":"healthy","version":"1.0.0"}
```

**2. Test Calculator API:**
```bash
# Addition
curl -X POST http://localhost:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "a": 10, "b": 5}'

# Multiplication  
curl -X POST http://localhost:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "multiply", "a": 7, "b": 6}'
```

**3. Open in Browser:**
- Go to: http://localhost:5000
- You should see the calculator web interface

---

## 🎛️ **Docker Desktop Operations**

### **View Running Containers:**
1. Go to "Containers" tab in Docker Desktop
2. You should see `calculator-app` running
3. Green status indicates it's healthy

### **View Container Logs:**
1. Click on your running container
2. Go to "Logs" tab
3. See real-time application logs

### **Container Actions:**
- **Stop**: Click the stop button
- **Restart**: Click restart button  
- **Delete**: Stop first, then delete
- **Terminal**: Click "Open in terminal" for bash access

---

## 🐳 **Using Docker Compose (Advanced)**

### **Start Full Stack:**
```bash
cd /Users/abdulnaseebrahmani/calculator-app/docker
docker-compose up -d
```

**This starts:**
- ✅ Calculator App (port 5000)
- ✅ Redis Cache (port 6379)
- ✅ Nginx Proxy (port 80)
- ✅ Prometheus Monitoring (port 9090)
- ✅ Grafana Dashboard (port 3000)

### **Stop Full Stack:**
```bash
docker-compose down
```

---

## 🧪 **Testing Commands**

### **Test All Calculator Operations:**
```bash
# Addition
curl -X POST http://localhost:5000/api/calculate -H "Content-Type: application/json" -d '{"operation": "add", "a": 10, "b": 5}'

# Subtraction
curl -X POST http://localhost:5000/api/calculate -H "Content-Type: application/json" -d '{"operation": "subtract", "a": 10, "b": 3}'

# Multiplication
curl -X POST http://localhost:5000/api/calculate -H "Content-Type: application/json" -d '{"operation": "multiply", "a": 4, "b": 7}'

# Division
curl -X POST http://localhost:5000/api/calculate -H "Content-Type: application/json" -d '{"operation": "divide", "a": 20, "b": 4}'

# Power
curl -X POST http://localhost:5000/api/calculate -H "Content-Type: application/json" -d '{"operation": "power", "a": 2, "b": 8}'

# Square Root
curl -X POST http://localhost:5000/api/calculate -H "Content-Type: application/json" -d '{"operation": "sqrt", "a": 25}'
```

### **Test CLI Interface:**
```bash
docker exec -it calculator-app python -c "from src.calculator import *; print(add(10, 5))"
```

---

## 🔧 **Troubleshooting**

### **Container Won't Start:**
1. Check Docker Desktop is running
2. Verify port 5000 isn't used: `lsof -i :5000`
3. Try different port: `-p 5001:5000`

### **Can't Access Web Interface:**
1. Verify container is running: `docker ps`
2. Check logs: `docker logs calculator-app`
3. Test health endpoint first

### **Image Not Found:**
1. Rebuild image: `docker build -t anrahmani007/calculator-app:latest .`
2. Check images: `docker images`

---

## 📊 **Docker Desktop Features to Use**

### **1. Resource Usage:**
- Monitor CPU and memory usage
- Set resource limits if needed

### **2. Volume Management:**
- Persistent data storage
- Log file access

### **3. Network Inspection:**
- View container networking
- Port mapping verification

### **4. Image Management:**
- Tag different versions
- Push to Docker Hub

---

## 🎯 **Quick Commands Reference**

```bash
# Build image
docker build -t anrahmani007/calculator-app:latest -f docker/Dockerfile .

# Run container
docker run -d --name calculator-app -p 5000:5000 anrahmani007/calculator-app:latest

# View running containers
docker ps

# View logs
docker logs calculator-app

# Stop container
docker stop calculator-app

# Remove container
docker rm calculator-app

# Access container shell
docker exec -it calculator-app bash

# Test health
curl http://localhost:5000/health
```

---

## 🚀 **You're Ready!**

Your calculator app is now:
- ✅ Containerized with Docker
- ✅ Running on port 5000
- ✅ Accessible via Web UI and API
- ✅ Ready for production deployment
- ✅ Integrated with your Docker Hub account

**Next Steps:**
1. Open http://localhost:5000 in your browser
2. Test the calculator functionality
3. Explore Docker Desktop features
4. Consider setting up Jenkins CI/CD pipeline

Your professional DevOps setup is complete! 🎉
