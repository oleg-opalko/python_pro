# Task 1

def do_something(before_func, after_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            before_func()
            result = func(*args, **kwargs)
            after_func()
            return result

        return wrapper

    return decorator


def do_before():
    print('Starting the function...')


def do_after():
    print('Function has completed')


@do_something(do_before, do_after)
def hello():
    print('Hello, World!')


hello()


# Task 2
def save_result(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                with open(file_name, 'a') as file:
                    file.write(f'{result}\n')
            except Exception as e:
                logging.error(e)

            return result
        return wrapper
    return decorator


@save_result('result_calculated.txt')
def test_calculation(x, y):
    return x + y


print(test_calculation(5, 10))


# Task 3
def exception_handler_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'An error in function: {func.__name__}: {e}')

    return wrapper


@exception_handler_decorator
def test_plus(x, y):
    return x + y


print(test_plus(10, 1))
test_plus(10, 's')

# Task 4
import time


def execution_time_measurement(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        diff = end - start
        print(f'Your function: {func.__name__} has been completed by {diff:.2f} seconds')
        return result

    return wrapper


@execution_time_measurement
def test_func_with_sleep(x, y):
    time.sleep(3)
    return x + y


test_func_with_sleep(123, 3)

# Task 5

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def logs(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        logging.info(f'Function: {func.__name__}, arguments: {args}, returned: {result}')
        return result

    return wrapper


@logs
def test_sum(a, b):
    return a + b


test_sum(1, 2)
test_sum(2, 9)


# Task 6

class CallLimit:
    def __init__(self, limit: int):
        self.limit = limit
        self.count = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.count >= self.limit:
                print(f'Your function {func.__name__} has used the usage limit: {self.limit}')
                return

            self.count += 1

            return func(*args, **kwargs)

        return wrapper


@CallLimit(3)
def hello():
    print('Hello, World!')


hello()
hello()
hello()
hello()
hello()


# Task 7
def cache(func):
    dict_cache = {}

    def wrapper(*args, **kwargs):
        if args in dict_cache:
            return dict_cache[args]

        result = func(*args, **kwargs)
        dict_cache[args] = result
        return result

    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(25))
print(fibonacci(25))
