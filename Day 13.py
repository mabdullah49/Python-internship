import requests
import json

def fetch_api_data(url):
    """Fetch JSON data from the given API URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

def extract_bitcoin_prices(data):
    """Extract currency names and current prices from Bitcoin API data."""
    try:
        bpi = data['bpi']
        prices = {currency: info['rate'] for currency, info in bpi.items()}
        return prices
    except KeyError:
        print("Unexpected JSON structure.")
        return None

def save_report(prices, filename='btc_price_report.txt'):
    """Save formatted price report to a text file."""
    try:
        with open(filename, 'w') as file:
            file.write("\U0001F4CA Bitcoin Price Report\n")
            file.write("--------------------------\n")
            for currency, price in prices.items():
                file.write(f"{currency}: {price}\n")
        print(f"Report saved to {filename}")
    except IOError as e:
        print(f"Failed to write report: {e}")

def filter_json_keys(data, keyword):
    """Filter JSON data keys containing the keyword."""
    matches = {}

    def recursive_search(d, parent_key=''):
        if isinstance(d, dict):
            for k, v in d.items():
                full_key = f"{parent_key}.{k}" if parent_key else k
                if keyword.lower() in k.lower():
                    matches[full_key] = v
                recursive_search(v, full_key)
        elif isinstance(d, list):
            for idx, item in enumerate(d):
                recursive_search(item, f"{parent_key}[{idx}]")

    recursive_search(data)
    return matches

def main():
    default_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    url = input(f"Enter API URL (or press Enter for default): ") or default_url

    data = fetch_api_data(url)
    if not data:
        return

    prices = extract_bitcoin_prices(data)
    if prices:
        save_report(prices)

    keyword = input("Enter a keyword to filter JSON data (or press Enter to skip): ")
    if keyword:
        matches = filter_json_keys(data, keyword)
        print(f"\nFiltered JSON Keys Containing '{keyword}':")
        for k, v in matches.items():
            print(f"{k}: {v}")

if __name__ == "__main__":
    main()
