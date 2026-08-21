from services.order_service import OrderService


class OrderController:
    def __init__(self):
        self.order_service = OrderService()

    def place_order(self, user):
        self.order_service.place_order(user.u_id)

    def order_history(self, user):
        orders = self.order_service.get_order_history(user.u_id)
        if not orders:
            return
        print("\n===== ORDER HISTORY =====")
        current_order = None
        for order in orders:
            if current_order != order[0]:
                current_order = order[0]
                print("\n-----------------------------")
                print(f"Order ID: {order[0]}")
                print(f"Order Date: {order[1]}")
                print(f"Order Total: ₹{order[2]:.2f}")
                print("-----------------------------")
            print(
                f"Product: {order[4]} | "
                f"Quantity: {order[5]} | "
                f"Price: ₹{order[6]:.2f} | "
                f"Item Total: ₹{order[7]:.2f}"
            )
