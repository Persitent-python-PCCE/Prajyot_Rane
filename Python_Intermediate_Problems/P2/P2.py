import yaml
from datetime import timedelta
from datetime import datetime
import json
import random

data = []
order_count = int(input("Enter number of Orders: "))
list_total_amount = []
delivery_count = 0
cancelled_count = 0
with open("config.yml", "r") as file:
    config_load = yaml.safe_load(file)

start_range = datetime(2026, 1, 1, 0, 0)
end_range = datetime(2027, 1, 1, 0, 0)


def random_date(start_date, end_date):
    end_date = end_date.date()
    start_date = start_date.date()
    delta = end_date - start_date
    random_days = random.randrange(delta.days + 1)
    return start_date + timedelta(days=random_days)


product_list = ["Laptop", "Mobile Phone", "Monitor", "Keyboard", "Mouse", "Headphones"]
for i in range(0, order_count):
    products = {}
    order_id = random.randint(0 + i, 1000)
    customer_id = random.randint(1000, 9999)
    product = random.choice(product_list)
    quantity = random.randint(1, 5)
    unit_price = random.uniform(100, 1000)
    total_amount = quantity * unit_price
    list_total_amount.append(total_amount)
    status = random.choice(config_load["allowed_statuses"])
    r_date = random_date(start_range, end_range)
    products["order_id"] = order_id
    products["customer_id"] = customer_id
    products["product"] = product
    products["quantity"] = quantity
    products["unit_price"] = unit_price
    products["total_amount"] = total_amount
    products["status"] = status
    if status == "Delivered":
        delivery_count += 1
    if status == "Cancelled":
        cancelled_count += 1

    products["order_date"] = r_date.isoformat()
    data.append(products)
with open("SampleOrders.json", "w") as file:
    json.dump(data, file, indent=4)

highest_order = max(list_total_amount)
lowest_order = min(list_total_amount)

print("==================================")
print("TechStore Order Report")
print("==================================")
print(f"Total Orders :{order_count}")
print(f"Total Sales : INR {total_amount:,.2f}")
print(f"Highest Order : INR {highest_order:,.2f}")
print(f"Lowest Order : INR {lowest_order}")
print(f"Delivered Orders : {delivery_count}")
print(f"Cancelled Orders : {cancelled_count}")
print("Order data saved successfully.")
