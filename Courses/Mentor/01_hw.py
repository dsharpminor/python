# Homework 1
import math

# Ex 1
# What will be value of a after execution ?
"""
a = 10  # we assign the value of 10 to a
print(a)
a += len(str(a))  # a stores 12 (10 + 2 = 12)
print(a)
a = str(a)  # int a -> string a; a still stores 12
print(a)
a = len(a)  # the length of a that was str(a) is 2
print(a)
"""

# Ex 2
# Change following python script, so it will execute without errors
# "Im Erdnusswald hatten" + 2 + "Zwerge ein Haus"

"""
print("Im Erdnusswald hatten " + str(2) + " Zwerge ein Haus")
"""

# Ex 3
# Write a program that will prompt user about his name, age, and hobby.
# f-Strings


name = input("Hi, user! What is your name?\n")
try:
    age = input("Nice to meet you! I am Prohor. How old are you, " + name + "?\n")
    # if not float(age).is_integer():
    if not age.isnumeric():
        raise ValueError()
except ValueError:
    print("That doesn't look like an integer to me.")
    age = input(f"So, how old are you, {name} ? This time as an integer, please.\n")
hobby = input(f"I remember being {age} years old! Just kidding. I am a macbook, I am not that old. \n"
              "So, what is your main hobby?\n")
print(f"Cool! Now I know everything about you, {name} .\nYou are {age} years old and your main hobby is {hobby}\n"
      "That's a cool hobby, by the way. I'd like doing it too if I were human, I guess.\n")


# Ex 4
# What value will have variable a, after code execution?

"""
a = 10  # the value will be 10
print(a)

a + 1  # this is an invalid statement so a will stay 10
# to make it 11 we could do one of the following things:
# a += 1
# var = a + 1
# print(a + 1)
print(a)
"""

# Ex 5
# Fix following python script, si it will execute without errors.
# a = input()
# a += 1

"""
a = int(input())  # we need it to be int to make a sum
a += 1
print(a)
"""

# Ex 6
# Write a program that will prompt user radius of a circle and will calculate it’s area.

# print(10 ** 2)  # 10^2 = 10 ** 2

"""
radius = float(input("What is the radius of the circle?\n"))
area = math.pi * radius ** 2
print("The area is " + str("%.2f" % area) + ".")
"""