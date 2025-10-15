# 🐧 Linux Installation Guide

## 📋 Requirements
- Ubuntu 20.04+ / Debian 11+ / CentOS 8+
- Terminal access

## 🔧 Step-by-Step Installation

### 1. Update System
```bash
# For Ubuntu/Debian
sudo apt update && sudo apt upgrade -y

# For CentOS/RHEL
# sudo dnf update -y
```

### 2. Install Python 3.12
```bash
# Ubuntu/Debian
sudo apt install python3.12 python3.12-venv python3-pip git -y

# CentOS/RHEL (if available)
# sudo dnf install python3.12 python3-pip git -y

# Verify installation
python3.12 --version
```

### 3. Setup Bot Environment
```bash
# Create virtual environment
python3.12 -m venv ~/bot_env

# Activate environment
source ~/bot_env/bin/activate

# Navigate to bot folder
cd ~/Downloads/customer_package
```

### 4. Install Dependencies
```bash
# Install packages (use --break-system-packages flag)
pip install --break-system-packages python-dotenv requests eth-account websockets
pip install --break-system-packages git+https://github.com/elliottech/lighter-python.git
```

### 5. Run the Bot
```bash
# Start bot
python main.py
```

## 🔄 Daily Usage
```bash
# Every time you use the bot:
source ~/bot_env/bin/activate
cd ~/Downloads/customer_package
python main.py
```

## ⚠️ Important Notes
- Use terminal or command line interface
- Must activate virtual environment every time
- Ensure you have internet connection for package installation

## 🆘 If Python 3.12 not available
```bash
# Add deadsnakes PPA (Ubuntu only)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv
```

---
🚀 Ready to trade on Lighter Exchange! 