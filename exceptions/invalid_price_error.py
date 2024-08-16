class InvalidPriceError(Exception):
    """
    Custom class exception for handle incorrect product price
    """

    def __init__(self, price, message='Price must be a positive number greater than zero'):
        super().__init__(message)
        self.price = price
        self.message = message

    def __str__(self):
        return f'Price {self.price} is invalid: {self.message}'
