#!/usr/bin/python2

#   General Strategy
#       Iterate over all product price listings
#       Try to find a match
#       If the match is good, add it to the list
#
#   For our purposes we assume the following:
#       Manufacturer is spelled correctly
#       Manufacturer in product listing and product has been normalized
#       It is ok to have an offline algorithm

from functions import load_json, calculate_score, get_related_products

PRODUCT_FILE = "products.txt"
LISTING_FILE = "listings.txt"
THRESHOLD = 0

listings = load_json(LISTING_FILE)
products = load_json(PRODUCT_FILE)

matches = {}

for listing in listings:
    related_products = get_related_products(listing, products)
    potential_matches = [];
    for product in related_products:
        score = calculate_score(listing, product)
        potential_matches.append({"score": score, "product": product})
    if potential_matches:
        best_match = max(potential_matches, key=lambda x: x["score"])
        if best_match["score"] >= THRESHOLD:
            product_name = best_match["product"]["product_name"];
            matches.setdefault(product_name, {}).setdefault("listings", []).append(listing)

#correctly format matches
#results_file = open("result.txt", "w+")
#for key, value in matches.iteritems():
#    results_file.write()
print(matches)
