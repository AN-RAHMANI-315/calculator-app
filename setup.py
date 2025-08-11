"""
Setup configuration for Calculator App.
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Version
version = os.environ.get("APP_VERSION", "1.0.0")

setup(
    name="calculator-app",
    version=version,
    author="DevOps Team",
    author_email="devops@company.com",
    description="A comprehensive Python calculator application with CI/CD pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/company/calculator-app",
    project_urls={
        "Bug Tracker": "https://github.com/company/calculator-app/issues",
        "Documentation": "https://docs.company.com/calculator-app",
        "Source Code": "https://github.com/company/calculator-app",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Flask",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "pytest-html>=4.1.1",
            "flake8>=6.1.0",
            "black>=23.10.1",
            "safety>=2.3.5",
            "bandit>=1.7.5",
            "coverage>=7.3.2",
        ],
        "monitoring": [
            "prometheus-client>=0.18.0",
            "statsd>=4.0.1",
        ],
        "cache": [
            "redis>=5.0.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "calculator-cli=src.cli:cli",
            "calculator-web=src.web_app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="calculator, math, flask, cli, devops, ci-cd",
)
