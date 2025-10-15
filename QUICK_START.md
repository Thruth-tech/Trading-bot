# ⚡ Quick Start Guide

Get your Lighter Trading Bot running in 5 minutes!

## 🚀 Super Fast Setup

### 1️⃣ Choose Your System
- 🖥️ **Windows**: [INSTALL_WINDOWS.md](INSTALL_WINDOWS.md)
- 🍎 **macOS**: [INSTALL_MAC.md](INSTALL_MAC.md)  
- 🐧 **Linux**: [INSTALL_LINUX.md](INSTALL_LINUX.md)

### 2️⃣ One-Command Setup (Linux/WSL)
```bash
# Install Python 3.12 + Create environment + Install packages
sudo apt update && sudo apt install python3.12 python3.12-venv -y && python3.12 -m venv ~/bot_env && source ~/bot_env/bin/activate && pip install --break-system-packages python-dotenv requests eth-account websockets && pip install --break-system-packages git+https://github.com/elliottech/lighter-python.git
```

### 3️⃣ Run the Bot
```bash
# Navigate to bot folder
cd path/to/customer_package

# Activate environment
source ~/bot_env/bin/activate

# Start bot
python main.py
```

## 🔑 Quick API Setup

### In Bot Menu:
1. **Select:** `3. 🔑 Setup API Key`
2. **Enter:** Your Lighter API credentials
3. **Done!** Start trading

### Manual Setup (.env file):
```bash
LIGHTER_API_KEY_PRIVATE_KEY='your_key_here'
WALLET_ADDRESS=0xYourWalletAddress
API_KEY_INDEX=0
MARKET_ID='2'
TRADE_AMOUNT='100'
```

## 🎯 Start Trading

### Main Menu Options:
- **1. 🤖 Trading Bot** → Start automated trading
- **2. 📊 Market Data** → View available markets  
- **3. 🔑 Setup API Key** → Configure credentials

### Trading Bot Menu:
- **1. 🔄 Start Liquidity Provider Bot** → Begin trading
- **2. 📝 Edit Trading Config** → Modify parameters

## ⚡ Daily Usage
```bash
# Every time you trade:
source ~/bot_env/bin/activate
cd path/to/customer_package
python main.py
```

## 🆘 Common Issues

### ❌ "No module named 'lighter'"
```bash
# Fix: Reinstall in virtual environment
source ~/bot_env/bin/activate
pip install --break-system-packages git+https://github.com/elliottech/lighter-python.git
```

### ❌ "bad magic number"
```bash
# Fix: Wrong Python version
python --version  # Must be 3.12.x
```

### ❌ Environment issues
```bash
# Fix: Recreate environment
rm -rf ~/bot_env
python3.12 -m venv ~/bot_env
source ~/bot_env/bin/activate
# Reinstall packages
```

## 💡 Pro Tips

### ⚡ **Fastest Setup**: Use one-command setup above
### 🔄 **Daily Use**: Create alias for quick activation
```bash
echo "alias botenv='source ~/bot_env/bin/activate && cd ~/path/to/customer_package'" >> ~/.bashrc
```
### 🎯 **Trading**: Start with small amounts to test
### 📊 **Monitoring**: Use Market Data menu to check prices

---

🚀 **You're ready to trade!** Start with the API setup and begin automated trading on Lighter Exchange. 