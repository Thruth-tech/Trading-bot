# 🎯 JOBJAB AIRDROP HUNTER - Display Banner (Python Version)

Universal banner system สำหรับทุกโปรเจค JOBJAB AIRDROP HUNTER แปลงจาก JavaScript เป็น Python

## 📱 Contact
Telegram: **t.me/jobjab_airdrop_hunter**

---

## 🚀 การใช้งาน

### 1. **Import Banner Functions**

```python
from display_banner import (
    display_jobjab_banner,
    display_jobjab_header,
    display_jobjab_logo,
    display_jobjab_goodbye,
    display_jobjab_interrupted
)
```

### 2. **Available Functions**

#### `display_jobjab_banner(wait_for_enter=False)`
แสดง ASCII Art banner แบบเต็ม
```python
# แสดง banner อย่างเดียว
display_jobjab_banner()

# แสดง banner และรอกด Enter
display_jobjab_banner(wait_for_enter=True)
```

#### `display_jobjab_header(subtitle="Main Menu")`
แสดง header แบบกะทัดรัดสำหรับหน้าเมนู
```python
display_jobjab_header()  # Default: "Main Menu"
display_jobjab_header('Test Mode')
display_jobjab_header('Production Mode')
display_jobjab_header('Settings')
```

#### `display_jobjab_logo()`
แสดง logo แบบง่าย
```python
display_jobjab_logo()
```

#### `display_jobjab_goodbye()`
แสดงข้อความลาก่อน
```python
display_jobjab_goodbye()
```

#### `display_jobjab_interrupted()`
แสดงข้อความเมื่อถูกขัดจังหวะ
```python
display_jobjab_interrupted()
```

---

## 🎨 **Preview**

### Full Banner
```
      ██╗ ██████╗ ██████╗      ██╗ █████╗ ██████╗ 
      ██║██╔═══██╗██╔══██╗     ██║██╔══██╗██╔══██╗
      ██║██║   ██║██████╔╝     ██║███████║██████╔╝
      ██║██║   ██║██╔══██╗██   ██║██╔══██║██╔══██╗
    ████║╚██████╔╝██████╔╝╚█████╔╝██║  ██║██████╔╝
    ╚═══╝ ╚═════╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═════╝ 
    █████╗ ██╗██████╗ ██████╗ ██████╗  ██████╗ ██████╗ 
   ██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
   ███████║██║██████╔╝██║  ██║██████╔╝██║   ██║██████╔╝
   ██╔══██║██║██╔══██╗██║  ██║██╔══██╗██║   ██║██╔═══╝ 
   ██║  ██║██║██║  ██║██████╔╝██║  ██║╚██████╔╝██║     
   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
    ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
    ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

📱 Telegram: t.me/jobjab_airdrop_hunter
🛡️ Universal Framework - 99.9% Human-Like Anti-Detection
🚀 Enhanced Features: Fingerprinting, Psychology, Timing
🌐 Multi-Domain Cookie Management & Proxy Intelligence
═══════════════════════════════════════════════════════════
💰 DONATE:
🔗 EVM (all): 0xDeB20b7a9c9A54e1Cfce270416752F9982B6B25C
☀️ Solana: CyNMKJUxJ4Y75LnQxaGCjyTrsivCPUvirL1DipWqyZAy
═══════════════════════════════════════════════════════════
```

### Header
```
🎯 JOBJAB AIRDROP HUNTER - Main Menu
📱 Telegram: t.me/jobjab_airdrop_hunter
═══════════════════════════════════════
```

### Logo
```
🎯 JOBJAB AIRDROP HUNTER
📱 Telegram: t.me/jobjab_airdrop_hunter
```

---

## 📝 **ตัวอย่างการใช้งานในโปรเจค**

### ในไฟล์ main.py ของโปรเจคใหม่:

```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'display_banner'))

from display_banner import (
    display_jobjab_banner,
    display_jobjab_header,
    display_jobjab_goodbye,
    display_jobjab_interrupted
)
import signal

def signal_handler(sig, frame):
    """Handle Ctrl+C"""
    display_jobjab_interrupted()
    sys.exit(0)

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

def main():
    # แสดง banner และรอกด Enter
    display_jobjab_banner(wait_for_enter=True)
    
    # เมนูหลัก
    while True:
        display_jobjab_header('Your Project Name')
        
        # เมนูต่างๆ
        choice = input("Select option: ")
        
        # การทำงาน...
        
        if choice == 'exit':
            display_jobjab_goodbye()
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        display_jobjab_interrupted()
        sys.exit(0)
```

---

## 🔧 **การติดตั้งและใช้งาน**

### 1. **Copy Files**
Copy โฟลเดอร์ `display_banner/` ไปยังโปรเจคของคุณ

### 2. **Import and Use**
```python
sys.path.append(os.path.join(os.path.dirname(__file__), 'display_banner'))
from display_banner import display_jobjab_banner

# ใช้งาน
display_jobjab_banner(wait_for_enter=True)
```

### 3. **ทดสอบ**
```bash
# ทดสอบตัวอย่าง
python display_banner/example.py
```

---

## 🎯 **Features**

- ✅ **Universal Design**: ใช้ได้กับทุกโปรเจค JOBJAB
- ✅ **Python Native**: ANSI color codes สำหรับ terminal
- ✅ **Cross-Platform**: รองรับ Windows, Linux, macOS
- ✅ **Easy Integration**: Copy & Paste ได้เลย
- ✅ **Beautiful ASCII Art**: สวยงามและเป็นเอกลักษณ์
- ✅ **Signal Handling**: รองรับ Ctrl+C interrupt
- ✅ **Donation Support**: รองรับ EVM chains และ Solana

---

**🚀 Ready to brand your Python projects with JOBJAB style!** 