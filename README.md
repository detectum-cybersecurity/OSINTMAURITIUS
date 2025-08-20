# 🕵️‍♂️ Detectum-OSINT

**Advanced OSINT Investigation Tool for Cybersecurity Professionals**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made in Mauritius](https://img.shields.io/badge/Made%20in-Mauritius-green.svg)](https://mauritius.govmu.org/)

---

## 🎯 About Detectum-OSINT

**Detectum-OSINT** is a powerful, enterprise-grade Open Source Intelligence (OSINT) investigation tool developed exclusively by **Vishal Coodye** for **Detectum Cybersecurity, Republic of Mauritius**. This tool represents the pinnacle of digital investigation capabilities, designed specifically for cybersecurity professionals, law enforcement, and private investigators.

### 🌟 Key Features

- **🔍 Comprehensive Username Investigation**: Check thousands of websites simultaneously for username existence
- **⚡ High-Performance Async Engine**: Built with modern Python async/await for lightning-fast investigations
- **🌐 Multi-Platform Coverage**: Supports social media, professional networks, development platforms, and more
- **📊 Detailed Reporting**: Generate comprehensive reports in JSON and text formats
- **🛡️ Professional-Grade**: Designed for cybersecurity investigations and threat intelligence
- **🚀 No API Keys Required**: Works out-of-the-box with no external dependencies
- **📱 Windows Command Utility**: Fast and efficient Windows-based command-line interface

---

## 🏢 About Detectum Cybersecurity

**Detectum Cybersecurity** is a leading cybersecurity firm based in the Republic of Mauritius, specializing in:

- **Digital Forensics & Incident Response**
- **Threat Intelligence & Analysis**
- **Cybersecurity Consulting & Training**
- **OSINT & Digital Investigations**
- **Penetration Testing & Security Audits**

**Location**: Republic of Mauritius  
**Website**: [www.detectum.it.com](https://www.detectum.it.com)  
**Contact**: v@riyaai.com

---

## 👨‍💻 Developer

**Vishal Coodye**  
*AI Developer * Software Engineer*  
*Detectum Cybersecurity, Republic of Mauritius*

---

## 🚀 Installation

### Prerequisites

- **Python 3.10 or higher** (Python 3.11+ recommended)
- **pip** package manager
- **Windows 10/11** (for optimal performance)

### Quick Installation

```bash
# Clone the repository
git clone https://github.com/detectum-cybersecurity/detectum-osint.git
cd detectum-osint

# Install dependencies
pip install -r requirements.txt

# Run the tool
python detectum_osint.py username
```

### Alternative Installation Methods

#### Using pip (Recommended)

```bash
pip install detectum-osint
```

#### Manual Installation

```bash
# Download and extract
wget https://github.com/detectum-cybersecurity/detectum-osint/archive/main.zip
unzip main.zip
cd detectum-osint-main

# Install
pip install -r requirements.txt
```

---

## 🎮 Usage

### Basic Usage

```bash
# Investigate a single username
python detectum_osint.py username

# Investigate with verbose output
python detectum_osint.py username -v

# Save results to file
python detectum_osint.py username -f results.txt
```

### Advanced Usage

```bash
# Check specific sites only
python detectum_osint.py username -s Facebook Twitter Instagram

# Generate JSON output
python detectum_osint.py username -o json

# Generate text report
python detectum_osint.py username -o txt -f report.txt
```

### Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `username` | Username to investigate | `python detectum_osint.py john_doe` |
| `-s, --sites` | Specific sites to check | `-s Facebook Twitter` |
| `-o, --output` | Output format (json/txt) | `-o json` |
| `-f, --output-file` | Save results to file | `-f results.txt` |
| `-v, --verbose` | Enable verbose logging | `-v` |
| `-h, --help` | Show help message | `-h` |

---

## 🖥️ Windows Command Utility

For Windows users, we provide a fast and efficient command utility:

### Windows Batch File

```batch
@echo off
echo ========================================
echo    DETECTUM-OSINT - Windows Utility
echo ========================================
echo.

if "%1"=="" (
    echo Usage: detectum-osint.bat username
    echo Example: detectum-osint.bat john_doe
    pause
    exit /b 1
)

echo Starting investigation for: %1
echo.

python detectum_osint.py %1

echo.
echo Investigation completed!
pause
```

### Windows PowerShell Script

```powershell
param(
    [Parameter(Mandatory=$true)]
    [string]$Username
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   DETECTUM-OSINT - PowerShell Utility" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Starting investigation for: $Username" -ForegroundColor Green
Write-Host ""

python detectum_osint.py $Username

Write-Host ""
Write-Host "Investigation completed!" -ForegroundColor Green
```

---

## 📊 Supported Platforms

### Social Media
- **Facebook** - Global social networking
- **Twitter** - Microblogging platform
- **Instagram** - Photo and video sharing
- **LinkedIn** - Professional networking
- **TikTok** - Short-form video platform
- **Snapchat** - Multimedia messaging
- **Discord** - Gaming and community platform

### Professional & Business
- **GitHub** - Software development platform
- **Stack Overflow** - Developer Q&A platform
- **AngelList** - Startup and investment platform
- **Crunchbase** - Business information platform

### Creative & Media
- **YouTube** - Video sharing platform
- **Twitch** - Live streaming platform
- **DeviantArt** - Art community platform
- **Behance** - Creative portfolio platform
- **Flickr** - Photo sharing platform

### And many more...

---

## 📈 Performance Features

- **Async HTTP Requests**: Concurrent checking of multiple sites
- **Smart Rate Limiting**: Prevents overwhelming target servers
- **Intelligent Pattern Matching**: Advanced detection algorithms
- **Comprehensive Error Handling**: Robust error management
- **Real-time Progress Tracking**: Live investigation status updates

---

## 🔧 Configuration

### Customizing Sites Database

Edit `data/sites.json` to add or modify supported platforms:

```json
{
  "CustomSite": {
    "url": "https://example.com/user/{account}",
    "category": "custom",
    "country": "global",
    "popularity": 50
  }
}
```

### Environment Variables

```bash
# Set custom timeout (default: 30 seconds)
export DETECTUM_TIMEOUT=60

# Set custom user agent
export DETECTUM_USER_AGENT="Custom User Agent"
```

---

## 📋 Requirements

### System Requirements

- **Operating System**: Windows 10/11, macOS 10.15+, Ubuntu 18.04+
- **Python**: 3.10 or higher
- **RAM**: Minimum 4GB, Recommended 8GB+
- **Storage**: 100MB free space
- **Network**: Stable internet connection

### Python Dependencies

- `aiohttp` >= 3.8.0 - Async HTTP client
- `asyncio` >= 3.4.3 - Async I/O support
- `pathlib2` >= 2.3.7 - Path manipulation
- `typing-extensions` >= 4.0.0 - Type hints support

---

## 🚨 Legal Disclaimer

**⚠️ IMPORTANT: This tool is intended for educational and lawful purposes only.**

The developers and Detectum Cybersecurity do not endorse or encourage any illegal activities or misuse of this tool. Users are responsible for ensuring compliance with all applicable laws and regulations in their jurisdiction.

### Permitted Uses

- **Cybersecurity Research & Education**
- **Digital Forensics Investigations**
- **Threat Intelligence Gathering**
- **Law Enforcement Operations**
- **Corporate Security Audits**
- **Penetration Testing (with proper authorization)**

### Prohibited Uses

- **Unauthorized Access to Systems**
- **Privacy Violations**
- **Harassment or Stalking**
- **Illegal Surveillance**
- **Any Criminal Activities**

---

## 🤝 Contributing

While this tool is developed exclusively by Vishal Coodye for Detectum Cybersecurity, we welcome:

- **Bug Reports**: Help improve tool reliability
- **Feature Suggestions**: Enhance functionality
- **Documentation Improvements**: Better user experience
- **Security Research**: Vulnerability disclosures

### Reporting Issues

1. Check existing issues first
2. Provide detailed reproduction steps
3. Include system information and error logs
4. Use appropriate issue templates

---

## 📞 Support & Contact

### Technical Support

- **Email**: support@detectum.mu
- **GitHub Issues**: [Report Issues](https://github.com/detectum-cybersecurity/detectum-osint/issues)
- **Documentation**: [Full Documentation]([https://docs.detectum.it.com](https://detectum.it.com/documents/PUBLICATIONS/osint)

### Business Inquiries

- **Email**: v@riyaai.com
- **Address**: Republic of Mauritius

---

## 📄 License

**MIT License** - See [LICENSE](LICENSE) file for details.

Copyright (c) 2025 **Detectum Cybersecurity, Republic of Mauritius**

---

## 🙏 Acknowledgments

Special thanks to the cybersecurity community and open-source contributors who have inspired and supported the development of advanced OSINT tools.

---

## 🔄 Version History

### v1.0.0 (Current)
- **Initial Release**: Complete OSINT investigation tool
- **Core Features**: Username checking, async processing, reporting
- **Platform Support**: 50+ major platforms
- **Windows Integration**: Native Windows command utilities

### Upcoming Features
- **Web Interface**: Browser-based investigation dashboard
- **Advanced Analytics**: Machine learning-powered pattern recognition
- **API Integration**: RESTful API for enterprise use
- **Mobile Support**: iOS and Android applications

---

## 📱 Social Media

- **Website**: [www.detectum.it.com](https://www.detectum.it.com)
- **GitHub**: [detectum-cybersecurity](https://github.com/detectum-cybersecurity)

---

**🕵️‍♂️ Detectum-OSINT - Empowering Cybersecurity Professionals Worldwide**

*Developed with ❤️ in the Republic of Mauritius*

