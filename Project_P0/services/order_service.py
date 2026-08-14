from dao.order_dao import OrderDao
from dao.cart_dao import cartDao
from dao.product_dao import ProductsDao


class OrderService:

    def __init__(self):
        self.order_dao = OrderDao()
        self.cart_dao = cartDao()
        self.product_dao = ProductsDao()

    def place_order(self, u_id):
        cart_items = self.cart_dao.get_cart(u_id)
        if not cart_items:
            print("Your cart is empty!")
            return

        # Check stock before creating the order
        for item in cart_items:
            p_id = item[1]
            quantity = item[4]
            product = self.product_dao.get_product_by_id(p_id)
            if product is None:
                print("Product no longer exists!")
                return
            stock = product[3]
            if quantity > stock:
                print(f"Insufficient stock for {product[1]}!")
                print(f"Available stock: {stock}")
                print(f"Required quantity: {quantity}")
                return

        # Calculate total
        total_amount = 0
        for item in cart_items:
            total_amount += item[5]

        # Create order
        order_id = self.order_dao.create_order(u_id, total_amount)

        # Create order items and reduce stock
        for item in cart_items:
            p_id = item[1]
            price = item[3]
            quantity = item[4]
            self.order_dao.add_order_item(order_id, p_id, quantity, price)
            self.product_dao.reduce_stock(p_id, quantity)

        # Clear cart
        self.cart_dao.clear_cart(u_id)
        print("Order placed successfully!")
        print(f"Order ID: {order_id}")
        print(f"Total Amount: ₹{total_amount:.2f}")

    def get_order_history(self, u_id):
        orders = self.order_dao.get_order_history(u_id)
        if not orders:
            print("No orders found.")
            return []
        return orders
