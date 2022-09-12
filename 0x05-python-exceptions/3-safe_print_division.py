#!/usr/bin/python3
def safe_print_devision(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print('Inside result: {}'.format(result))
    return result
