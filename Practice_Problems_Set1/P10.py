def inventory_report( inventory, gst=0.05, **filters):
    categories=set()
    for item in inventory:
        categories.add(item[1])
    print("Categories:"," ,".join(categories))
    stock=list(filter(lambda quantity : quantity[2]<10 ,inventory))
    print("[!] Reorder soon (stock < 10):",stock)
    price_with_gst=map(lambda item:(item[0],item[3]*(1+0.05)),inventory)
    print(f"Prices incl. GST:",dict(price_with_gst))
    result=inventory
    if "category" in filters:
        result= filter(lambda item:item[0]==filters["category"],inv)
        
    if "max_price" in filters:
        result= filter(lambda item:item[3]==filters["max_price"],inv)

    if "main_stock" in filters:
        result= filter(lambda item:item[2]==filters["main_stock"],inv)

    matches=list(map(lambda item:item[0],result))
    print("Matching Results: ",filters,":",matches)

    

    
inv = [
        ("Masala Chai", "Tea", 5, 20),
        ("Green Tea", "Tea", 15, 30), 
        ("Samosa", "Snack", 8, 15),
        ("Biscuit", "Snack", 25, 10),
        ]
inventory_report(inv, category="Snack",max_price=15)

