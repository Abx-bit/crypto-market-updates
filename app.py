import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    parameters = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,ripple,litecoin,cardano",  # Add more cryptocurrencies if needed
        "price_change_percentage": "24h,30d"  # Include 30-day price change percentage
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    return data

def fetch_coin_details(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def display_crypto_data(data):
    print("Cryptocurrency Market Updates:")
    for coin in data:
        name = coin['name']
        symbol = coin['symbol'].upper()
        current_price = coin['current_price']
        market_cap = coin['market_cap']
        volume = coin['total_volume']
        high_24h = coin['high_24h']
        low_24h = coin['low_24h']
        price_change_24h = coin['price_change_percentage_24h']
        price_change_30d = coin.get('price_change_percentage_30d', 'N/A')
        circulating_supply = coin.get('circulating_supply', 'N/A')  # Some coins might not have this field
        all_time_high = coin.get('ath', 'N/A')
        all_time_low = coin.get('atl', 'N/A')
        last_updated = coin.get('last_updated', 'N/A')

        # Calculate price change in USD (absolute value)
        price_change_usd = (current_price - (current_price / (1 + price_change_24h / 100))) if price_change_24h != 0 else 0

        print(f"\n{name} ({symbol}):")
        print(f"  Current Price: ${current_price:.2f}")
        print(f"  Market Cap: ${market_cap:,.2f}")
        print(f"  24h Volume: ${volume:,.2f}")
        print(f"  24h High Price: ${high_24h:,.2f}")
        print(f"  24h Low Price: ${low_24h:,.2f}")
        print(f"  24h Price Change: {price_change_24h:.2f}% (${price_change_usd:.2f})")
        print(f"  30d Price Change: {price_change_30d}")
        print(f"  Circulating Supply: {circulating_supply}")
        print(f"  All-Time High: ${all_time_high}")
        print(f"  All-Time Low: ${all_time_low}")
        print(f"  Last Updated: {last_updated}")

def main():
    crypto_data = fetch_crypto_data()
    display_crypto_data(crypto_data)

if __name__ == "__main__":
    main()
