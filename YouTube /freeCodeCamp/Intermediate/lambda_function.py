#  lambda arguments: expression

"""
When used?
1. You need a simple function that is only used once
2. You need a lambda function to be used as an argument to higher order functions

They are used along with the built-in functions such as: sorted, map, filter (they are built-in), reduce
"""
from functools import reduce

add10 = lambda x: x + 10
print(add10(5))


def add10_func(x):
    return x + 10


mult = lambda x, y: x * y
print(mult(2, 10))

points2D = [(0, 1), (-2, 3), (18, 10), (-10, 2), (6, 14), (2, 15)]
points2D_sorted = sorted(points2D) # sorts by the first argument
print(points2D_sorted)
points2D_sorted = sorted(points2D, key=lambda x: x[1])  # sorts by the second argument, aka x[1]
print(points2D_sorted)
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])  # sorts by the sum
print(points2D_sorted)

# map

a = [1, 2, 3, 4]
b = map(lambda x: x*2, a)
print(list(b))

# or with list comprehension
c = [x * 2 for x in a]
print(list(c))

d = filter(lambda x: x % 2 == 0, a)  # only even
print(list(d))

d2 = [x for x in a if x % 2 == 0]
print(list(d2))

product_a = reduce(lambda x, y: x * y, a)
print(product_a)  # 1 * 2 * 3 * 4 = 24
