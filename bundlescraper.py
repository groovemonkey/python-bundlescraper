#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/cloud-computing-books"
tier_dict = {}

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')

# Bundle Tiers
tiers = soup.select(".dd-game-row")


for tier in tiers:
    # Only for sections that have a headline
    if tier.select(".dd-header-headline"):
        # Grab tier name (and price)
        tiername = tier.select(".dd-header-headline")[0].text.strip()
        
        # Grab tier product names
        product_names = tier.select(".dd-image-box-caption")
        product_names = [prodname.text.strip() for prodname in product_names]
        
        # Add one product tier to our datastructure
        tier_dict[tiername] = { "products": product_names }


# After we build our datastructure...
for tiername,tierinfo in tier_dict.items():
    print(tiername)
    print("########################")
    print("\n".join(tierinfo['products']))
    print("\n\n")









# # Old tiers
# tier_headlines = soup.select(".dd-header-headline")
# stripped_tiernames = [tier.text.strip() for tier in tier_headlines]


# # Product Names
# product_names = soup.select(".dd-image-box-caption")
# stripped_product_names = [prodname.text.strip() for prodname in product_names]

## This is the datastructure we'll use to store bundle info
# tiers = {
#     "tier1": {
#         "price": 500,
#         "products": [
#             "name1",
#             "name2"
#         ]
#     },
#     "tier2": {
#         "price": 500,
#         "products": [
#             "name1",
#             "name2"
#         ]
#     }
# }

## Common access pattern
# for tiername,tierinfo in tier_dict.items():
#     print(tiername)
#     print("products:")
#     print(", ".join(tierinfo['products']))
#     print("\n\n")

# - tier1 name and price
#     - product1
#     - product2
# - tier2 name and price
#     - product1
#     - product2
