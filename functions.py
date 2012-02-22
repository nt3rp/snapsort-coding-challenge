def load_json(filename):
    import json
    results = []
    my_file = open(filename, "r")
    for line in my_file.readlines():
        results.append(json.loads(line))
    my_file.close()
    return results
    
def get_related_products(listing, products):
    return filter(lambda x: x["manufacturer"] == listing["manufacturer"], products)

#Should probably alter this; I am sure that certain qualities have more weight
#Also, need to be more rigourous than just seeing if the name is part of the listing title
def calculate_score(listing, product):
    score = 0
    if (product.get("product_name") and product["product_name"] in listing["title"]):
        score += 1
    
    if (product.get("manufacturer") and product["manufacturer"] in listing["title"]):
        score += 1
    
    if (product.get("family") and product["family"] in listing["title"]):
        score += 1
        
    if (product.get("model") and product["model"] in listing["title"]):
        score += 1
    
    return score
