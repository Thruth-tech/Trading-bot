"""
Lighter Exchange Market Configuration
Contains market-specific data including decimal precision for accurate order placement
"""

import asyncio
import lighter
import json
import os
from datetime import datetime

class LighterMarketConfig:
    def __init__(self):
        self.markets = {}
        self.config_file = "data/markets.json"
        
    async def fetch_and_save_market_data(self):
        """Fetch market data from Lighter API and save to file"""
        try:
            print("🔄 Fetching market data from Lighter API...")
            
            # Initialize API client
            client = lighter.ApiClient(
                configuration=lighter.Configuration(host="https://mainnet.zklighter.elliot.ai")
            )
            
            order_api = lighter.OrderApi(client)
            
            # Get all order books
            order_books = await order_api.order_books()
            
            if order_books and order_books.order_books:
                markets_data = {}
                
                for market in order_books.order_books:
                    market_id = market.market_id
                    symbol = market.symbol
                    
                    markets_data[market_id] = {
                        "symbol": symbol,
                        "market_id": market_id,
                        "status": market.status,
                        "min_base_amount": market.min_base_amount,
                        "min_quote_amount": market.min_quote_amount,
                        "supported_size_decimals": market.supported_size_decimals,
                        "supported_price_decimals": market.supported_price_decimals,
                        "supported_quote_decimals": market.supported_quote_decimals,
                        "taker_fee": market.taker_fee,
                        "maker_fee": market.maker_fee,
                        "liquidation_fee": market.liquidation_fee,
                        "last_updated": datetime.now().isoformat()
                    }
                    
                    print(f"✅ {symbol} (ID: {market_id}) - Price: {market.supported_price_decimals}dp, Size: {market.supported_size_decimals}dp")
                
                # Save to file
                os.makedirs("data", exist_ok=True)
                with open(self.config_file, 'w') as f:
                    json.dump(markets_data, f, indent=2)
                
                print(f"💾 Saved {len(markets_data)} markets to {self.config_file}")
                self.markets = markets_data
                
            await client.close()
            return True
            
        except Exception as e:
            print(f"❌ Error fetching market data: {e}")
            return False
    
    def load_market_data(self):
        """Load market data from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.markets = json.load(f)
                print(f"📊 Loaded {len(self.markets)} markets from {self.config_file}")
                return True
            else:
                print(f"⚠️  Market config file not found: {self.config_file}")
                return False
        except Exception as e:
            print(f"❌ Error loading market data: {e}")
            return False
    
    def get_market_info(self, market_id):
        """Get market information by market ID"""
        market_id_str = str(market_id)
        if market_id_str in self.markets:
            return self.markets[market_id_str]
        else:
            print(f"⚠️  Market ID {market_id} not found in config")
            return None
    
    def format_price(self, price, market_id):
        """Format price according to market's decimal precision"""
        market_info = self.get_market_info(market_id)
        if market_info:
            decimals = market_info["supported_price_decimals"]
            return round(price, decimals)
        return round(price, 2)  # Default 2 decimals
    
    def format_size(self, size, market_id):
        """Format size according to market's decimal precision"""
        market_info = self.get_market_info(market_id)
        if market_info:
            decimals = market_info["supported_size_decimals"]
            return round(size, decimals)
        return round(size, 4)  # Default 4 decimals
    
    def calculate_base_amount_for_lighter(self, usd_amount, price, market_id):
        """Calculate base amount in Lighter's internal format"""
        market_info = self.get_market_info(market_id)
        if not market_info:
            return int((usd_amount / price) * 10000)  # Default calculation
        
        # Calculate base amount in actual units
        base_amount = usd_amount / price
        
        # Convert to Lighter's internal format (multiply by 10^size_decimals)
        size_decimals = market_info["supported_size_decimals"]
        multiplier = 10 ** size_decimals  # Use only the size decimals
        
        # Don't format first - multiply directly to avoid precision loss
        return int(round(base_amount * multiplier))
    
    def calculate_price_for_lighter(self, price, market_id):
        """Calculate price in Lighter's internal format"""
        market_info = self.get_market_info(market_id)
        if not market_info:
            return int(price * 100)  # Default calculation
        
        # Convert to Lighter's internal format
        price_decimals = market_info["supported_price_decimals"]
        multiplier = 10 ** price_decimals  # Use only the price decimals
        
        # Multiply first, then round to avoid precision loss
        result = price * multiplier
        
        # Round to integer (this is the final format Lighter expects)
        return int(round(result))
    
    def print_market_summary(self):
        """Print summary of all markets"""
        if not self.markets:
            print("❌ No market data loaded")
            return
        
        print("\n📊 Lighter Markets Summary:")
        print("=" * 80)
        print(f"{'ID':<3} {'Symbol':<12} {'Price Dec':<9} {'Size Dec':<8} {'Min Base':<12} {'Min Quote'}")
        print("-" * 80)
        
        for market_id, info in self.markets.items():
            symbol = info["symbol"]
            price_dec = info["supported_price_decimals"]
            size_dec = info["supported_size_decimals"]
            min_base = info["min_base_amount"]
            min_quote = f"${info['min_quote_amount']}"
            
            print(f"{market_id:<3} {symbol:<12} {price_dec:<9} {size_dec:<8} {min_base:<12} {min_quote}")

async def main():
    """Main function to fetch and save market data"""
    config = LighterMarketConfig()
    
    # Try to load existing data first
    if not config.load_market_data():
        print("🔄 No existing data found, fetching from API...")
        await config.fetch_and_save_market_data()
    else:
        # Check if data is older than 1 day
        try:
            with open(config.config_file, 'r') as f:
                data = json.load(f)
            
            # Check first market's timestamp
            first_market = next(iter(data.values()))
            last_updated = datetime.fromisoformat(first_market["last_updated"])
            age_hours = (datetime.now() - last_updated).total_seconds() / 3600
            
            if age_hours > 24:
                print(f"⏰ Data is {age_hours:.1f} hours old, refreshing...")
                await config.fetch_and_save_market_data()
            else:
                print(f"✅ Using cached data ({age_hours:.1f} hours old)")
        except:
            print("🔄 Error checking data age, refreshing...")
            await config.fetch_and_save_market_data()
    
    # Print summary
    config.print_market_summary()

if __name__ == "__main__":
    asyncio.run(main()) 