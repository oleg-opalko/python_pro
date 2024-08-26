from exceptions.invalid_quantity_error import InvalidQuantityError
from mixins.discount_mixin import DiscountMixin
from mixins.loggining_mixin import LoggingMixin
from payment_processors.payment_processor import PaymentProcessor
from product.product import Product


class Cart(LoggingMixin, DiscountMixin):
    """
    Class for cart representation
    """

    def __init__(self):
        LoggingMixin.__init__(self)
        self.items = {}

    def __len__(self):
        return len(self.items)

    def __getitem__(self, item):
        return list(self.items.items())[item]

    def __iadd__(self, other_card):
        if not isinstance(other_card, Cart):
            raise TypeError('Need add another Card')

        for product, quantity in other_card.items.items():
            self.items[product] = self.items.get(product, 0) + quantity

        self.log('Merged another cart in one')

        return self

    def add_product(self, product: Product, quantity: int | float):
        if not isinstance(quantity, int | float):
            raise TypeError('Quantity must be a number')
        if quantity <= 0:
            raise InvalidQuantityError(f'Invalid quantity for {product.name}')
        self.items[product] = self.items.get(product, 0) + quantity
        self.log(f'Added {quantity} of {product.name} to the card')

    def total_cost(self):
        total_cost = sum(product.price * quantity for product, quantity in self.items.items())
        self.log(f'Total cost: {total_cost}')
        return total_cost

    def pay(self, paymentProcessor: PaymentProcessor):
        total_sum = self.total_cost()
        paymentProcessor.pay(total_sum)

        self.log(f'Payment of {total_sum} made using {type(paymentProcessor).__name__}')

    def __str__(self):
        cart_content = '\n'.join([f"{product.name}: {quantity} x ${product.price}" for product, quantity
                                  in self.items.items()])
        return f'Card: \n{cart_content}\n'
