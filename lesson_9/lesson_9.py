# Task 1
class BalanceDescriptor:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Balance must be an integer or float.')
        if value < 0:
            raise ValueError('Balance can\'t be negative.')

        instance.__dict__[self._name] = value


class Score:
    _balance = BalanceDescriptor()

    def __init__(self, init_balance=0):
        self._balance = init_balance

    def __setattr__(self, key, value):
        if key == 'balance':
            raise AttributeError('Can\'t modification balance property.')

        super().__setattr__(key, value)

    def __getattr__(self, item):
        return f'Property {item} does not exist'


score = Score(100)
print(score.balance)

try:
    score.balance = 200
except Exception as e:
    print(e)

print(score.balance)

# Task 2


class User:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    def __setattr__(self, key, value):
        if key == 'first_name':
            raise AttributeError(f'Can\'t modification {key} property')
        elif key == 'last_name':
            raise AttributeError(f'Can\'t modification {key} property')

        super().__setattr__(key, value)

    def __getattr__(self, item):
        return f'Property {item} not found'


user = User('Ivan', 'Ivanov')

try:

    user.first_name = "Oleh"
    user.last_name = "Opalko"

except Exception as e:
    print(e)

print(user.first_name)
print(user.last_name)
print(user.age)

# Task 3


class Rectangle:
    def __init__(self, width: int | float, height: int | float):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int | float):
            raise TypeError(f'Property must be integer or decimal')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int | float):
            raise TypeError(f'Property must be integer or decimal')
        self.__height = value

    def __setattr__(self, key, value):
        if key == 'height':
            raise AttributeError('Can\'t modification height property')
        elif key == 'width':
            raise AttributeError('Can\'t modification width property')

        super().__setattr__(key, value)

    def __getattr__(self, item):
        return f'Property {item} not found'

    def area(self):
        return self.__height * self.__width


rect = Rectangle(4, 5)
print(rect.width)
print(rect.height)
print(rect.area())
print(rect.x)

try:
    rect.width = 10
    rect.width = 9
except Exception as e:
    print(e)










