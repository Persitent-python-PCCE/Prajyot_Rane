from services.cart_service import CartService


def test_add_to_cart_success():

    service = CartService()

    # Fake product returned by ProductDao
    service.product_dao.get_product_by_id = lambda p_id: (3, "Lenovo LOQ", 70000, 10)

    added_item = []

    # Fake CartDao
    def fake_add_to_cart(u_id, p_id, quantity):
        added_item.append((u_id, p_id, quantity))

    service.cart_dao.add_to_cart = fake_add_to_cart

    service.add_to_cart(6, 3, 2)

    assert added_item == [(6, 3, 2)]


def test_add_to_cart_product_not_found():
    service = CartService()
    service.product_dao.get_product_by_id = lambda p_id: None
    result = service.add_to_cart(6, 99, 2)
    assert result is None
