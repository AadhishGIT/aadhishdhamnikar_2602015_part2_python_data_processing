def generate_summary(raw_orders, cleaned_orders, rejected_orders):

    summary = {}

    summary["total_raw_records"] = len(raw_orders)
    summary["total_cleaned_records"] = len(cleaned_orders)
    summary["total_rejected_records"] = len(rejected_orders)

    revenue = 0

    revenue_by_category = {}
    revenue_by_city = {}
    payment_count = {}
    customer_spend = {}
    product_quantity = {}
    rejection_count = {}

    for order in cleaned_orders:

        if order["order_status"] == "Completed":

            amount = float(order["total_amount"])

            revenue += amount

            category = order["category"]
            city = order["city"]

            revenue_by_category[category] = (
                revenue_by_category.get(category, 0) + amount
            )

            revenue_by_city[city] = revenue_by_city.get(city, 0) + amount

        payment = order["payment_method"]

        payment_count[payment] = payment_count.get(payment, 0) + 1

        customer = order["customer_name"]

        customer_spend[customer] = customer_spend.get(customer, 0) + float(
            order["total_amount"]
        )

        product = order["product_name"]

        product_quantity[product] = product_quantity.get(product, 0) + int(
            order["quantity"]
        )

    for record in rejected_orders:

        reasons = record["rejection_reason"].split(",")

        for reason in reasons:

            reason = reason.strip()

            rejection_count[reason] = rejection_count.get(reason, 0) + 1

    summary["total_revenue"] = revenue
    summary["revenue_by_category"] = revenue_by_category
    summary["revenue_by_city"] = revenue_by_city
    summary["payment_count"] = payment_count

    summary["top_customers"] = sorted(
        customer_spend.items(), key=lambda x: x[1], reverse=True
    )[:3]

    summary["highest_quantity_product"] = (
        max(product_quantity, key=product_quantity.get) if product_quantity else "N/A"
    )

    summary["highest_revenue_category"] = (
        max(revenue_by_category, key=revenue_by_category.get)
        if revenue_by_category
        else "N/A"
    )

    summary["rejection_count"] = rejection_count

    # Generate dynamic insights
    most_used_payment = (
        max(payment_count, key=payment_count.get) if payment_count else "N/A"
    )

    summary["business_insights"] = [
        f"Highest revenue category is {summary['highest_revenue_category']}.",
        f"Most preferred payment method is {most_used_payment}.",
        f"Total revenue generated from completed orders is ₹{summary['total_revenue']:.2f}.",
    ]

    return summary
