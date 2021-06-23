from homework11.discount import Order, elder_discount, morning_discount


def test_order_with_morning_discount():
    order = Order(100, morning_discount)
    assert order.discount == 0.5
    assert order.final_price() == 50


def test_order_with_elder_discount():
    order = Order(100, elder_discount)
    assert order.discount == 0.9
    assert order.final_price() == 10


def test_order_without_discount():
    order = Order(100)
    assert order.discount == 0
    assert order.final_price() == 100
