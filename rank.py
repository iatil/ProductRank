import time
import string
import collections


def process(review: str, products: set, data: dict):
    print("Processing review: ", review)
    # Split into words and clean punctuation marks
    table = str.maketrans("", "", string.punctuation)
    review_list = review.lower().split()
    review_list = [x.translate(table) for x in review_list]
    print(review_list)
    review_set = set(review_list)
    for item in products.intersection(review_list):
        print(item, " -> ", data[item])
        data[item] += 1

    return data


if __name__ == "__main__":
    file = open("products.txt", "r")
    products = file.read().split()
    products = set(item.lower() for item in products)
    print("Product List")
    print(products)
    file.close()


    data = {item.lower(): 0 for item in products}
    print(data)
    file = open("reviews.txt", "r")
    for review in file:
        process(review, products, data)
    file.close()

    print("Final Counts")
    print(data)
    sorted_data = sorted(data.items(), key=lambda kv:(kv[1], kv[0]))[::-1]
    print(sorted_data)
    print("Done")
