import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    parameters = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,ripple,litecoin,cardano",  # Add more cryptocurrencies if needed
        "price_change_percentage": "24h"
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    return data

def display_crypto_data(data):
    print("Cryptocurrency Market Updates:")
    for coin in data:
        name = coin['name']
        symbol = coin['symbol'].upper()
        current_price = coin['current_price']
        market_cap = coin['market_cap']
        volume = coin['total_volume']
        price_change_24h = coin['price_change_percentage_24h']

        print(f"\n{name} ({symbol}):")
        print(f"  Current Price: ${current_price:.2f}")
        print(f"  Market Cap: ${market_cap:,.2f}")
        print(f"  24h Volume: ${volume:,.2f}")
        print(f"  24h Price Change: {price_change_24h:.2f}%")

def main():
    crypto_data = fetch_crypto_data()
    display_crypto_data(crypto_data)

if __name__ == "__main__":
    main()
