from services.user_service import UserService
from controller.product_controller import ProductController
from controller.cart_controller import CartController
from controller.orders_controller import OrderController


class UserController:
    def __init__(self):
        self.user_service = UserService()
        self.product_controller = ProductController()
        self.cart_controller = CartController()
        self.order_controller = OrderController()

    def get_details(self):
        username = input("Enter Username: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        self.user_service.register_user(username, password, email)

    def check_user(self):
        email = input("Enter Email: ")
        password = input("Enter password: ")
        user = self.user_service.login_user(email, password)
        if user is None:
            return None
        print(f"Role: {user.role}")
        if user.role == "admin":
            self.admin_menu(user)
        else:
            self.user_menu(user)
        return user

    def admin_menu(self, user):
        print("Admin Logged In")
        while True:
            print("\n===== ADMIN MENU =====")
            print("1.Add Products")
            print("2.View Products")
            print("3.Update Product")
            print("4.Delete Product")
            print("5.Logout")
            inp = int(input())
            if inp == 1:
                self.product_controller.add_product()
            if inp == 2:
                self.product_controller.get_product_details()
            if inp == 3:
                self.product_controller.update_product()
            if inp == 4:
                self.product_controller.delete_product()
            if inp == 5:
                return False

    def user_menu(self, user):
        print("User Logged In")
        while True:
            print("\n===== USER MENU =====")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. Remove Products from Cart")
            print("4. View Cart")
            print("5. Place Order")
            print("6. Order History")
            print("7. Logout")
            inp = int(input())
            if inp == 1:
                self.product_controller.get_product_details()
            elif inp == 2:
                self.cart_controller.add_to_cart(user)
            elif inp == 3:
                self.cart_controller.delete_from_cart(user)
            elif inp == 4:
                self.cart_controller.view_cart(user)
            elif inp == 5:
                self.order_controller.place_order(user)
            elif inp == 6:
                self.order_controller.order_history(user)
            elif inp == 7:
                return False
            else:
                print("Invalid Choice")
