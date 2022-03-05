"""
Generators are functions with yield instead of return
that return an object that can be iterated over.

ADVANTAGE: Save a lot of memory when you work with large data.

They generate the items lazily - one at a time and only when you ask for it.
Therefore they are much more efficient when we deal with larger data sets.
A powerful advanced Python technique.

We can have multiple yield statements per generator.
"""


def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()
# print(g)
# <generator object my_generator at 0x10f151950>

# for i in g:
#     print(i)
"""
value = next(g)
print(value)  # pauses at the line "yield 1"

value = next(g)
print(value)  # pauses at the line "yield 2"

value = next(g)
print(value)  # pauses at the line "yield 3"

# value = next(g)
# print(value)  # 4th time out of 3?
# would raise a StopIteration error
# because it doesn't reach another yield statement
"""

"""
Can be used as inputs to other functions that take iterables.
sum() takes iterables
"""

# print(sum(g))
# print(sorted(g))


def countdown(num):
    print("Start")
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)  # nothing is executed here
value = next(cd)   # run until the first yield statement
print(value)
print(next(cd))
print(next(cd))
print(next(cd))
# print(next(cd))  # would raise the StopIteration