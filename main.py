from src.loader import load_orders, load_products
from src.cleaner import clean_orders
from src.analyzer import generate_summary
from src.reporter import write_summary_report


def main():
    print("Loading data...")

    orders = load_orders("data/raw_orders.csv")
    products = load_products("data/product_master.csv")

    print(f"Loaded {len(orders)} orders")
    print(f"Loaded {len(products)} products")

    cleaned_orders, rejected_orders = clean_orders(
        orders,
        products
    )

    summary = generate_summary(
        orders,
        cleaned_orders,
        rejected_orders
    )

    write_summary_report(
        summary,
        "outputs/summary_report.txt"
    )

    print("Processing completed successfully")
    print(f"Cleaned Records: {len(cleaned_orders)}")
    print(f"Rejected Records: {len(rejected_orders)}")


if __name__ == "__main__":
    main()