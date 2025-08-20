# Detectum-OSINT Documentation

**Complete Technical Documentation and User Guide**

*Developed by Vishal Coodye for Detectum Cybersecurity, Republic of Mauritius*

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Installation Guide](#installation-guide)
4. [Configuration](#configuration)
5. [Usage Examples](#usage-examples)
6. [API Reference](#api-reference)
7. [Troubleshooting](#troubleshooting)
8. [Security Considerations](#security-considerations)
9. [Performance Optimization](#performance-optimization)
10. [Development Guide](#development-guide)

---

## Overview

### What is Detectum-OSINT?

Detectum-OSINT is a high-performance, enterprise-grade Open Source Intelligence (OSINT) investigation tool designed for cybersecurity professionals, law enforcement, and digital investigators. It provides comprehensive username investigation capabilities across thousands of online platforms.

### Core Capabilities

- **Multi-Platform Investigation**: Check username existence across 50+ major platforms
- **Async Processing**: High-performance concurrent checking using Python asyncio
- **Intelligent Detection**: Advanced pattern matching for account existence verification
- **Comprehensive Reporting**: Multiple output formats with detailed investigation results
- **Professional Integration**: Designed for enterprise cybersecurity workflows

### Use Cases

- **Threat Intelligence**: Identify threat actor presence across platforms
- **Digital Forensics**: Comprehensive digital footprint analysis
- **Corporate Security**: Employee social media presence verification
- **Law Enforcement**: Criminal investigation support
- **Penetration Testing**: Target reconnaissance and profiling

---

## Architecture

### System Design

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   CLI Interface │───▶│  DetectumOSINT   │───▶│  Sites Database │
└─────────────────┘    │     Engine       │    └─────────────────┘
                       └──────────────────┘
                                │
                       ┌──────────────────┐
                       │  Async HTTP      │
                       │   Client Pool    │
                       └──────────────────┘
                                │
                       ┌──────────────────┐
                       │  Pattern         │
                       │  Matching       │
                       └──────────────────┘
```

### Key Components

1. **CLI Interface** (`detectum_osint.py`)
   - Command-line argument parsing
   - User interaction and output formatting
   - Error handling and logging

2. **Core Engine** (`DetectumOSINT` class)
   - Async HTTP session management
   - Concurrent site checking
   - Result aggregation and analysis

3. **Sites Database** (`data/sites.json`)
   - Platform definitions and URLs
   - Categorization and popularity scoring
   - Customizable site configurations

4. **HTTP Client** (aiohttp-based)
   - Async HTTP requests with timeouts
   - Connection pooling and rate limiting
   - Error handling and retry logic

---

## Installation Guide

### Prerequisites

- **Python 3.10+** (3.11+ recommended)
- **pip** package manager
- **Windows 10/11** (optimal performance)
- **Stable internet connection**

### Step-by-Step Installation

#### Method 1: Direct Installation

```bash
# Clone repository
git clone https://github.com/detectum-cybersecurity/detectum-osint.git
cd detectum-osint

# Install dependencies
pip install -r requirements.txt

# Verify installation
python detectum_osint.py --help
```

#### Method 2: pip Installation

```bash
# Install from PyPI (when available)
pip install detectum-osint

# Verify installation
detectum-osint --help
```

#### Method 3: Development Installation

```bash
# Clone and install in development mode
git clone https://github.com/detectum-cybersecurity/detectum-osint.git
cd detectum-osint
pip install -e .

# Run tests
python -m pytest tests/
```

### Windows-Specific Setup

#### Batch File Setup

1. Ensure `detectum-osint.bat` is in your PATH or current directory
2. Run: `detectum-osint.bat username`

#### PowerShell Setup

1. Set execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
2. Run: `.\detectum-osint.ps1 -Username "username"`

---

## Configuration

### Sites Database Customization

The `data/sites.json` file contains all supported platforms. Each site has the following structure:

```json
{
  "SiteName": {
    "url": "https://example.com/user/{account}",
    "category": "social",
    "country": "global",
    "popularity": 85
  }
}
```

#### Field Descriptions

- **url**: Template URL with `{account}` placeholder
- **category**: Site classification (social, professional, gaming, etc.)
- **country**: Geographic focus or availability
- **popularity**: Relative importance score (0-100)

#### Adding Custom Sites

```json
{
  "MyCustomSite": {
    "url": "https://mycustomsite.com/profile/{account}",
    "category": "custom",
    "country": "global",
    "popularity": 50
  }
}
```

### Environment Variables

```bash
# Custom timeout (default: 30 seconds)
export DETECTUM_TIMEOUT=60

# Custom user agent
export DETECTUM_USER_AGENT="Custom User Agent String"

# Debug mode
export DETECTUM_DEBUG=true
```

### Configuration File

Create `config.yaml` for advanced configuration:

```yaml
# Detectum-OSINT Configuration
http:
  timeout: 30
  max_connections: 100
  max_connections_per_host: 10
  user_agent: "Detectum-OSINT/1.0"

investigation:
  default_sites_limit: 500
  concurrent_checks: 50
  retry_attempts: 3

output:
  default_format: "json"
  include_timestamps: true
  include_metadata: true

logging:
  level: "INFO"
  format: "%(asctime)s - %(levelname)s - %(message)s"
  file: "detectum-osint.log"
```

---

## Usage Examples

### Basic Investigation

```bash
# Simple username check
python detectum_osint.py john_doe

# Verbose output
python detectum_osint.py john_doe -v

# Save to file
python detectum_osint.py john_doe -f results.txt
```

### Advanced Investigation

```bash
# Check specific sites only
python detectum_osint.py john_doe -s Facebook Twitter Instagram

# Multiple usernames
python detectum_osint.py john_doe jane_smith admin_user

# Custom output format
python detectum_osint.py john_doe -o txt -f report.txt

# Site category filtering
python detectum_osint.py john_doe --category social professional
```

### Windows Utilities

#### Batch File Usage

```batch
# Basic usage
detectum-osint.bat john_doe

# With parameters (if supported)
detectum-osint.bat john_doe
```

#### PowerShell Usage

```powershell
# Basic investigation
.\detectum-osint.ps1 -Username "john_doe"

# Advanced options
.\detectum-osint.ps1 -Username "john_doe" -OutputFile "results.txt" -OutputFormat txt

# Specific sites
.\detectum-osint.ps1 -Username "john_doe" -Sites "Facebook,Twitter,Instagram"
```

### Programmatic Usage

```python
from detectum_osint import DetectumOSINT
import asyncio

async def main():
    tool = DetectumOSINT()
    
    # Investigate username
    results = await tool.investigate_username("john_doe")
    
    # Generate report
    report = tool.generate_report(results, "txt")
    print(report)

# Run investigation
asyncio.run(main())
```

---

## API Reference

### DetectumOSINT Class

#### Constructor

```python
DetectumOSINT()
```

Creates a new DetectumOSINT instance with default configuration.

#### Methods

##### `investigate_username(username, sites=None)`

Investigates a username across multiple platforms.

**Parameters:**
- `username` (str): Username to investigate
- `sites` (list, optional): Specific sites to check

**Returns:**
- `dict`: Investigation results with comprehensive metadata

**Example:**
```python
results = await tool.investigate_username("john_doe")
print(f"Found {results['accounts_found']} accounts")
```

##### `check_username(username, site_info)`

Checks username existence on a specific site.

**Parameters:**
- `username` (str): Username to check
- `site_info` (dict): Site configuration information

**Returns:**
- `dict`: Site-specific check results

##### `generate_report(results, output_format='json')`

Generates formatted investigation reports.

**Parameters:**
- `results` (dict): Investigation results
- `output_format` (str): Output format ('json' or 'txt')

**Returns:**
- `str`: Formatted report

### Result Structure

```json
{
  "username": "john_doe",
  "investigation_date": "2025-01-15T10:30:00",
  "total_sites_checked": 50,
  "accounts_found": 12,
  "success_rate": "24.00%",
  "found_sites": ["Facebook", "Twitter", "GitHub"],
  "detailed_results": {
    "Facebook": {
      "exists": true,
      "url": "https://facebook.com/john_doe",
      "status_code": 200,
      "error_type": null,
      "timestamp": "2025-01-15T10:30:00"
    }
  }
}
```

---

## Troubleshooting

### Common Issues

#### Python Version Issues

**Problem**: "Python version not supported"
**Solution**: Ensure Python 3.10+ is installed and in PATH

```bash
# Check Python version
python --version

# Install Python 3.10+ from python.org
```

#### Dependency Issues

**Problem**: "Module not found" errors
**Solution**: Install required dependencies

```bash
# Install dependencies
pip install -r requirements.txt

# Upgrade pip if needed
python -m pip install --upgrade pip
```

#### Network Issues

**Problem**: "Connection timeout" errors
**Solution**: Check network configuration

```bash
# Test connectivity
ping google.com

# Check firewall settings
# Verify proxy configuration if applicable
```

#### Permission Issues (Windows)

**Problem**: "Access denied" errors
**Solution**: Run as administrator or adjust permissions

```powershell
# Set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Run PowerShell as administrator if needed
```

### Debug Mode

Enable debug logging for troubleshooting:

```bash
# Set debug environment variable
export DETECTUM_DEBUG=true

# Run with verbose output
python detectum_osint.py username -v
```

### Log Files

Check log files for detailed error information:

```bash
# View recent logs
tail -f detectum-osint.log

# Search for specific errors
grep "ERROR" detectum-osint.log
```

---

## Security Considerations

### Legal Compliance

- **Authorized Use Only**: Ensure proper authorization for investigations
- **Privacy Laws**: Comply with GDPR, CCPA, and local privacy regulations
- **Terms of Service**: Respect platform terms of service
- **Rate Limiting**: Avoid overwhelming target servers

### Data Protection

- **Secure Storage**: Encrypt investigation results
- **Access Control**: Limit access to investigation data
- **Audit Logging**: Maintain investigation audit trails
- **Data Retention**: Implement appropriate data retention policies

### Network Security

- **VPN Usage**: Use VPN for sensitive investigations
- **Proxy Configuration**: Configure proxies if required
- **Firewall Rules**: Ensure proper firewall configuration
- **SSL Verification**: Verify SSL certificates for secure connections

### Ethical Guidelines

- **Professional Conduct**: Maintain professional standards
- **Minimal Impact**: Minimize impact on target systems
- **Transparency**: Be transparent about investigation purposes
- **Accountability**: Take responsibility for investigation actions

---

## Performance Optimization

### Async Configuration

```python
# Optimize async settings
async def optimize_performance():
    # Increase connection limits
    connector = aiohttp.TCPConnector(
        limit=200,                    # Total connections
        limit_per_host=20,            # Per-host connections
        ttl_dns_cache=300,            # DNS cache TTL
        use_dns_cache=True            # Enable DNS caching
    )
    
    # Configure timeouts
    timeout = aiohttp.ClientTimeout(
        total=60,                     # Total timeout
        connect=10,                   # Connection timeout
        sock_read=30                  # Socket read timeout
    )
```

### Memory Management

```python
# Optimize memory usage
class OptimizedDetectumOSINT(DetectumOSINT):
    def __init__(self):
        super().__init__()
        self.max_concurrent = 100     # Limit concurrent requests
        self.batch_size = 50          # Process in batches
```

### Caching Strategies

```python
# Implement result caching
import hashlib
import pickle

class CachedDetectumOSINT(DetectumOSINT):
    def __init__(self, cache_file="cache.pkl"):
        super().__init__()
        self.cache_file = cache_file
        self.cache = self._load_cache()
    
    def _get_cache_key(self, username, sites):
        data = f"{username}:{sorted(sites) if sites else 'all'}"
        return hashlib.md5(data.encode()).hexdigest()
    
    def _load_cache(self):
        try:
            with open(self.cache_file, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}
    
    def _save_cache(self):
        with open(self.cache_file, 'wb') as f:
            pickle.dump(self.cache, f)
```

---

## Development Guide

### Project Structure

```
detectum-osint/
├── detectum_osint.py          # Main application
├── data/
│   └── sites.json            # Sites database
├── tests/                    # Test suite
├── docs/                     # Documentation
├── scripts/                  # Utility scripts
├── requirements.txt          # Dependencies
├── setup.py                 # Installation script
├── README.md                # Project overview
├── DOCUMENTATION.md         # This file
├── LICENSE                  # MIT license
├── detectum-osint.bat       # Windows batch utility
└── detectum-osint.ps1       # PowerShell utility
```

### Development Setup

```bash
# Clone repository
git clone https://github.com/detectum-cybersecurity/detectum-osint.git
cd detectum-osint

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -e .

# Install development tools
pip install pytest black flake8 mypy
```

### Testing

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=detectum_osint

# Run specific test file
python -m pytest tests/test_detectum_osint.py

# Run with verbose output
python -m pytest -v
```

### Code Quality

```bash
# Format code
black detectum_osint.py

# Lint code
flake8 detectum_osint.py

# Type checking
mypy detectum_osint.py
```

### Contributing Guidelines

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/new-feature`
3. **Make changes** following coding standards
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Submit pull request** with detailed description

### Release Process

1. **Update version** in `setup.py` and `__init__.py`
2. **Update changelog** with new features and fixes
3. **Run tests** to ensure quality
4. **Create release tag**: `git tag v1.1.0`
5. **Push changes**: `git push origin main --tags`
6. **Update PyPI** package (when applicable)

---

## Support and Contact

### Technical Support

- **Email**: support@detectum.mu
- **GitHub Issues**: [Report Issues](https://github.com/detectum-cybersecurity/detectum-osint/issues)
- **Documentation**: [Full Documentation](https://detectum.it.com/documents/PUBLICATIONS/osint)

### Business Inquiries

- **Email**: info@detectum.mu
- **Address**: Republic of Mauritius
- **Website**: [www.detectum.it.com](https://www.detectum.it.com)

### Community

- **LinkedIn**: [Detectum Cybersecurity][(https://www.linkedin.com/in/r-i-y-a-ai-53a5a1b)
- **GitHub**: [detectum-cybersecurity](https://github.com/detectum-cybersecurity)
- **LinkedIn**: [Paypal Donation](https://www.paypal.com/ncp/payment/2R65EQMNCPEMQ)
---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2025 Detectum Cybersecurity, Republic of Mauritius**

---

**🕵️‍♂️ Detectum-OSINT - Empowering Cybersecurity Professionals Worldwide**

*Developed with ❤️ in the Republic of Mauritius by Vishal Coodye*

