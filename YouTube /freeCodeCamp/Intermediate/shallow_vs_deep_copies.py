import copy

# Integers are immutable
org = 5
cpy = org
# now both point to the same id
print(id(org) == id(cpy))
cpy = 6  # creates a new variable -> org and cpy become independent
print(id(org) == id(cpy))

# Lists are mutable

org1 = [0, 1, 2, 3, 4]
cpy1 = org1
cpy1[0] = -10
print(id(org1) == id(cpy1))  # now both point to the same id
# so unfortunately both lists are changed now
print(org1, cpy1)


"""
Shallow copies (if the element is one level deep)
"""

# cpy1 = copy.copy(org1)
# cpy1 = org1.copy()
# cpy1 = list(org)
# cpy1 = org[:]

"""
Deep copies (if the element is more than one level deep)
"""
# shallow c
deep_list = [[0, 1], [2, 3], [4, 5]]
# lcopy = copy.copy(deep_list)  # it is only one level deep
lcopy = copy.deepcopy(deep_list)
lcopy[0][0] = -10
# both lists are changed with copy, but now with deepcopy
print(deep_list)
print(lcopy)

"""
With copy:
[[-10, 1], [2, 3], [4, 5]]
[[-10, 1], [2, 3], [4, 5]]

With deepcopy:
[[0, 1], [2, 3], [4, 5]]
[[-10, 1], [2, 3], [4, 5]]

Can be used for built-in types AND for custom objects.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person("Alex", 27)
# p2 = p1  # not an actual copy, both will be changed
p2 = copy.copy(p1)
p2.age = 33
print(id(p1) == id(p2))

company = Company(p2, p1)
company_clone = copy.copy(company)
company_clone.boss.age = 56
print(id(company.boss) == id(company_clone.boss))
# again not an actual copy, both will be changed

company_smart_clone = copy.deepcopy(company)
company_smart_clone.boss.age = 56
print(id(company.boss) == id(company_smart_clone.boss))
# and here it is a deep copy, so everything is fine
# deepcopy works recursively

