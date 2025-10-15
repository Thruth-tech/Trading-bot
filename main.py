#!/usr/bin/env python3

"""
Lighter Exchange Trading Bot - Protected Version
===============================================

This software contains protected trading algorithms.
For commercial use only.
"""

import os
import sys
import asyncio
import json
from datetime import datetime
from dotenv import load_dotenv

# Add display_banner to path
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

# Load environment variables
load_dotenv()

def print_main_menu():
    """Print main menu options"""
    display_jobjab_header('LIGHTER EXCHANGE BOT')
    print("1. 🤖 Trading Bot")
    print("2. 📊 Market Data")
    print("3. 🔑 Setup API Key")
    print("4. ❌ Exit")
    print("-" * 40)

def print_trading_menu():
    """Print trading submenu"""
    display_jobjab_header('TRADING BOT')
    print("1. 🔄 Start Liquidity Provider Bot")
    print("2. 📝 Edit Trading Config")
    print("3. 🔙 Back to Main Menu")
    print("-" * 40)

def print_market_data_menu():
    """Print market data submenu"""
    display_jobjab_header('MARKET DATA')
    print("1. 📊 View All Markets")
    print("2. 🔍 Search Market by Symbol")
    print("3. 🔄 Update Market Data")
    print("4. 🔙 Back to Main Menu")
    print("-" * 40)

def load_market_data():
    """Load market data from JSON file"""
    try:
        with open('data/markets.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Market data file not found. Please update market data first.")
        return {}
    except json.JSONDecodeError:
        print("❌ Invalid market data file format.")
        return {}

def show_all_markets():
    """Display all available markets"""
    markets = load_market_data()
    
    if not markets:
        print("❌ No market data available.")
        return
    
    print(f"\n📊 Available Markets ({len(markets)} total)")
    print("=" * 80)
    print(f"{'ID':<4} {'Symbol':<12} {'Status':<8} {'Min Amount':<12} {'Decimals':<10} {'Last Updated':<20}")
    print("-" * 80)
    
    # Sort by market_id
    sorted_markets = sorted(markets.items(), key=lambda x: int(x[0]))
    
    for market_id, data in sorted_markets:
        symbol = data.get('symbol', 'N/A')
        status = data.get('status', 'N/A')
        min_base = data.get('min_base_amount', 'N/A')
        size_decimals = data.get('supported_size_decimals', 'N/A')
        last_updated = data.get('last_updated', 'N/A')
        
        # Format last updated
        if last_updated != 'N/A':
            try:
                dt = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
                last_updated = dt.strftime('%Y-%m-%d %H:%M')
            except:
                pass
        
        print(f"{market_id:<4} {symbol:<12} {status:<8} {min_base:<12} {size_decimals:<10} {last_updated:<20}")
    
    print("-" * 80)

def search_market_by_symbol():
    """Search for specific market by symbol"""
    markets = load_market_data()
    
    if not markets:
        print("❌ No market data available.")
        return
    
    symbol = input("\n🔍 Enter symbol to search (e.g., BTC, ETH): ").strip().upper()
    
    found_markets = []
    for market_id, data in markets.items():
        if symbol in data.get('symbol', '').upper():
            found_markets.append((market_id, data))
    
    if not found_markets:
        print(f"❌ No markets found for symbol: {symbol}")
        return
    
    print(f"\n🎯 Found {len(found_markets)} market(s) for '{symbol}'")
    print("=" * 100)
    
    for market_id, data in found_markets:
        print(f"\n📊 Market ID: {market_id}")
        print(f"   Symbol: {data.get('symbol', 'N/A')}")
        print(f"   Status: {data.get('status', 'N/A')}")
        print(f"   Min Base Amount: {data.get('min_base_amount', 'N/A')}")
        print(f"   Min Quote Amount: {data.get('min_quote_amount', 'N/A')}")
        print(f"   Size Decimals: {data.get('supported_size_decimals', 'N/A')}")
        print(f"   Price Decimals: {data.get('supported_price_decimals', 'N/A')}")
        print(f"   Quote Decimals: {data.get('supported_quote_decimals', 'N/A')}")
        print(f"   Taker Fee: {data.get('taker_fee', 'N/A')}")
        print(f"   Maker Fee: {data.get('maker_fee', 'N/A')}")
        print(f"   Liquidation Fee: {data.get('liquidation_fee', 'N/A')}")
        print(f"   Last Updated: {data.get('last_updated', 'N/A')}")
        print("-" * 50)

async def update_market_data():
    """Update market data from API"""
    print("\n🔄 Updating market data from Lighter API...")
    
    try:
        from data.market_config import LighterMarketConfig
        
        market_config = LighterMarketConfig()
        await market_config.fetch_and_save_market_data()
        
        print("✅ Market data updated successfully!")
        
    except Exception as e:
        print(f"❌ Error updating market data: {e}")

def update_env_value(key, value):
    """Update .env file value directly to avoid quote escaping"""
    try:
        # Read current .env file
        with open('.env', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Find and update the line
        updated = False
        for i, line in enumerate(lines):
            if line.strip().startswith(f"{key}="):
                lines[i] = f"{key}={value}\n"
                updated = True
                break
        
        # If key not found, add it
        if not updated:
            lines.append(f"{key}={value}\n")
        
        # Write back to file
        with open('.env', 'w', encoding='utf-8') as f:
            f.writelines(lines)
            
    except Exception as e:
        print(f"❌ Error updating .env file: {e}")

def setup_api_key():
    """Setup API key configuration"""
    print("\n🔑 API KEY SETUP")
    print("=" * 50)
    
    # Load current configuration
    load_dotenv()
    
    print("\n📋 Current API Configuration:")
    current_private_key = os.getenv('LIGHTER_API_KEY_PRIVATE_KEY', '')
    current_wallet = os.getenv('WALLET_ADDRESS', '')
    current_index = os.getenv('API_KEY_INDEX', '0')
    
    print(f"Private Key: {'*' * 20 if current_private_key else 'Not set'}")
    print(f"Wallet Address: {current_wallet if current_wallet else 'Not set'}")
    print(f"API Key Index: {current_index}")
    
    print("\n🔧 Setup Options:")
    print("1. Set API Private Key")
    print("2. Set Wallet Address") 
    print("3. Set API Key Index")
    print("4. View Current Config")
    print("5. Back to Main Menu")
    print("-" * 40)
    
    while True:
        choice = input("👉 Select option (1-5): ").strip()
        
        if choice == "1":
            print("\n🔑 Enter API Private Key:")
            print("(This should be the private key from Lighter setup, NOT your ETH private key)")
            new_key = input("API Private Key: ").strip()
            if new_key:
                # Basic validation
                if len(new_key) < 32:
                    print("❌ Invalid key length. Please check your key.")
                else:
                    # Update .env file directly to avoid quote escaping
                    update_env_value("LIGHTER_API_KEY_PRIVATE_KEY", f"'{new_key}'")
                    print("✅ API Private Key updated successfully!")
            
        elif choice == "2":
            print("\n👛 Enter Wallet Address:")
            new_wallet = input("Wallet Address (0x...): ").strip()
            if new_wallet:
                # Basic validation
                if not new_wallet.startswith('0x') or len(new_wallet) != 42:
                    print("❌ Invalid wallet address format. Should be 0x followed by 40 characters.")
                else:
                    # Update without quotes for wallet address
                    update_env_value("WALLET_ADDRESS", new_wallet)
                    print("✅ Wallet Address updated successfully!")
            
        elif choice == "3":
            print("\n🔢 Enter API Key Index:")
            print("Usually 0, 1, or 2")
            new_index = input("API Key Index: ").strip()
            if new_index:
                try:
                    int(new_index)  # Validate it's a number
                    # Update without quotes for API key index
                    update_env_value("API_KEY_INDEX", new_index)
                    print("✅ API Key Index updated successfully!")
                except ValueError:
                    print("❌ Invalid index. Please enter a number.")
            
        elif choice == "4":
            # Reload and show current config
            load_dotenv()
            print(f"\n📋 Current Configuration:")
            print(f"Private Key: {'*' * 20 if os.getenv('LIGHTER_API_KEY_PRIVATE_KEY') else 'Not set'}")
            print(f"Wallet: {os.getenv('WALLET_ADDRESS', 'Not set')}")
            print(f"Index: {os.getenv('API_KEY_INDEX', 'Not set')}")
            
        elif choice == "5":
            break
            
        else:
            print("❌ Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")

async def handle_trading_menu():
    """Handle trading menu selections"""
    while True:
        print_trading_menu()
        choice = input("👉 Select option (1-3): ").strip()
        
        if choice == "1":
            print("\n🔄 Starting Liquidity Provider Bot...")
            try:
                # Import the protected trading bot from bytecode
                import importlib.util
                import glob
                
                # Find the bytecode file
                bytecode_pattern = os.path.join("trading", "__pycache__", "lighter_bot.cpython-*.pyc")
                bytecode_files = glob.glob(bytecode_pattern)
                
                if not bytecode_files:
                    raise ImportError("Protected trading module not found")
                
                # Load module from bytecode
                spec = importlib.util.spec_from_file_location("lighter_bot", bytecode_files[0])
                lighter_bot_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(lighter_bot_module)
                
                # Get the class
                LighterLiquidityBot = lighter_bot_module.LighterLiquidityBot
                bot = LighterLiquidityBot()
                print("✅ Trading bot loaded successfully")
                await bot.run()
            except KeyboardInterrupt:
                print("\n🛑 Bot stopped by user")
            except Exception as e:
                print(f"❌ Error starting bot: {e}")
                input("Press Enter to continue...")
        
        elif choice == "2":
            print("\n📝 Opening Trading Configuration...")
            try:
                from trading.config_editor import edit_config
                edit_config()
            except Exception as e:
                print(f"❌ Error editing config: {e}")
                input("Press Enter to continue...")
        
        elif choice == "3":
            break
        
        else:
            print("❌ Invalid option. Please try again.")
            input("Press Enter to continue...")

async def handle_market_data_menu():
    """Handle market data menu selections"""
    while True:
        print_market_data_menu()
        choice = input("👉 Select option (1-4): ").strip()
        
        if choice == "1":
            print("\n📊 Loading All Markets...")
            try:
                show_all_markets()
            except Exception as e:
                print(f"❌ Error loading markets: {e}")
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            print("\n🔍 Search Market by Symbol...")
            try:
                search_market_by_symbol()
            except Exception as e:
                print(f"❌ Error searching market: {e}")
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            try:
                await update_market_data()
            except Exception as e:
                print(f"❌ Error updating market data: {e}")
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            break
        
        else:
            print("❌ Invalid option. Please try again.")
            input("Press Enter to continue...")

async def main():
    """Main application loop"""
    
    # Show JOBJAB banner
    display_jobjab_banner(wait_for_enter=False)
    
    print("\n🚀 LIGHTER TRADING BOT - PROTECTED VERSION")
    print("="*50)
    print("✅ Bot initialized successfully!")
    print("="*50)
    
    input("\nPress Enter to continue to main menu...")
    
    # Main application loop
    while True:
        print_main_menu()
        choice = input("👉 Select option (1-4): ").strip()
        
        if choice == "1":
            await handle_trading_menu()
        
        elif choice == "2":
            await handle_market_data_menu()
        
        elif choice == "3":
            try:
                setup_api_key()
            except Exception as e:
                print(f"❌ Error in API setup: {e}")
                input("Press Enter to continue...")
        
        elif choice == "4":
            display_jobjab_goodbye()
            break
        
        else:
            print("❌ Invalid option. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        display_jobjab_interrupted()
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Critical application error: {e}")
        print("Please check your configuration and try again.")
        display_jobjab_interrupted()
        sys.exit(1) 