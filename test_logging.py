import logging

logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error")
        return None

divide(10, 2)
