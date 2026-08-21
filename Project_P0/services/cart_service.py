from dao.cart_dao import cartDao
from dao.product_dao import ProductsDao


class CartService:
    def __init__(self):
        self.cart_dao = cartDao()
        self.product_dao = ProductsDao()

    def add_to_cart(self, u_id, p_id, quantity):
        product = self.product_dao.get_product_by_id(p_id)
        if product is None:
            print("ProductID not Found")
            return
        if quantity < 0:
            print("Quantity must be greater than 0:")
            return
        stock = product[3]
        if quantity > stock:
            print("Insufficient Stock!!")
            return
        self.cart_dao.add_to_cart(u_id, p_id, quantity)
        self.product_dao.reduce_stock(p_id, quantity)
        print("Product Added Successfully!!")

    def get_cart(self, u_id):
        cart_items = self.cart_dao.get_cart(u_id)
        if not cart_items:
            print("Cart is empty.")
            return []
        return cart_items

    def remove_product_from_cart(self, p_id):
        self.cart_dao.remove_product_from_cart(p_id)
