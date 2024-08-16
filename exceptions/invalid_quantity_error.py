class InvalidQuantityError(Exception):
    """
    Custom class exception for handle incorrect product quantity
    """

    def __init__(self, message='Quantity must be a positive number greater than zero'):
        self.message = message
        super().__init__(self.message)