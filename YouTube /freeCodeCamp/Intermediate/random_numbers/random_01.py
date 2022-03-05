import random  # pseudo random / reproducable
import secrets # random for cyber security, takes more time, obly has 3 methods
import numpy as np
# proves that it is can be reproduced:

# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))
a = random.random()
print(a)

b = random.uniform(1, 10)  # float
print(b)

c = random.randint(1, 10)  # int, includes upper bound
print(c)

d = random.randrange(1, 10) # int, upper bound NOT included
print(d)

e = random.normalvariate(0, 1)  # где-то по Гауссу
print(e)

myList = list("ABCDEFGH")
print(myList)

# pick one random element:
f = random.choice(myList)
print(f)

# pick more random elements:
# .sample() - one cannot be picked multiple times
a_few = random.sample(myList, 3)
print(a_few)

# .choices() one can be picked multiple times:
can_be_repeated = random.choices(myList, k=3)
print(can_be_repeated)

# shuffle a list (поменять местами элементы)
random.shuffle(myList)
print(myList)

print("----------")

sec_a = secrets.randbelow(10)  # from 0 to 10, 10 not included
sec_b = secrets.randbits(4)  # return an integer with 4 random <<bits>>
# (aka from 0 to 15)
# because the highest possible number would be
# 1111 in binary, aka 15
# 2^3, 2^2, 2^1, 2^0 = 8 + 4 + 2 + 1 = 15
sec_c = secrets.choice(myList)  # a choice that is not reproducable
print(sec_a, sec_b, sec_c)

print("----------")

# numpy is also an option (pseudo random)
# a different number generator and a different seed function

no_idea = np.random.rand()
print(no_idea)
no_idea2 = np.random.randint(0, 10, 3)  # 10 excluded, size 3
print(no_idea2)
no_idea3 = np.random.randint(0, 10, (3, 4))  # 10 excluded, a 3 by 4 list with random integers
print(no_idea3)
print("Array:")
arr = np.array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr)
np.random.shuffle(arr)
print(arr)

# unsafe. Demonstrtation:
np.random.seed(1)
print(np.random.rand(1, 2))
np.random.seed(1)
print(np.random.rand(1, 2))

