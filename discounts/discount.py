class Discount:
    def apply(self, price):
        raise NotImplementedError


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


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        if not isinstance(percentage, int | float):
            raise TypeError('Percentage must be a number')

        self.percentage = percentage

    def apply(self, price) -> float:
        """
        Calculate total amount with percentage discount
        :param price: int | float
        :return: int | float
        """
        return price * (1 - self.percentage / 100)
