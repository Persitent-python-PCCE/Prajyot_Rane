import csv

with open("sales.csv", "r") as file:
    total = 0
    count = 0
    category_revenue = {}
    max_revenue = 0
    sales = csv.DictReader(file)
    print("=== Sales Report ===")
    print("Revenue by Category:")

    for row in sales:
        revenue = int(row["quantity"]) * int(row["unit_price"])
        category = row["category"]

        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue
        total += revenue
        count += 1
        if revenue > max_revenue:
            max_revenue = revenue
            top_product = row["product"]
for category, revenue in category_revenue.items():
    print(f"{category} : {revenue}")
avg_per_txn = total / count
print(f"Top Product : {top_product} : {max_revenue}")
print(f"Total Revenue: {total}")
print(f"Avg / Txn : {avg_per_txn}")
