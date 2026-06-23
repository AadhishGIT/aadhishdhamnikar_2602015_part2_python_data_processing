import csv
from datetime import datetime

VALID_STATUS = ["Completed", "Pending", "Cancelled"]
VALID_PAYMENTS = ["UPI", "Card", "Cash", "NetBanking"]


def standardize_city(city):
    city = city.strip().title()

    city_map = {"Mumbi": "Mumbai", "Bombay": "Mumbai", "Pune ": "Pune"}

    return city_map.get(city, city)


def standardize_status(status):
    status = status.strip().title()
    return status


def standardize_payment(payment):
    payment = payment.strip()
    return payment


def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def clean_orders(orders, products):
    cleaned_orders = []
    rejected_orders = []

    seen_order_ids = set()

    for order in orders:

        reasons = []

        order_id = order["order_id"].strip()

        if order_id in seen_order_ids:
            reasons.append("Duplicate order ID")
        else:
            seen_order_ids.add(order_id)

        customer_name = order["customer_name"].strip()

        if not customer_name:
            reasons.append("Missing customer name")

        city = order["city"].strip()

        if not city:
            reasons.append("Missing city")

        city = standardize_city(city)

        status = standardize_status(order["order_status"])

        if status not in VALID_STATUS:
            reasons.append("Invalid order status")

        payment = standardize_payment(order["payment_method"])

        if payment not in VALID_PAYMENTS:
            reasons.append("Invalid payment method")

        product_id = order["product_id"].strip()

        if product_id not in products:
            reasons.append("Product ID not found")

        try:
            quantity = int(order["quantity"])

            if quantity <= 0:
                reasons.append("Invalid quantity")

        except ValueError:
            reasons.append("Invalid quantity")

        if not validate_date(order["order_date"]):
            reasons.append("Invalid date format")

        if product_id in products:

            expected_price = float(products[product_id]["standard_price"])

        try:
            actual_price = float(order["unit_price"])
        except ValueError:
            reasons.append("Invalid unit price")

            if actual_price != expected_price:
                reasons.append("Unit price mismatch")

        if reasons:

            order["rejection_reason"] = ", ".join(reasons)
            rejected_orders.append(order)

        else:

            product = products[product_id]

            order["city"] = city
            order["customer_name"] = customer_name.title()
            order["order_status"] = status
            order["payment_method"] = payment

            order["product_name"] = product["product_name"]
            order["category"] = product["category"]

            total_amount = quantity * float(order["unit_price"])

            order["total_amount"] = round(total_amount, 2)

            cleaned_orders.append(order)

    write_cleaned_orders(cleaned_orders)
    write_rejected_orders(rejected_orders)

    return cleaned_orders, rejected_orders


def write_cleaned_orders(cleaned_orders):

    if not cleaned_orders:
        return

    fields = [
        "order_id",
        "customer_id",
        "customer_name",
        "city",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "unit_price",
        "total_amount",
        "order_status",
        "payment_method",
        "order_date",
    ]

    with open("outputs/cleaned_orders.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(cleaned_orders)


def write_rejected_orders(rejected_orders):

    if not rejected_orders:
        return

    fields = list(rejected_orders[0].keys())

    with open(
        "outputs/rejected_records.csv", "w", newline="", encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rejected_orders)
