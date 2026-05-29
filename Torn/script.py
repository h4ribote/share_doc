import os
import json
import requests

API_KEY = os.environ.get("TORN_API_KEY")

def main():
    headers = {
        'accept': 'application/json',
        'Authorization': f'ApiKey {API_KEY}'
    }
    response = requests.get("https://api.torn.com/v2/torn/items?sort=ASC", headers=headers).json()['items']

    with open("Torn/items.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(response, indent=2) + "\n")
    items = []

    target_types = [
        "Alcohol", "Booster", "Candy", "Drug", "Energy Drink",
        "Enhancer", "Flower", "Medical", "Plushie", "Special", "Supply Pack"
    ]

    for item in response:
        market_price = item.get('value', {}).get('market_price', 0)

        if item.get('is_tradable') and item.get('type') in target_types and market_price > 200:
            new_item = {
                'id': int(item['id']),
                'name': item['name'],
                'type': item['type'],
                'market_price': int(market_price)
            }
            items.append(new_item)

    with open("Torn/tradable_items.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(items, indent=2) + "\n")

if __name__ == "__main__":
    main()
