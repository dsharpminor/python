# Exercises

a = ['a', 'b', 'c', 'd']

""" Ex 1. 
What will be value of this expression [int(int('3' * 2) // 11] ?"""
# exp = [int(int('3' * 2) // 11]
# SyntaxError: invalid syntax. It is because of the lacking ) after 11
# But what if the syntax was ok? Step by step:
val1 = int('3' * 2)  # '3'* 2 = 33
val2 = val1 // 11    # 33 // 11 = 3
print(val1, val2)
# And now together:
print([int(int('3' * 2) // 11)])  # 3

""" Ex 2. 
Add a new item into array a on first index. 
"""

a.insert(1, "new item")
print(a)

""" Ex 3.
Delete last 2 items from array a.
"""

# The first option would require the usage of the keyword 'del'
del a[-1]
del a[-1]
print(a)

# Let's add the elements back.
a.extend(['c', 'd'])  # extend is a convenient method for adding multiple values as separate elements, not as a new list
print(a)

# The second option would require slicing:
a = a[:-2]  # only the elements from start till the second last one (excluded)
print(a)

# Let's add the elements back again (in a different way)
a.append('c')
a.append('d')
print(a)

# The third option is pop():
# a.pop(-1)
# a.pop(-1)
# print(a)

""" Ex. 4
Sort array a in the descending order
"""

a.sort(reverse=True)
print(a)

""" Ex. 5
Create new array b that will contain all elements from a excluding first 2 elements.
"""
# Slicing is the most obvious option, so I'm going to try it first.
# The first two elements have indices 0 and 1, hence:
b = a[2:]
print(b)

# Another possibility would be to copy the whole list and then remove the first two elements.
# However, this is not efficient
b = a.copy()
#    or
# b = list(a)
#    or
# b = a[:]
#    and then:
b.pop(0)
b.pop(0)
print(b)
# The most important thing is not to copy lists in the following way:
c = a
# because
print(id(a), id(c))
# they refer to the same object, for instance to the object 4475677664.
