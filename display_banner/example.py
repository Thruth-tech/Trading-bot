# -*- coding: utf-8 -*-
"""
ตัวอย่างการใช้งาน JOBJAB Banner Functions (Python Version)
สำหรับโปรเจคอื่นๆ
"""

from display_banner import (
    display_jobjab_banner,
    display_jobjab_header,
    display_jobjab_logo,
    display_jobjab_goodbye,
    display_jobjab_interrupted
)
import signal
import sys

def signal_handler(sig, frame):
    """Handle Ctrl+C"""
    display_jobjab_interrupted()
    sys.exit(0)

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

def example1():
    """ตัวอย่าง 1: Full Banner"""
    print('=== ตัวอย่าง 1: Full Banner ===')
    display_jobjab_banner(wait_for_enter=True)

def example2():
    """ตัวอย่าง 2: Headers สำหรับเมนูต่างๆ"""
    print('=== ตัวอย่าง 2: Headers ===')
    
    display_jobjab_header('Main Menu')
    input('Main menu content here...\nPress Enter to continue...')
    
    display_jobjab_header('Test Mode')
    input('Test mode content here...\nPress Enter to continue...')
    
    display_jobjab_header('Production Mode')
    input('Production mode content here...\nPress Enter to continue...')
    
    display_jobjab_header('Settings')
    input('Settings content here...\nPress Enter to continue...')

def example3():
    """ตัวอย่าง 3: Logo แบบง่าย"""
    print('=== ตัวอย่าง 3: Simple Logo ===')
    display_jobjab_logo()
    input('Your app content here...\nPress Enter to continue...')

def example4():
    """ตัวอย่าง 4: Goodbye Message"""
    print('=== ตัวอย่าง 4: Goodbye Message ===')
    display_jobjab_goodbye()

def example5():
    """ตัวอย่าง 5: Interrupted Message"""
    print('=== ตัวอย่าง 5: Interrupted Message ===')
    display_jobjab_interrupted()

def example_full_app():
    """ตัวอย่าง 6: การใช้งานแบบโปรเจคจริง"""
    print('=== ตัวอย่าง 6: Full App Example ===')
    
    # 1. แสดง welcome banner
    display_jobjab_banner(wait_for_enter=True)
    
    # 2. Main menu loop
    while True:
        display_jobjab_header('Example Project')
        
        print('1. 🧪 Test Mode')
        print('2. 🏭 Production Mode')
        print('3. ⚙️ Settings')
        print('4. ❌ Exit')
        print('─' * 40)
        
        choice = input('Enter your choice (1-4): ')
        
        if choice.strip() == '1':
            display_jobjab_header('Test Mode')
            print('🧪 Running test mode...')
            import time
            time.sleep(2)
            print('✅ Test completed!')
            input('Press Enter to continue...')
            
        elif choice.strip() == '2':
            display_jobjab_header('Production Mode')
            print('🏭 Running production mode...')
            import time
            time.sleep(2)
            print('✅ Production completed!')
            input('Press Enter to continue...')
            
        elif choice.strip() == '3':
            display_jobjab_header('Settings')
            print('⚙️ Settings page...')
            input('Press Enter to continue...')
            
        elif choice.strip() == '4':
            display_jobjab_goodbye()
            return
            
        else:
            print('❌ Invalid choice. Please try again.')
            input('Press Enter to continue...')

def main():
    """Main menu สำหรับตัวอย่าง"""
    print('🎯 JOBJAB Banner Functions - Examples\n')
    print('Choose an example to run:')
    print('1. Full Banner with Enter prompt')
    print('2. Different Headers')
    print('3. Simple Logo')
    print('4. Goodbye Message')
    print('5. Interrupted Message')
    print('6. Full App Example')
    print('7. Exit')
    print('─' * 40)
    
    choice = input('Enter your choice (1-7): ')
    
    if choice.strip() == '1':
        example1()
    elif choice.strip() == '2':
        example2()
    elif choice.strip() == '3':
        example3()
    elif choice.strip() == '4':
        example4()
    elif choice.strip() == '5':
        example5()
    elif choice.strip() == '6':
        example_full_app()
        return
    elif choice.strip() == '7':
        display_jobjab_goodbye()
        return
    else:
        print('❌ Invalid choice. Please try again.')
    
    input('Press Enter to return to main menu...')
    main()  # กลับไปเมนูหลัก

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        display_jobjab_interrupted()
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        display_jobjab_interrupted()
        sys.exit(1) 