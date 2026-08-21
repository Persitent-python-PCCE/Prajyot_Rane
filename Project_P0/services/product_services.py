from dao.product_dao import ProductsDao


class Product_services:
    def __init__(self):
        self.product_dao = ProductsDao()

    def add_products(self, p_name, price, stock):
        if not p_name:
            print("Product name cannot be empty.")
            return

        if price <= 0:
            print("Price must be greater than 0.")
            return

        if stock < 0:
            print("Stock cannot be negative.")
            return
        self.product_dao.add_products(p_name, price, stock)

    def get_all_products(self):
        products = self.product_dao.get_all_products()
        if not products:
            print("No Products Available!")
            return []
        return products

    def update_products(self, p_id, p_name, price, stock):
        if p_name == "":
            print("Product Name cannot be empty")
        if price <= 0:
            print("Price cannot be negeative")
        if stock < 0:
            print("Stock cannot be negative")
        result = self.product_dao.update_products(p_id, p_name, price, stock)
        if result == 0:
            print("Products not found!")
        else:
            print("Product updated Successfully!!")

    def get_product_by_id(self, p_id):
        product = self.product_dao.get_product_by_id(p_id)
        if product is None:
            print("Product ID not found.")
            return None
        return product

    def delete_product(self, p_id):
        product = self.product_dao.get_product_by_id(p_id)
        if product is None:
            print("Product ID not found")
            return
        rows_affected = self.product_dao.delete_product(p_id)
        if rows_affected > 0:
            print("Product Deleted Successfully")
