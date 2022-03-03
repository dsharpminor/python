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
