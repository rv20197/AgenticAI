def fetch_sales():
    print("Fetching sales data...")
    return [100, 200, 300]

def filter_valid_orders(sales):
    print("Filtering valid orders...")
    return [sale for sale in sales if sale > 150]

def summarize_sales(valid_sales):
    print("Summarizing sales...")
    return sum(valid_sales)

def generate_report():
    sales = fetch_sales()
    valid_sales = filter_valid_orders(sales)
    total_sales = summarize_sales(valid_sales)
    print(f"Total valid sales: {total_sales}")

generate_report()