"""
Errors and exceptions.
"""

# trying to add a number to a string will raise the type error

# raise your own exception
"""
x = -5
if x < 0:
    raise Exception('x should be positive')
"""
# assert
"""
x = -5
assert(x >= 0), "x is not positive"
"""

# try & catch exceptions

"""
try:
    a = 5 / 0
except Exception as e:
    print(e)
    print("You can't divide by 0, dummy"
"""

try:
    b = 5 / 0
except ZeroDivisionError:
    print("You can't divide by 0, dummy")
else:
    print("It's fine")


class ValueTooSmall(Exception):
    def __init__(self, message, value):  # custom init method
        self.message = message
        self.value = value


class ValueTooHighError(Exception):  # you want to keep these classes small
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmall("Value is too small", x)


try:
    # test_value(300)
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmall as e:
    print(e.message, e.value)