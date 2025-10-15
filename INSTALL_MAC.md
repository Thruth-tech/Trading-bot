# 🍎 macOS Installation Guide

## 📋 Requirements
- macOS 10.15 or later
- Terminal access

## 🔧 Step-by-Step Installation

### 1. Install Homebrew
```bash
# Install Homebrew package manager
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Python 3.12
```bash
# Install Python 3.12 and Git
brew install python@3.12 git

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
# Install packages (use --break-system-packages if needed)
pip install python-dotenv requests eth-account websockets
pip install git+https://github.com/elliottech/lighter-python.git

# If above fails, use:
# pip install --break-system-packages python-dotenv requests eth-account websockets
# pip install --break-system-packages git+https://github.com/elliottech/lighter-python.git
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
- Use Terminal app (Applications → Utilities → Terminal)
- Must activate virtual environment every time
- Keep bot files in Downloads or Desktop for easy access

---
🚀 Ready to trade on Lighter Exchange! 