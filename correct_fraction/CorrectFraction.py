from math import gcd


class CorrectFraction:
    """
    A class representing a fraction in its simplest form.
    """
    def __init__(self, numerator: int, denominator: int):
        """
        Initializes a CorrectFraction instance and reduces it to its simplest form.
        :param numerator: The numerator of the fraction.
        :param denominator: The denominator of the fraction.
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError('Numerator and denominator must be integers')
        if denominator == 0:
            raise ValueError('Denominator cannot be zero')

        # calculate greatest Common Divisor
        divisor = gcd(numerator, denominator)

        # reducing the fraction to its simplest form.
        self.top = numerator // divisor
        self.bottom = denominator // divisor

    def __add__(self, other):
        """
        Adds two CorrectFraction objects.
        :param other: Another CorrectFraction instance to add.
        :return: A new CorrectFraction representing the sum.
        """
        if not isinstance(other, CorrectFraction):
            raise TypeError('Must be a CorrectFraction object')

        new_top = self.top * other.bottom + other.top * self.bottom
        new_bottom = self.bottom * other.bottom
        return CorrectFraction(new_top, new_bottom)

    def __sub__(self, other):
        """
        Subtracts another CorrectFraction from this one.
        :param other: Another CorrectFraction instance to subtract.
        :return: A new CorrectFraction representing the difference.
        """
        if not isinstance(other, CorrectFraction):
            raise TypeError('Must be a CorrectFraction object')

        new_top = (self.top * other.bottom) - (other.top * self.bottom)
        new_bottom = self.bottom * other.bottom
        return CorrectFraction(new_top, new_bottom)

    def __mul__(self, other):
        """
        Multiplies two CorrectFraction objects.
        :param other: Another CorrectFraction instance to multiply with.
        :return: A new CorrectFraction representing the product.
        """
        if not isinstance(other, CorrectFraction):
            raise TypeError('Must be a CorrectFraction object')

        new_top = self.top * other.top
        new_bottom = self.bottom * other.bottom
        return CorrectFraction(new_top, new_bottom)

    def __lt__(self, other):
        """
        Compares if this fraction is less than another.
        :param other: Another CorrectFraction instance to compare with.
        :return: True if this fraction is less, False otherwise.
        """
        if not isinstance(other, CorrectFraction):
            raise TypeError('Must be a CorrectFraction object')

        return self.top * other.bottom < other.top * self.bottom

    def __gt__(self, other):
        """
        Compares if this fraction is greater than another.
        :param other: Another CorrectFraction instance to compare with.
        :return: True if this fraction is greater, False otherwise.
        """
        if not isinstance(other, CorrectFraction):
            raise TypeError('Must be a CorrectFraction object')

        return self.top * other.bottom > other.top * self.bottom

    def __eq__(self, other):
        """
        Checks if this fraction is equal to another.
        :param other: Another CorrectFraction instance to compare with.
        :return: True if the fractions are equal, False otherwise.
        """
        if not isinstance(other, CorrectFraction):
            raise TypeError('Must be a CorrectFraction object')

        return self.top * other.bottom == other.top * self.bottom

    def __le__(self, other):
        """
        Checks if this fraction is less than or equal to another.
        :param other: Another CorrectFraction instance to compare with.
        :return: True if this fraction is less or equal, False otherwise.
        """
        return self < other or other == self

    def __ge__(self, other):
        """
        Checks if this fraction is greater than or equal to another.
        :param other: Another CorrectFraction instance to compare with.
        :return: True if this fraction is greater or equal, False otherwise.
        """
        return self > other or self == other

    def __str__(self):
        """
        Returns the string representation of the fraction.
        :return: A string representing the fraction.
        """
        if self.bottom == 1:
            return f'{self.top}'
        elif self.top > self.bottom:
            return f'{self.top // self.bottom}  {CorrectFraction(self.top % self.bottom, self.bottom)}'
        return f'{self.top} / {self.bottom}'


print(CorrectFraction(3, 4) + CorrectFraction(1, 2))

print(CorrectFraction(1, 2) * CorrectFraction(3, 7))

print(CorrectFraction(3, 5) - CorrectFraction(1, 5))

lt = CorrectFraction(3, 4) < CorrectFraction(11, 2)
print(lt)

gt = CorrectFraction(4, 11) > CorrectFraction(4, 7)
print(gt)

eq = CorrectFraction(3, 4) == CorrectFraction(6, 8)
print(eq)

le = CorrectFraction(3, 4) <= CorrectFraction(6, 8)
print(le)

ge = CorrectFraction(6, 8) >= CorrectFraction(3, 4)
print(ge)




