"""
Parameters are the variables that are defined or used inside parentheses when defining a function.
Arguments are the values passed for these parameters while calling a function.

*args    (tuple) - you can pass any number of positional arguments to your function
**kwargs (dict) - you can pass any number of keyword arguments to your function

Ana - argument
name:Ana - keyword argument
"""


def print_name(name):  # name - parameter
    print(name)


print_name("Ana")  # name - argument


def foo(a, b, c, d=4):
    print(a, b, c, d)


# foo(1, c=3, b=2)
# foo(1, c=3, b=2, d=7)


def hm(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


hm(1, 2, 3, 4, 5, six=6, seven=7)

print("------------")


def mm(a, b, *, c, d):
    # now every parameter after the start must be a keyword argument
    print(a, b, c, d)


def hh(*args, last):
    # now every parameter after the start must be a keyword argument
    for arg in args:
        print(arg)
    print(last)


mm(1, 2, c=3, d=4)
print("------------")
hh(1, 2, 3, last=100)
print("------------")


def ll(a, b, c):
    print(a, b, c)


my_list = [0, 1, 2]
ll(*my_list)  # list lenght must match the num of parameters
my_dict = {"a": 1, "b": 2, "c": 1}
ll(*my_dict)

print("------------")


def loc_glob():
    global number  # this is global
    number = 3     # this only lives inside of function


number = 0
loc_glob()
print(number)

"""
Call by value / call by reference
in Python is
call by object / call by object reference

1) the parameter passed in is actually a reference passed to an object, 
but the reference is passed by value

2) mutable objects (lists, dicts) can be changed within a method,
but if you rebind the reference in the method,
then the outer reference will still point at the original object
3) immutable objects in a mutable object can be reassigned
within a method
"""


def fool(x):
    x = 5  # even if we assign x to 5, it still prints 10


var = 10
fool(var)
print(var)


def fool2(a_list):

    # a_list = [200, 300]  # doesn't do anything
    a_list.append(4)
    a_list[0] = -100
    a_list += [200, 300]  # works



print("---------")
my_list2 = [1, 2, 3]
fool2(my_list2)
print(my_list2)

