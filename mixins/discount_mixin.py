from discounts.discount import Discount


class DiscountMixin:
    """
    A mixin class that provides the functionality to apply discounts to product in a shopping cart.

    Attributes:
        items (dict): A dictionary where the keys are Product instances and the values are their corresponding quantities.

    Methods:
        apply_discount(discount: Discount):
            Applies the given discount to all product in the cart by adjusting their prices accordingly.
    """

    def __init__(self):
        self.items = None

    def apply_discount(self, discount: Discount):
        for product in self.items.keys():
            product.price = discount.apply(product.price)
