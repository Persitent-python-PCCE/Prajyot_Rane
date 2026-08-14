from services.order_service import OrderService


def test_place_order_success():
    service = OrderService()
    # Fake cart
    service.cart_dao.get_cart = lambda u_id: [
        (
            1,  # c_id
            3,  # p_id
            "Lenovo LOQ",
            70000,  # price
            2,  # quantity
            140000,  # total
        )
    ]
    # Fake product with enough stock
    service.product_dao.get_product_by_id = lambda p_id: (3, "Lenovo LOQ", 70000, 10)
    # Fake order creation
    service.order_dao.create_order = lambda u_id, total: 100
    order_items = []
    service.order_dao.add_order_item = (
        lambda order_id, p_id, quantity, price: order_items.append(
            (order_id, p_id, quantity, price)
        )
    )
    reduced_stock = []
    service.product_dao.reduce_stock = lambda p_id, quantity: reduced_stock.append(
        (p_id, quantity)
    )
    cleared_cart = []
    service.cart_dao.clear_cart = lambda u_id: cleared_cart.append(u_id)
    service.place_order(1)
    assert order_items == [(100, 3, 2, 70000)]
    assert reduced_stock == [(3, 2)]
    assert cleared_cart == [1]


def test_place_order_empty_cart():
    service = OrderService()
    service.cart_dao.get_cart = lambda u_id: []
    result = service.place_order(1)
    assert result is None


def test_place_order_insufficient_stock():
    service = OrderService()
    # User has 10 units in cart
    service.cart_dao.get_cart = lambda u_id: [(1, 3, "Lenovo LOQ", 70000, 10, 700000)]
    # Only 5 units actually available
    service.product_dao.get_product_by_id = lambda p_id: (3, "Lenovo LOQ", 70000, 5)
    service.place_order(1)
