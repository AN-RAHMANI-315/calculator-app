#!/bin/bash

# Deployment script for Calculator App
# Usage: ./deploy.sh <environment> <version>

set -euo pipefail

# Script configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

# Default values
ENVIRONMENT="${1:-dev}"
VERSION="${2:-latest}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Validate environment
validate_environment() {
    case "$ENVIRONMENT" in
        dev|staging|production)
            log_info "Deploying to $ENVIRONMENT environment"
            ;;
        *)
            log_error "Invalid environment: $ENVIRONMENT"
            log_error "Valid environments: dev, staging, production"
            exit 1
            ;;
    esac
}

# Load environment-specific configuration
load_config() {
    local config_file="${SCRIPT_DIR}/config/${ENVIRONMENT}.env"
    
    if [[ -f "$config_file" ]]; then
        log_info "Loading configuration from $config_file"
        source "$config_file"
    else
        log_warning "No config file found for $ENVIRONMENT, using defaults"
        
        # Default configuration
        case "$ENVIRONMENT" in
            dev)
                export APP_PORT=5000
                export REPLICAS=1
                export MEMORY_LIMIT="512Mi"
                export CPU_LIMIT="500m"
                export DOMAIN="dev-calculator.company.com"
                ;;
            staging)
                export APP_PORT=5000
                export REPLICAS=2
                export MEMORY_LIMIT="1Gi"
                export CPU_LIMIT="1000m"
                export DOMAIN="staging-calculator.company.com"
                ;;
            production)
                export APP_PORT=5000
                export REPLICAS=3
                export MEMORY_LIMIT="2Gi"
                export CPU_LIMIT="2000m"
                export DOMAIN="calculator.company.com"
                ;;
        esac
    fi
}

# Pre-deployment checks
pre_deployment_checks() {
    log_info "Running pre-deployment checks..."
    
    # Check if Docker image exists
    if ! docker image inspect "anrahmani007/calculator-app:${VERSION}" >/dev/null 2>&1; then
        log_info "Docker image not found locally, pulling from registry..."
        docker pull "anrahmani007/calculator-app:${VERSION}" || {
            log_error "Docker image anrahmani007/calculator-app:${VERSION} not found in registry"
            exit 1
        }
    fi
    
    # Check deployment prerequisites
    case "$ENVIRONMENT" in
        production)
            # Additional checks for production
            if [[ "$VERSION" == "latest" ]]; then
                log_error "Cannot deploy 'latest' tag to production"
                exit 1
            fi
            
            # Check if this is a tagged release
            if ! git tag --contains HEAD >/dev/null 2>&1; then
                log_warning "Deploying untagged commit to production"
                read -p "Continue? (y/N): " -n 1 -r
                echo
                if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                    log_info "Deployment cancelled"
                    exit 0
                fi
            fi
            ;;
    esac
    
    log_success "Pre-deployment checks passed"
}

# Backup current deployment (for production)
backup_current_deployment() {
    if [[ "$ENVIRONMENT" == "production" ]]; then
        log_info "Creating backup of current production deployment..."
        
        # Create backup directory
        local backup_dir="/opt/backups/calculator-app/${TIMESTAMP}"
        sudo mkdir -p "$backup_dir"
        
        # Backup current application
        if docker ps | grep -q "calculator-app-prod"; then
            log_info "Backing up current production container..."
            docker commit calculator-app-prod "calculator-app:backup-${TIMESTAMP}"
            echo "calculator-app:backup-${TIMESTAMP}" > "${backup_dir}/image_tag.txt"
            
            # Export current configuration
            docker inspect calculator-app-prod > "${backup_dir}/container_config.json"
        fi
        
        log_success "Backup created at $backup_dir"
        export BACKUP_DIR="$backup_dir"
    fi
}

# Deploy to development environment
deploy_dev() {
    log_info "Deploying to development environment..."
    
    # Stop existing containers
    docker stop calculator-app-dev 2>/dev/null || true
    docker rm calculator-app-dev 2>/dev/null || true
    
    # Run new container
    docker run -d \
        --name calculator-app-dev \
        --restart unless-stopped \
        -p "${APP_PORT}:5000" \
        -e FLASK_ENV=development \
        -e SECRET_KEY=dev-secret-key \
        --memory="${MEMORY_LIMIT}" \
        --cpus="${CPU_LIMIT}" \
        "anrahmani007/calculator-app:${VERSION}"
    
    # Wait for application to start
    sleep 10
    
    # Health check
    if curl -f "http://localhost:${APP_PORT}/health" >/dev/null 2>&1; then
        log_success "Development deployment successful"
        log_info "Application available at: http://${DOMAIN}"
    else
        log_error "Health check failed"
        exit 1
    fi
}

# Deploy to staging environment
deploy_staging() {
    log_info "Deploying to staging environment..."
    
    # Use Docker Compose for staging
    cat > docker-compose.staging.yml << EOF
version: '3.8'
services:
  calculator-app:
    image: anrahmani007/calculator-app:${VERSION}
    container_name: calculator-app-staging
    restart: unless-stopped
    ports:
      - "${APP_PORT}:5000"
    environment:
      - FLASK_ENV=staging
      - SECRET_KEY=\${STAGING_SECRET_KEY}
    deploy:
      replicas: ${REPLICAS}
      resources:
        limits:
          memory: ${MEMORY_LIMIT}
          cpus: '${CPU_LIMIT}'
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  nginx:
    image: nginx:alpine
    container_name: calculator-nginx-staging
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.staging.conf:/etc/nginx/nginx.conf
    depends_on:
      - calculator-app
EOF

    # Create Nginx configuration
    cat > nginx.staging.conf << EOF
events {
    worker_connections 1024;
}

http {
    upstream calculator_app {
        server calculator-app:5000;
    }

    server {
        listen 80;
        server_name ${DOMAIN};

        location / {
            proxy_pass http://calculator_app;
            proxy_set_header Host \$host;
            proxy_set_header X-Real-IP \$remote_addr;
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto \$scheme;
        }

        location /health {
            proxy_pass http://calculator_app/health;
        }
    }
}
EOF

    # Deploy with Docker Compose
    export STAGING_SECRET_KEY="${STAGING_SECRET_KEY:-staging-secret-key}"
    docker-compose -f docker-compose.staging.yml down
    docker-compose -f docker-compose.staging.yml up -d
    
    # Wait for services to start
    sleep 20
    
    # Health check
    if curl -f "http://localhost/health" >/dev/null 2>&1; then
        log_success "Staging deployment successful"
        log_info "Application available at: http://${DOMAIN}"
    else
        log_error "Health check failed"
        exit 1
    fi
}

# Deploy to production environment
deploy_production() {
    log_info "Deploying to production environment..."
    
    # Production deployment using Kubernetes or Docker Swarm
    # This is a simplified version - in real production, you'd use K8s manifests
    
    # Blue-Green deployment simulation
    local current_color=$(docker ps --filter "name=calculator-app-prod" --format "{{.Names}}" | grep -o "blue\|green" || echo "blue")
    local new_color=$([ "$current_color" = "blue" ] && echo "green" || echo "blue")
    
    log_info "Current production color: $current_color"
    log_info "Deploying new color: $new_color"
    
    # Deploy new version
    docker run -d \
        --name "calculator-app-prod-${new_color}" \
        --restart unless-stopped \
        -p "$((APP_PORT + 1)):5000" \
        -e FLASK_ENV=production \
        -e SECRET_KEY="${PRODUCTION_SECRET_KEY}" \
        --memory="${MEMORY_LIMIT}" \
        --cpus="${CPU_LIMIT}" \
        "anrahmani007/calculator-app:${VERSION}"
    
    # Wait for new deployment to be healthy
    sleep 30
    
    # Health check on new deployment
    if curl -f "http://localhost:$((APP_PORT + 1))/health" >/dev/null 2>&1; then
        log_success "New deployment is healthy"
        
        # Switch traffic (update load balancer or proxy)
        log_info "Switching traffic to new deployment..."
        
        # Update main production container
        docker stop calculator-app-prod 2>/dev/null || true
        docker rm calculator-app-prod 2>/dev/null || true
        
        # Rename new container to production
        docker rename "calculator-app-prod-${new_color}" calculator-app-prod
        
        # Update port mapping (this would be handled by load balancer in real scenario)
        docker stop calculator-app-prod
        docker run -d \
            --name calculator-app-prod \
            --restart unless-stopped \
            -p "${APP_PORT}:5000" \
            -e FLASK_ENV=production \
            -e SECRET_KEY="${PRODUCTION_SECRET_KEY}" \
            --memory="${MEMORY_LIMIT}" \
            --cpus="${CPU_LIMIT}" \
            "anrahmani007/calculator-app:${VERSION}"
        
        # Clean up old deployment
        docker stop "calculator-app-prod-${current_color}" 2>/dev/null || true
        docker rm "calculator-app-prod-${current_color}" 2>/dev/null || true
        
        log_success "Production deployment successful"
        log_info "Application available at: https://${DOMAIN}"
        
    else
        log_error "New deployment health check failed, rolling back..."
        docker stop "calculator-app-prod-${new_color}"
        docker rm "calculator-app-prod-${new_color}"
        exit 1
    fi
}

# Post-deployment verification
post_deployment_verification() {
    log_info "Running post-deployment verification..."
    
    local base_url
    case "$ENVIRONMENT" in
        dev)
            base_url="http://localhost:${APP_PORT}"
            ;;
        staging)
            base_url="http://localhost"
            ;;
        production)
            base_url="http://localhost:${APP_PORT}"
            ;;
    esac
    
    # Test basic functionality
    log_info "Testing basic functionality..."
    
    # Health check
    if curl -f "${base_url}/health" >/dev/null 2>&1; then
        log_success "✓ Health check passed"
    else
        log_error "✗ Health check failed"
        return 1
    fi
    
    # Test API endpoints (if available)
    if curl -f "${base_url}/api/calculate" -X POST \
        -H "Content-Type: application/json" \
        -d '{"operation":"add","a":2,"b":3}' >/dev/null 2>&1; then
        log_success "✓ API functionality test passed"
    else
        log_warning "✗ API test failed (might not be implemented yet)"
    fi
    
    # Performance test
    log_info "Running basic performance test..."
    local response_time=$(curl -o /dev/null -s -w '%{time_total}' "${base_url}/health")
    if (( $(echo "$response_time < 1.0" | bc -l) )); then
        log_success "✓ Response time: ${response_time}s (good)"
    else
        log_warning "✗ Response time: ${response_time}s (slow)"
    fi
    
    log_success "Post-deployment verification completed"
}

# Rollback function
rollback() {
    if [[ -n "${BACKUP_DIR:-}" ]] && [[ -f "${BACKUP_DIR}/image_tag.txt" ]]; then
        local backup_image=$(cat "${BACKUP_DIR}/image_tag.txt")
        log_warning "Rolling back to: $backup_image"
        
        # Stop current deployment
        docker stop calculator-app-prod
        docker rm calculator-app-prod
        
        # Restore from backup
        docker run -d \
            --name calculator-app-prod \
            --restart unless-stopped \
            -p "${APP_PORT}:5000" \
            "$backup_image"
        
        log_success "Rollback completed"
    else
        log_error "No backup available for rollback"
        exit 1
    fi
}

# Cleanup old images and containers
cleanup() {
    log_info "Cleaning up old images and containers..."
    
    # Remove old images (keep last 5)
    docker images "calculator-app" --format "{{.Tag}}" | tail -n +6 | xargs -r docker rmi "calculator-app:" 2>/dev/null || true
    
    # Remove old backup images (keep last 3)
    docker images --format "{{.Repository}}:{{.Tag}}" | grep "calculator-app:backup-" | tail -n +4 | xargs -r docker rmi 2>/dev/null || true
    
    # Clean up unused volumes and networks
    docker system prune -f --volumes
    
    log_success "Cleanup completed"
}

# Main deployment function
main() {
    log_info "Starting Calculator App deployment..."
    log_info "Environment: $ENVIRONMENT"
    log_info "Version: $VERSION"
    log_info "Timestamp: $TIMESTAMP"
    
    # Validate inputs
    validate_environment
    
    # Load configuration
    load_config
    
    # Pre-deployment checks
    pre_deployment_checks
    
    # Create backup (production only)
    backup_current_deployment
    
    # Deploy based on environment
    case "$ENVIRONMENT" in
        dev)
            deploy_dev
            ;;
        staging)
            deploy_staging
            ;;
        production)
            deploy_production
            ;;
    esac
    
    # Post-deployment verification
    if ! post_deployment_verification; then
        if [[ "$ENVIRONMENT" == "production" ]]; then
            log_error "Post-deployment verification failed, initiating rollback..."
            rollback
            exit 1
        else
            log_warning "Post-deployment verification failed, but continuing for non-production environment"
        fi
    fi
    
    # Cleanup (optional)
    if [[ "${CLEANUP:-true}" == "true" ]]; then
        cleanup
    fi
    
    log_success "Deployment completed successfully!"
    log_info "Application is now running on $ENVIRONMENT environment"
    
    # Display useful information
    echo
    echo "==================================="
    echo "   DEPLOYMENT SUMMARY"
    echo "==================================="
    echo "Environment: $ENVIRONMENT"
    echo "Version: $VERSION"
    echo "Port: $APP_PORT"
    echo "Domain: ${DOMAIN:-localhost}"
    echo "Replicas: ${REPLICAS:-1}"
    echo "Memory Limit: ${MEMORY_LIMIT:-512Mi}"
    echo "CPU Limit: ${CPU_LIMIT:-500m}"
    echo "==================================="
}

# Handle script interruption
trap 'log_error "Deployment interrupted"; exit 1' INT TERM

# Help function
show_help() {
    echo "Calculator App Deployment Script"
    echo
    echo "Usage: $0 <environment> [version]"
    echo
    echo "Environments:"
    echo "  dev         - Development environment"
    echo "  staging     - Staging environment"
    echo "  production  - Production environment"
    echo
    echo "Options:"
    echo "  version     - Docker image version (default: latest)"
    echo
    echo "Examples:"
    echo "  $0 dev"
    echo "  $0 staging v1.2.3"
    echo "  $0 production v1.2.3"
    echo
    echo "Environment variables:"
    echo "  CLEANUP=false     - Skip cleanup after deployment"
    echo "  STAGING_SECRET_KEY - Secret key for staging"
    echo "  PRODUCTION_SECRET_KEY - Secret key for production"
}

# Check if help is requested
if [[ "${1:-}" == "-h" ]] || [[ "${1:-}" == "--help" ]]; then
    show_help
    exit 0
fi

# Run main function
main "$@"
