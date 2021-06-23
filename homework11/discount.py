from typing import Callable, Union


def morning_discount(order: "Order") -> None:
    """Sets to the given instance attribute 'discount'
    with the percent of morning discount (50%).
    :param order: instance of Order that should use morning discount
    programm when it calculates final price
    :type order: instance of Order
    """
    setattr(order, "discount", 0.5)


def elder_discount(order: "Order") -> None:
    """Sets to the given instance attribute 'discount'
    with the percent of elder discount (90%).
    :param order: instance of Order that should use elder discount
    programm when it calculates final price
    :type order: instance of Order
    """
    setattr(order, "discount", 0.9)


def without_discount(order: "Order") -> None:
    """Default discount programm that sets to the given
    instance attribute 'discount' without any discount (0%).
    :param order: instance of Order that shouldn't use discount
    programm when it calculates final price
    :type order: instance of Order
    """
    setattr(order, "discount", 0)


class Order:
    """Class of orders which can use different discount
    programms to calculate final price of the order.

    :param price: initial price of the order
    :type price: int or float
    :param discount: function that set attribute 'discount'
    with percent of discount programm. By default there
    isn't any discount
    :type discont: func
    """

    def __init__(
        self, price: Union[int, float], discount: Callable = without_discount
    ) -> None:
        self.price = price
        discount(self)

    def final_price(self):
        """Returns final price of the order considering
        discount programm.
        """
        return self.price - self.price * self.discount
