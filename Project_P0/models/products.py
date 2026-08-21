class Product:
    def __init__(self, p_id, p_name, price, stock):
        self.p_id = p_id
        self.p_name = p_name
        self.price = price
        self.stock = stock

    def display_products(self):
        print(f"Product ID: {self.p_id}")
        print(f"Product Name: {self.p_name}")
        print(f"Price: ₹{self.price}")
        print(f"Stock: {self.stock}")
