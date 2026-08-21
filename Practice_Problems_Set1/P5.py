orders=[("Masala Chai", 3, 20),
("Samosa", 2,15),
("Green Tea", 1, 30)]

bill=list(map(lambda item: item[1]*item[2]*1.05,orders))
print("Line totals (incl. GST): [",list(bill),"]")
total=sum(bill)
print(f"Grand Total: {total:.2f}")