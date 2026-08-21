from services.cart_service import CartService


class CartController:
    def __init__(self):
        self.cart_service = CartService()

    def add_to_cart(self, user):
        p_id = int(input("Enter ProductID :"))
        quantity = int(input("Enter Quantity:"))
        self.cart_service.add_to_cart(user.u_id, p_id, quantity)

    def view_cart(self, user):
        cart_items = self.cart_service.get_cart(user.u_id)
        if not cart_items:
            return
        print("\n===== YOUR CART =====")
        grand_total = 0
        for item in cart_items:
            print(
                f"ID: {item[0]} | "
                f"Product: {item[2]} | "
                f"ProductID:{item[1]}  |"
                f"Price: ₹{item[3]:.2f} | "
                f"Quantity: {item[4]} | "
                f"Total: ₹{item[5]:.2f}"
            )
        grand_total += item[5]

        print("-----------------------------")
        print(f"Grand Total: ₹{grand_total:.2f}")

    def delete_from_cart(self, user):
        self.view_cart(user)
        p_id = input("Enter Product ID to remvoe from cart:")
        self.cart_service.remove_product_from_cart(p_id)
