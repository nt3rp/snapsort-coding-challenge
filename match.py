#!/usr/bin/python2
import json
from operator import attrgetter

PRODUCT_FILE = "products-subset.txt"
LISTING_FILE = "listings-subset.txt"
THRESHOLD = 4

def load_json(filename):
    results = []
    my_file = open(filename, "r")
    for line in my_file.readlines():
        results.append(json.loads(line))
    my_file.close()
    return results
    
def get_related_products(listing, products):
    return filter(lambda x: x["manufacturer"] == listing["manufacturer"], products)
    
def likelihood(listing, product):
    return 1
    

listings = load_json(LISTING_FILE)
products = load_json(PRODUCT_FILE)

my_matches = []

for listing in listings:
    related_products = get_related_products(listing, products)
    scores = [];
    for product in related_products:
        score = likelihood(listing, product)
        scores.append({"score": score, "product": product})
    if scores:
        max_score = max(scores, key=lambda x: x["score"])
        print(max_score)
        if max_score >= THRESHOLD:
            my_matches.append({"product_name": max_score["product"]["product_name"], "listing": listing})

print(my_matches)
