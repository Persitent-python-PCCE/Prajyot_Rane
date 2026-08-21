from controller.user_controller import UserController
from controller.product_controller import ProductController

user_controller = UserController()
product_controller = ProductController()


def home_menu():
    while True:
        print("\n" + "=" * 50)
        print("            E-COMMERCE STORE")
        print("=" * 50)
        print("  1. Register")
        print("  2. Login")
        print("  3. Exit")
        print("=" * 50)
        try:
            choice = int(input("  Enter your choice: "))
            if choice == 1:
                user_controller.get_details()

            elif choice == 2:
                user_controller.check_user()

            elif choice == 3:
                print("\nThank you for visiting! 👋")
                break

            else:
                print("\n Invalid choice! Please select 1, 2, or 3.")

        except ValueError:
            print("\n Please enter a number.")


home_menu()
