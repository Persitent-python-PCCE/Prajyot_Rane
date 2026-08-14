from services.product_services import Product_services


class ProductController:
    def __init__(self):
        self.product_service = Product_services()

    def add_product(self):
        p_name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        self.product_service.add_products(p_name, price, stock)
        print("Product Added Sucessfully")

    def get_product_details(self):
        products = self.product_service.get_all_products()
        if not products:
            return
        print("\n----- PRODUCTS -----")
        for p in products:
            print(
                f"ID: {p[0]} | "
                f"Name: {p[1]}        | "
                f"Price: ₹{p[2]} | "
                f"Stock: {p[3]}"
            )

    def update_product(self):
        p_id = int(input("Enter product ID to update: "))
        product = self.product_service.get_product_by_id(p_id)
        if product is None:
            return
        p_name = input("Enter new product name: ")
        price = float(input("Enter new price: "))
        stock = int(input("Enter new stock: "))
        self.product_service.update_products(p_id, p_name, price, stock)

    def delete_product(self):
        self.get_product_details()
        p_id = int(input("Enter productID of Product you want to delete: "))
        product = self.product_service.delete_product(p_id)
        print("Product deleted successfully!!")
