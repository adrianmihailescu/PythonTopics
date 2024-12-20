import logging

logging.basicConfig(level=logging.DEBUG)

def my_function():
    a = 10
    b = 20
    logging.debug(f'a: {a}, b: {b}')
    c = a + b
    logging.debug(f'c: {c}')

my_function()
