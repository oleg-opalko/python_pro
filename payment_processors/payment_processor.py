class PaymentProcessor:
    def pay(self, amount):
        """
        Base method for pay items
        :param amount:
        :return:
        """
        raise NotImplementedError


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
