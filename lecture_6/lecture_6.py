# Task 2
def geometric_prog_gen(a: int, r: int, n: int):
    """
    Generator for geometric progression.

    :param a: First term of the progression.
    :param r: Common ratio.
    :param n: Number of terms to generate.
    """
    if not isinstance(a, int) or not isinstance(r, int) or not isinstance(n, int):
        raise TypeError('Properties must be int')

    for i in range(n):
        curr_term = a * pow(r, i)
        yield curr_term


gen = geometric_prog_gen(2, 2, 4)

for i in gen:
    print(i)


# Task 3

def my_range(start: None, stop: None, step: int = 1):
    """
    Custom implementation of the range() generator.

    :param start: Start of the range. If stop is not provided, start is treated as stop and start is set to 0.
    :param stop: End of the range (exclusive).
    :param step: Step size between each number in the range.
    """

    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError('Step can\'t be 0')

    current = start

    if start > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step


for i in my_range(1, 10, 2):
    print(i)


# Task 4

def prime_numbers_gen(limit: int):
    """
    Generate prime numbers up to a given limit.

    :param limit: The upper limit (inclusive) for generating prime numbers.
    :return: A generator yielding prime numbers up to the limit.
    """
    if not isinstance(limit, int):
        raise TypeError("The limit must be an integer.")

    for number in range(2, limit + 1):
        for i in range(2, int(number // 2) + 1):
            if number % i == 0:
                break
        else:
            yield number


for prime in prime_numbers_gen(25):
    print(prime)


from datetime import datetime, timedelta


def date_range_gen(start_date: str, end_date: str):
    """
    Generate a sequence of dates from start_date to end_date.

    :param start_date: The start date in 'YYYY-MM-DD' format.
    :param end_date: The end date in 'YYYY-MM-DD' format.
    :return: A sequence of dates from start_date to end_date as strings.
    """
    try:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Dates must be in \'YYYY-MM-DD\' format')

    if start > end:
        raise ValueError('The start date must be before or equal to the end date')

    current_date = start
    while current_date <= end:
        yield current_date.strftime('%Y-%m-%d')
        current_date += timedelta(days=1)


for date in date_range_gen('2024-01-01', '2024-01-05'):
    print(date)
