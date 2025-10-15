# 🖥️ Windows Installation Guide

## 📋 Requirements
- Windows 10/11
- Administrator access

## 🔧 Step-by-Step Installation

### 1. Install WSL Ubuntu
```powershell
# Open PowerShell as Administrator
wsl --install Ubuntu
```
**Restart your computer after installation**

### 2. Open Ubuntu Terminal
- Search "Ubuntu" in Start Menu
- Open Ubuntu terminal

### 3. Install Python 3.12
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.12
sudo apt install python3.12 python3.12-venv python3-pip git -y

# Verify installation
python3.12 --version
git --version
```

### 4. Setup Bot Environment
```bash
# Create virtual environment
python3.12 -m venv ~/bot_env

# Activate environment
source ~/bot_env/bin/activate

# Navigate to bot folder
cd /mnt/c/Users/YourUsername/Downloads/customer_package
```

### 5. Install Dependencies
```bash
# Install packages (use --break-system-packages flag)
pip install --break-system-packages python-dotenv requests eth-account websockets
pip install --break-system-packages git+https://github.com/elliottech/lighter-python.git
```

### 6. Run the Bot
```bash
# Start bot
python main.py
```

## 🔄 Daily Usage
```bash
# Every time you use the bot:
source ~/bot_env/bin/activate
cd /mnt/c/Users/YourUsername/Downloads/customer_package
python main.py
```

## ⚠️ Important Notes
- Always use Ubuntu terminal (not Windows CMD/PowerShell)
- Must activate virtual environment every time
- Bot files should be in Windows folder for easy access

---
🚀 Ready to trade on Lighter Exchange! 