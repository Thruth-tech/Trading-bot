"""
Trading Configuration Editor for Lighter Exchange
=================================================

This module provides an interactive configuration editor for trading parameters.
"""

import os
from dotenv import load_dotenv, set_key

def edit_config():
    """Interactive configuration editor"""
    print("\n📝 TRADING CONFIGURATION EDITOR")
    print("=" * 50)
    
    # Load current configuration
    load_dotenv()
    
    # Configuration options
    config_options = {
        "1": ("MARKET_ID", "Market ID to trade", "0"),
        "2": ("TRADE_AMOUNT", "Trade amount per position (USD)", "60.0"),
        "3": ("DESIRED_SPREAD", "Desired spread percentage", "0.0001"),
        "4": ("ADJUSTMENT_THRESHOLD", "Price adjustment threshold", "0.005"),
        "5": ("LEVERAGE", "Leverage multiplier", "10"),
        "6": ("POST_ONLY", "Use POST_ONLY orders", "true"),
        "7": ("MARGIN_MODE", "Margin mode (0=Cross, 1=Isolated)", "0"),
        "8": ("CHECK_INTERVAL", "Check interval (seconds)", "1"),
        "9": ("MAX_PRICE_DEVIATION", "Maximum price deviation", "0.05"),
        "10": ("MIN_QUOTE_BALANCE", "Minimum quote balance", "100")
    }
    
    while True:
        print("\n📋 CONFIGURATION OPTIONS")
        print("-" * 40)
        
        for key, (env_var, description, default) in config_options.items():
            current_value = os.getenv(env_var, default)
            print(f"{key}. {description}")
            print(f"   Current: {current_value}")
        
        print("11. 💾 Save and Exit")
        print("12. ❌ Exit without saving")
        print("-" * 40)
        
        choice = input("👉 Select option to edit (1-12): ").strip()
        
        if choice in config_options:
            env_var, description, default = config_options[choice]
            current_value = os.getenv(env_var, default)
            
            print(f"\n✏️  Editing: {description}")
            print(f"Current value: {current_value}")
            
            new_value = input(f"Enter new value (or press Enter to keep current): ").strip()
            
            if new_value:
                # Validate input based on type
                try:
                    if env_var in ["MARKET_ID", "LEVERAGE", "MARGIN_MODE", "CHECK_INTERVAL"]:
                        int(new_value)
                    elif env_var in ["TRADE_AMOUNT", "DESIRED_SPREAD", "ADJUSTMENT_THRESHOLD", 
                                   "MAX_PRICE_DEVIATION", "MIN_QUOTE_BALANCE"]:
                        float(new_value)
                    elif env_var == "POST_ONLY":
                        if new_value.lower() not in ["true", "false"]:
                            raise ValueError("Must be 'true' or 'false'")
                    
                    # Update environment variable
                    set_key(".env", env_var, new_value)
                    print(f"✅ Updated {env_var} to {new_value}")
                    
                except ValueError as e:
                    print(f"❌ Invalid value: {e}")
            
        elif choice == "11":
            print("\n💾 Configuration saved successfully!")
            break
            
        elif choice == "12":
            print("\n❌ Exiting without saving changes.")
            break
            
        else:
            print("❌ Invalid option. Please try again.")

def show_current_config():
    """Display current configuration"""
    print("\n📋 CURRENT TRADING CONFIGURATION")
    print("=" * 50)
    
    load_dotenv()
    
    config_items = [
        ("MARKET_ID", "Market ID", "0"),
        ("TRADE_AMOUNT", "Trade Amount (USD)", "60.0"),
        ("DESIRED_SPREAD", "Desired Spread", "0.0001"),
        ("ADJUSTMENT_THRESHOLD", "Adjustment Threshold", "0.005"),
        ("LEVERAGE", "Leverage", "10"),
        ("POST_ONLY", "POST_ONLY Orders", "true"),
        ("MARGIN_MODE", "Margin Mode", "0"),
        ("CHECK_INTERVAL", "Check Interval (s)", "1"),
        ("MAX_PRICE_DEVIATION", "Max Price Deviation", "0.05"),
        ("MIN_QUOTE_BALANCE", "Min Quote Balance", "100")
    ]
    
    for env_var, description, default in config_items:
        value = os.getenv(env_var, default)
        print(f"{description:<20}: {value}")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    edit_config() 