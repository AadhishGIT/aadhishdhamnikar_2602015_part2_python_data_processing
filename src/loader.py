import csv


def load_orders(file_path):
    orders = []

    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                orders.append(row)

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return orders


def load_products(file_path):
    products = {}

    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                products[row["product_id"]] = row

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return products