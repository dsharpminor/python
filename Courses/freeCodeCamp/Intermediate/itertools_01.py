# Itertools are iterators that can be used in loops
"""
product            - cartesian product
permutations       - all possible permutations
combinations       - combinations, combinations_with_replacement
accumulate         - accumulate (next element is += previous one); or import operator and change to
                     *= operator.mul, -= operator.sub
groupby            -
infinite iterators -
"""

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator
a = [1, 2, 3, 4]
b = [5]

prod = product(a, b, repeat = 2)  # cartesian product
print(prod)  # <itertools.product object at 0x106c492d0>
print(list(prod))

perm = permutations(a, 2)  # 2 - количество элементов в каждом tuple
print(list(perm))

comb = combinations(a, 2)
print(list(comb))

c2 = combinations_with_replacement(a, 2)  # если "4" только одна, то можно (4,4)
print(list(c2))

# a = accumulate(a)
# print(list(a))   # [1, 2, 3, 4] -> [1, 3, 6, 10]

a2 = list(accumulate(a, operator.mul))  # or func=operator.mul or .sub
print(a2)


# groupby

c = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def smaller_than_three(x):
    return x < 3


group_obj = groupby(c, key=lambda x: x < 3)  # or key=smaller_than_three
for key, value in group_obj:
    print(key, list(value))


people = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 23}, {'name': 'Tina', 'age': 21}]

group_obj2 = groupby(people, key=lambda x: x['age'])  # or key=smaller_than_three
for key, value in group_obj2:
    print(key, list(value))

# counters

for i in count(10): # infinite loop that starts at 10
    print(i)
    if i == 15:
        break

d = [1, 2, 3, 4]


# for i in cycle(d): # types 1,2,3,4 infinitely
#     print(i)


# for i in repeat(1): # types 1 infinitely
#     print(i)

for i in repeat(1, 10):  # types 1 ten times
    print(i)