def write_summary_report(summary, file_path):

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("BUSINESS SUMMARY REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write(f"Total Raw Records: {summary['total_raw_records']}\n")

        file.write(f"Total Cleaned Records: {summary['total_cleaned_records']}\n")

        file.write(f"Total Rejected Records: {summary['total_rejected_records']}\n")

        file.write(f"Total Revenue: {summary['total_revenue']}\n\n")

        file.write("Revenue By Category\n")

        for k, v in summary["revenue_by_category"].items():
            file.write(f"{k}: {v}\n")

        file.write("\nRevenue By City\n")

        for k, v in summary["revenue_by_city"].items():
            file.write(f"{k}: {v}\n")

        file.write("\nOrders By Payment Method\n")

        for k, v in summary["payment_count"].items():
            file.write(f"{k}: {v}\n")

        file.write("\nTop 3 Customers\n")

        for customer, spend in summary["top_customers"]:
            file.write(f"{customer}: {spend}\n")

        file.write(
            f"\nHighest Quantity Product: " f"{summary['highest_quantity_product']}\n"
        )

        file.write(
            f"Highest Revenue Category: " f"{summary['highest_revenue_category']}\n"
        )

        file.write("\nRejected Records By Reason\n")

        for k, v in summary["rejection_count"].items():
            file.write(f"{k}: {v}\n")

        file.write("\nBusiness Insights\n")

        for index, insight in enumerate(summary["business_insights"], start=1):
            file.write(f"{index}. {insight}\n")
