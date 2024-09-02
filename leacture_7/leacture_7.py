# Task 1
from typing import List, Any


def custom_gen(func, start: int, n: int):
    """
    Generator function that yields numbers based on a user-defined function.

    :param func: A function that defines the rule of the sequence.
    :param start: The starting number of the sequence.
    :param n: The maximum number of terms to generate.
    """
    if not isinstance(start, int) or not isinstance(n, int):
        raise TypeError('Start and End must be integer')

    current = start
    count = 0

    while current < n:
        cmd = yield current

        if cmd == 'stop':
            break

        current = func(current)
        count += 1


def geometric_prog(number: int):
    if not isinstance(number, int):
        raise TypeError('Number must be integer')

    if number == 0:
        raise ZeroDivisionError

    return number * 3


gen = custom_gen(geometric_prog, 1, 90)

print(next(gen))
print(next(gen))
gen.send('stop')


# Task 2
import functools
from timeit import timeit


def fibonacci_rec_with_buff(n, buff: None):
    if buff is None:
        buff = {0: 0, 1: 1}
    if n in buff:
        return buff[n]
    else:
        buff[n] = fibonacci_rec_with_buff(n - 1, buff) + fibonacci_rec_with_buff(n - 2, buff)
        return buff[n]


@functools.lru_cache(maxsize=None)
def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


fb1 = fibonacci_rec_with_buff(40, buff=None)
fb2 = fibonacci_rec(40)

print(fb1)
print(fb2)

print(timeit(stmt='fb1', globals=globals(), number=1))
print(timeit(stmt='fb1', globals=globals(), number=1))


# Task 3

def square(x: int) -> int:
    """
    Squares the given integer.

    :param x: An integer to be squared.
    :return: The square of the integer.
    """
    return x * x


def my_sum(numbers: List[int], func: Any):
    """
    Applies a given function to each element of a list of integers and returns the sum of the transformed elements.

    :param numbers: A list of integers to which the function will be applied.
    :param func: A function that takes an integer and returns an integer.
    :return: The sum of the elements in the transformed list.
    """
    if not numbers:
        raise ValueError('The list of numbers is empty')

    new_list_numbers = (func(x) for x in numbers)

    return sum(new_list_numbers)


text = input('Enter numbers separated by a space: >>>')
list_numbers = list(map(int, text.strip().split()))


current_sum = my_sum(list_numbers, square)

print(current_sum)















