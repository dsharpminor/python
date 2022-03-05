"""
There are 2 types of decorators: function and class decorators.
Function decorators are more common.

Syntax: @name

It is a function that takes another function as argument
and extends the behavior of this function without
explicitly modifying it.

i.e. extend a function with decorator's functionality

in Python functions are class objects, so they can be treated like an object
because they basically are objects

Use as many argyments/keywords as you'd like with *args, **kwargs:
def decorator_one(*args, **kwargs)

USE CASES:
1. A timer decorator to calculate the execution time of a function.
2. A debug decorator to print out some info about a function and its arguments
3. A check decorator to check if the arguments fulfill some requirements
4. Register functions like plug ins with decorators (???)
5. Cache return values
6. Add information / update the state
"""
import functools

# @mydecorator
# def do_something():
#     pass


def start_end_decorator(func):  # decorator function
    def wrapper():  # wrapper function (inside of decorator)
        # extend the behaviour before
        print("start")
        func()
        # extend the behaviour after
        print("end")

    return wrapper


# Second option
@start_end_decorator
def print_name():
    print("Anastasia")


# Don't like @? You can remove that line and write this instead:
# print_name = start_end_decorator(print_name)
print_name()


def start_end_decorator_two(func):  # decorator function
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # wrapper function (inside of decorator)
        print("start")
        result = func(*args, **kwargs)
        print("end, but kind of \"middle\", because technically return is the end now")
        return result  # end
    return wrapper

# What happens if our function has some arguments?


@start_end_decorator_two
def add_five(x):
    return x + 5

# print(add_five(10))  # unexpected argument if we use first decorator

print("____________")
print(add_five(10))
print("____________")
print(help(add_five))
# Python got confused about the identity of the decorator function:
"""
Help on function wrapper in module __main__:

wrapper(*args, **kwargs)

None
"""
# import functools to fix this and apply another @functools.wraps(func) before wrapper
# And it will become
"""
Help on function add_five in module __main__:

add_five(x)

None

"""