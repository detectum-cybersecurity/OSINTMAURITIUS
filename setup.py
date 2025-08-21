#!/usr/bin/env python3
"""
Detectum-OSINT Setup Script
Advanced OSINT Investigation Tool for Cybersecurity Professionals

Developed by Vishal Coodye for Detectum Cybersecurity, Republic of Mauritius
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="detectum-osint",
    version="1.0.0",
    author="Vishal Coodye",
    author_email="vishal.coodye@detectum.mu",
    description="Advanced OSINT Investigation Tool for Cybersecurity Professionals",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/detectum-cybersecurity/detectum-osint",
    project_urls={
        "Bug Reports": "https://github.com/detectum-cybersecurity/detectum-osint/issues",
        "Source": "https://github.com/detectum-cybersecurity/detectum-osint",
        "Documentation": "https://detectum.it.com/documents/PUBLICATIONS/osint/",
        "Company Website": "https://www.detectum.it.com",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal and Law Enforcement",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: AsyncIO",
        "Typing :: Typed",
    ],
    python_requires=">=3.10",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.18.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "detectum-osint=detectum_osint:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.md", "*.txt", "*.bat", "*.ps1"],
    },
    keywords=[
        "osint",
        "cybersecurity",
        "investigation",
        "username",
        "social-media",
        "digital-forensics",
        "threat-intelligence",
        "penetration-testing",
        "security-audit",
        "mauritius",
        "detectum",
    ],
    platforms=[
        "Windows",
        "Linux",
        "macOS",
    ],
    license="MIT",
    zip_safe=False,
    # Additional metadata
    maintainer="Vishal Coodye",
    maintainer_email="v@riyaai.com",
    download_url="https://github.com/detectum-cybersecurity/detectum-osint/archive/v1.0.0.tar.gz",
    # Project information
    project_name="Detectum-OSINT",
    organization="Detectum Cybersecurity",
    location="Republic of Mauritius",
    website="https://www.detectum.it.com",
    # Security classification
    security_classification="Unclassified",
    intended_use="Cybersecurity investigations, digital forensics, threat intelligence",
    # Contact information
    support_email="v@riyaai.com",
    business_email="v@riyaai.com",
)


