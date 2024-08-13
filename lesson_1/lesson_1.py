import datetime
import logging


class PaymentProcessor:
    def pay(self, amount):
        """
        Base method for pay items
        :param amount:
        :return:
        """
        pass


class CreditCardProcessor(PaymentProcessor):
    """
    Processor for handling credit card payments.
    """

    def __init__(self, cardNumber: str, credit_card_holder: str, cvv: int, expiry_date: str):
        self.cardNumber = cardNumber
        self.credit_card_holder = credit_card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount):
        """
        Process the payment using credit card.
        :param amount: The amount to be paid.
        :return: None
        """
        print(f'Paid: {amount:.2f} using credit card')

    def __str__(self):
        return f'{self.cardNumber}, {self.credit_card_holder}, {self.expiry_date}'


class PayPalProcessor(PaymentProcessor):
    """
     Processor for handling PayPal payments.
    """

    def __init__(self, email: str):
        self.email = email

    def pay(self, amount):
        """
        Process the payment using PayPal.
        :param amount: The amount to be paid.
        :return: None
        """
        print(f'Paid: {amount:.2f} using pay pal')

    def __str__(self):
        return f'PayPal Account: {self.email}'


class BankTransferProcessor(PaymentProcessor):
    """
    Processor for handling bank transfer payments.
    """

    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder

    def __str__(self):
        return f'{self.account_number} - {self.account_holder}'

    def pay(self, amount):
        """
        Process the payment using bank transfer.
        :param amount: The amount to be paid.
        :return: None
        """
        print(f'Paid: {amount:.2f} using bank transfer from account {self.account_number}')


class Discount:
    def apply(self, price):
        pass


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, price) -> float:
        """
        Calculate total amount with percentage discount
        :param price: int | float
        :return: int | float
        """
        return price * (1 - self.percentage / 100)


class FixedAmountDiscount(Discount):
    def __init__(self, fixed_amount):
        self.fixed_amount = fixed_amount

    def apply(self, price: int | float) -> float:
        """
        Calculate total amount with fixed amount discount
        :param price:
        :return:
        """
        return price - self.fixed_amount


class InvalidPriceError(Exception):
    """
    Custom class exception for handle incorrect product price
    """

    def __init__(self, message='Price must be a positive number greater than zero'):
        self.message = message
        super().__init__(self.message)


class InvalidQuantityError(Exception):
    """
    Custom class exception for handle incorrect product quantity
    """

    def __init__(self, message='Quantity must be a positive number greater than zero'):
        self.message = message
        super().__init__(self.message)


class LoggingMixin:
    import datetime

    """
    A mixin for logging basic actions in classes.
    """

    def __init__(self):
        self.logger = logging.getLogger(f'{type(self).__name__}')
        self.logger.setLevel(logging.DEBUG)

        c_handler = logging.StreamHandler()
        time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        log_format = f'[{time}] - %(message)s'

        c_format = logging.Formatter(log_format)

        c_handler.setFormatter(c_format)
        self.logger.addHandler(c_handler)

    def log(self, message: str):
        """
        Logs a message with the event time added.
        :param message: Log message text
        :return: None
        """
        self.logger.debug(message)


class Product(LoggingMixin):
    """
    Class for product representation
    """

    def __init__(self, name: str, price: int | float, description: str):
        super().__init__()
        if price <= 0:
            raise InvalidPriceError(f'Invalid price for {name}: {price}')
        self.name = name
        self.price = price
        self.description = description

        self.log(f'Created product: {self.name}, price: {self.price}')

    def __str__(self):
        return f'Product: name:{self.name},price: {self.price},description: {self.description}'


class DiscountMixin:
    """
    A mixin class that provides the functionality to apply discounts to products in a shopping cart.

    Attributes:
        items (dict): A dictionary where the keys are Product instances and the values are their corresponding quantities.

    Methods:
        apply_discount(discount: Discount):
            Applies the given discount to all products in the cart by adjusting their prices accordingly.
    """

    def __init__(self):
        self.items = None

    def apply_discount(self, discount: Discount):
        for product in self.items.keys():
            product.price = discount.apply(product.price)


class Cart(LoggingMixin, DiscountMixin):
    """
    Class for cart representation
    """

    def __init__(self):
        super().__init__()
        self.items = {}

    def add_product(self, product: Product, quantity: int | float):
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


def main():
    cart = Cart()

    # Created test products
    try:
        product1 = Product("Laptop", 1500.00, "A high-end gaming laptop")
        product2 = Product("Mouse", 50.00, "A wireless mouse")
        product3 = Product("Keyboard", 100.00, "A mechanical keyboard")
        # product4 = Product("Headphones", -10.00, "Noise-cancelling headphones")
        # product5 = Product("Monitor", 0, "4K monitor")

        cart.add_product(product1, 1)
        cart.add_product(product2, 2)
        cart.add_product(product3, 3)
        # cart.add_product(product4, -1)
        # cart.add_product(product5, 3)

        print(cart)
        print(f'Total cost:{cart.total_cost()} $')

        # Applying different types of discounts
        percentage_discount = PercentageDiscount(10)
        fixed_amount_discount = FixedAmountDiscount(20)

        cart.apply_discount(percentage_discount)
        cart.log('Applied percentage discount to the cart')

        print(cart)
        print(f'Total cost after percentage discount: {cart.total_cost()} $')

        cart.apply_discount(fixed_amount_discount)
        cart.log('Applied fixed amount discount to the cart')
        print(cart)
        print(f'Total cost after fixed amount discount: {cart.total_cost()} $')

        # Using different payment systems
        credit_card_processor = CreditCardProcessor("1234-5678-9800-1111", "Oleh Opalko", "000", "12/26")
        paypal_processor = PayPalProcessor("oleh.opalko@gmail.com")
        bank_transfer_processor = BankTransferProcessor("123456789", "Oleh Opalko")

        cart.pay(credit_card_processor)
        cart.pay(paypal_processor)
        cart.pay(bank_transfer_processor)

    except InvalidPriceError as e:
        print(e)
    except InvalidQuantityError as e:
        print(e)


if __name__ == "__main__":
    main()
