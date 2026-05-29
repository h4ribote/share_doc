"""
TornW3B (weav3r.dev) bazaar price mirror.

Fetches the public weav3r marketplace endpoint and writes a slim
Torn/bazaar_prices.json so consumers can read averaged bazaar prices from
this repo (raw) instead of each client calling weav3r directly (which is
rate limited to 100 calls/min by Cloudflare). Same mirror pattern as
script.py / tradable_items.json.

No authentication required (/marketplace is public).

MarketplaceItem schema (weav3r OpenAPI 3.0):
  item_id, item_name, market_price, bazaar_average (nullable),
  lowest_price (nullable), total_bazaars
GET /marketplace -> { total_count, items: [MarketplaceItem], response_time_ms }

Output Torn/bazaar_prices.json:
  {
    "meta": { "source": "...", "generated_utc": "ISO8601", "count": N },
    "items": { "<item_id>": { "name": str, "market": int,
                              "bazaar": int|null, "lowest": int|null,
                              "sellers": int } }
  }
"""

import json
from datetime import datetime, timezone

import requests

ENDPOINT = "https://weav3r.dev/api/marketplace"
OUT_PATH = "Torn/bazaar_prices.json"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


def main() -> None:
    resp = requests.get(
        ENDPOINT,
        headers={"accept": "application/json", "User-Agent": UA},
        timeout=60,
    )
    resp.raise_for_status()
    payload = resp.json()

    items = {}
    for it in payload.get("items", []):
        item_id = it.get("item_id")
        if item_id is None:
            continue

        entry = {
            "name": it.get("item_name"),
            "market": it.get("market_price"),
            "sellers": it.get("total_bazaars", 0),
        }
        if it.get("bazaar_average") is not None:
            entry["bazaar"] = it["bazaar_average"]
        if it.get("lowest_price") is not None:
            entry["lowest"] = it["lowest_price"]

        items[str(item_id)] = entry

    out = {
        "meta": {
            "source": ENDPOINT,
            "generated_utc": datetime.now(timezone.utc).isoformat(),
            "count": len(items),
        },
        "items": items,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(out, ensure_ascii=False, indent=2) + "\n")

    print(f"wrote {OUT_PATH}: {len(items)} items")


if __name__ == "__main__":
    main()
