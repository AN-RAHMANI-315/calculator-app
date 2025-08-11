# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set metadata
LABEL maintainer="DevOps Team <devops@company.com>"
LABEL version="1.0.0"
LABEL description="Calculator App - Python Flask Application"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=web_app.py \
    FLASK_ENV=production \
    PORT=5000

# Create app user for security (don't run as root)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        curl \
        && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY setup.py .
COPY README.md .

# Install the application
RUN pip install -e .

# Create necessary directories
RUN mkdir -p /app/logs /app/tmp \
    && chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

# Expose port
EXPOSE ${PORT}

# Start command using gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "30", "--keep-alive", "2", "--max-requests", "1000", "--max-requests-jitter", "100", "src.web_app:app"]
