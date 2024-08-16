from exceptions.invalid_price_error import InvalidPriceError
from mixins.loggining_mixin import LoggingMixin


class Product(LoggingMixin):
    """
    Class for product representation
    """

    def __init__(self, name: str, price: int | float, description: str):
        super().__init__()

        if not isinstance(price, int | float):
            raise TypeError('Price must be a number')
        if price <= 0:
            raise InvalidPriceError(f'Invalid price for {name}: {price}')

        self.name = name
        self.price = price
        self.description = description

        self.log(f'Created product: {self.name}, price: {self.price}')

    def __str__(self):
        return f'Product: name:{self.name},price: {self.price},description: {self.description}'
