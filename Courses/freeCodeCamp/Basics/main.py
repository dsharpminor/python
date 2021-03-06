from math import *
from decimal import Decimal

# strings

"""
phrase = "I'm learning Python"
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("learning"))
print(phrase.replace("I'm", "She's"))
"""

# numbers

"""
print(-2.0987)
print(4 + 1.5)
print(10 % 3)
num = -4
print(str(abs(num)) + " is a random number")  # Python starts complaining without str()
print(pow(2, 10))
print(max(16, 3))
print(min(16, 3))
print(round(17.24))
print(round(17.94))
print(floor(4.9))  # from the math import module to chop off the decimal point
print(ceil(4.01))  # round the number up no matter what
print(sqrt(16))
"""

# getting input from user

"""
name = input("What is your name? Please tell me here: ")  # take the value that the user inputs, store it in name
age = input("So how old are you? Please write to me here: ")
print("Hi, " + name + "! I know that you are " + age + " years old.")
"""

# addition of user input

"""
num1 = input("First number: ")
num2 = input("Second number: ")
res = float(num1) + float(num2)  # by default user input is string, so we have to convert to int or float
print("%.1f" % res)  # I only want 1 decimal after the point
"""

# Mad Lib Game (enter a noun / adj / etc.)

"""
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity's name: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
"""

# lists

"""
friends = ["Kevin", "Jim", "Roy"]
print(friends)
print(friends[0])
print(friends[-1])  # the last element is of index -1, it starts indexing from the back of the list
print(friends[1:])  # print the list starting with the element of index 1 (Jim and Roy only, no Kevin)

#  you can put anything in a list, different data types at the same time
# booleans True and False are capitalised

random_stuff = [True, 2, 2.34, "Stacey", "Faith", "Marie"]
print(random_stuff[1:3])  # only prints 1 and 2,            [2, 2.34]
print(random_stuff[:3])   # print up to element of index 3, [True, 2, 2.34]
print(random_stuff[-2: -1])  # the same as [-2] but in brackets as a list with one element. ['Faith']
print(random_stuff[-2])  # Faith
random_stuff[0] = False
# print(random_stuff[0])
# print(random_stuff)
"""

# basic list functions

"""
# Function names should be lowercase, with words separated by underscores as necessary to improve readability
# i.e. no camelCase

lucky_numbers = [4, 8, 15, 16, 23, 42]
names = ['Sarah', 'Stacey', 'Norman', 'Olga', 'Aphrodite']

# extend (add everithing)
names.extend(lucky_numbers)  # adding the elements from the second list into the first one
# ['Sarah', 'Stacey', 'Norman', 'Olga', 'Aphrodite', 4, 8, 15, 16, 23, 42]

# append (add individual elements to the end)
names.append("Sirius")
# ['Sarah', 'Stacey', 'Norman', 'Olga', 'Aphrodite', 4, 8, 15, 16, 23, 42, 'Sirius']

# insert (add individual elements into a specific place)
names.insert(1, "Anna")
# ['Sarah', 'Anna', 'Stacey', 'Norman', 'Olga', 'Aphrodite', 4, 8, 15, 16, 23, 42, 'Sirius']
# Anna goes to place 1, it does NOT overwrite anything - everything else just gets pushed right.

# remove (a specific element)
names.remove("Anna")
# ['Sarah', 'Stacey', 'Norman', 'Olga', 'Aphrodite', 4, 8, 15, 16, 23, 42, 'Sirius']

# pop (remove the last element)
names.pop()
# ['Sarah', 'Stacey', 'Norman', 'Olga', 'Aphrodite', 4, 8, 15, 16, 23, 42]

# index (find index by element)
print(names.index("Stacey"))
# print(names.index("Sirius"))
# would give us an error. ValueError: 'Sirius' is not in list

# clear (delete everything)
print(names.clear())
# []
print(names)

# count (count appearances of a certain value in the list)
new_names = ["Michael", "Michael", "Michael", "Anna", "Stacey"]
print(new_names.count("Michael"))  # it should say 3

# sort
# print(new_names.sort())   # it would not work because the result is not the list itself, so we print separately
new_names.sort()
print(new_names)

# reverse
new_names.reverse()
print(new_names)

# copy lists
very_new_names = new_names.copy()
print(very_new_names)
"""

# tuples

"""
# Lists has variable length, tuple has fixed length. [] for lists, () for tuples.
# List has mutable nature, tuple has immutable nature. List has more functionality than the tuple.
# use tuples for data that is never going to change

coordinates = (4, 5)  # we cannot modify it anymore
# coordinates[1] = 10  # 'tuple' object does not support item assignment (because it's immutable)
print(coordinates)
print(coordinates[0])

# a list of tuples
list_of_tuples = [(4, 5), (16, 3), (7, 15)]
print(list_of_tuples)
"""

# functions

"""
# our function is going to say "hi" to the user
# give descriptive names; "sayhi" or "say_hi" are both ok
# the code inside of a function needs to be indented


def say_hi(name, age):
    print("Hello, " + name + "! You are already " + str(age) + " years old, wow.")


say_hi("Mike", 23)

"""

# return statements

"""
def cube(num):
    return pow(num, 3)  # without the return statement it returns None


result = cube(5)
print("%.f" % result)
# one "%.1f" %
# two decimals "%.2f" %
# it converts float to string
# old-fashioned, use f-notation instead
"""

# if statements

"""
is_female = True
is_tall = False

if is_female and is_tall:
    print("You are a girl and you're tall!")
elif is_female and not is_tall:
    print("You are a girl or you're short.")
else:
    print("Go learn Python.")
"""

# if statements & comparisons

"""
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def is_dog():
    if "dog" == "dog":  # you can compare strings, booleans, etc.
        return print("it is a dog")


print(max_num(3, 12, 134))
is_dog()
"""

# building a better calculator

"""
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
"""

# dictionaries

"""
# key-value pairs
# keys have to be unique, we can't have "Jan" twice on the left

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}

print(monthConversions["Feb"])  # prints out February
print(monthConversions.get("Jan"))  # the same way to do it
print(monthConversions.get("Luv"))  # None
print(monthConversions.get("Luv", "Not a valid key"))  # Not a valid key (for this case only)
"""

# while loop

"""
# execute repeatedly until a certain condition is false

i = 1

while i <= 10:
    print(i)
    i += 1 #it ends up being 11 and we go down

print("Done with loop")
"""

# building a guessing game (guess a secret word, keep guessing until you get it right)

"""
secret_word = "giraffe"
guess = ""  # a variable to store the user's guess
guess_count = 0
guess_limit = 3

while guess != secret_word and guess_count < guess_limit:
    guess = input("Enter guess: ")
    guess_count += 1

if guess == secret_word:
    print("You win!")
else:
    print("Game over")
"""

# for loop

"""
friends = ["Jim", "Kevin", "Caren"]
print(len(friends))

for f in friends:
    print(f)


for i in "freeCodeCamp":
    print(i)


for index in range(10):  # 0-9, not including 10
    print(index)


for index in range(3, 11):  # 3-10, not including 11
        print(index)


for index in range(len(friends)):  # 0, 1, 2
    print(index)


for index in range(len(friends)):  # Jim, Kevin, Caren
        print(friends[index])


for index in range(len(friends)):  # Jim, Kevin, Caren
    if index == 0:
        print("First iretation!")
        print(friends[index])
    else:
        print("Not first")
        print(friends[index])

"""

# exponent function

"""
print(2**3)
print(pow(2, 3))


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return print(result)


raise_to_power(2, 10)
"""

# palindrome

"""
def is_palindrome(s):
    return s == s[::-1]


is_palindrome("tt")
s = "abcd"
print(s[::-1])
"""

# lesson 1

"""
print(8 / 2 * (2 + 2))
print(8 / (2 * (2+2)))
print(10 / 22 + 10)
print(77 // 12)
print(7 ** 6)
print(8 % 3)

# // rounds down
print(14 / 3)
print(14 // 3)

print(Decimal(10.01))

print('77' * str(10))
print("Ana" * "Ion")

print(float('10.70'))   # ?????????? , ???? ??????????????????

type(10.0)
print(type('10.0'))

print(locals())  # like in debugger

a = input("Enter your name: ")
print(a)
"""

# 2D lists and nested loops

"""
# list of lists; 4 rows, 3 columns
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# accessing elements
print(number_grid[0][0])  # row 0, column 0 -> 1
print(number_grid[0][2])  # row 0, column 2 -> 3
print(number_grid[2][1])  # row 2, column 2 -> 8

# print out all the elements
for row in number_grid:
    for col in row:
        print(col)
"""

# build a translator (replace all vowels with a "g")

"""
def translate(phrase):
    result = ""
    # loop through every letter; vowel? -> g
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                result += "G"
            else:
                result += "g"
        else:
            result += letter
    return result


print(translate(input("Enter a phrase: ")))
"""

# catching errors (Try Except)

"""
# you can store an error via
# except as err (it will print out something relevant automatically)

try:
    value = 10/0
    number = int(input("Enter a number:\n"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
"""

# reading files

"""
# r - read, w - write, a - append (just add some info to the end of the file), r+ - read and write
# once you're done reading a file, close it
my_file = open("1.txt", "r")

# is the file readable? returns a boolean
# print(my_file.readable())

# reads the whole file
# print(my_file.read())


# print(my_file.readline())  # reads the first line in the file, and then moves the cursor to the next line
# print(my_file.readline())  # so that this is the next line being printed out

# print(my_file.readlines())   # put all lines to an array
# print(my_file.readlines()[1])   # access a specific line in the array

for name in my_file.readlines():
    print(name)


my_file.close()
"""

# writing to files

"""
my_file = open("1.txt", "a")  # change to a to append, to w to write and replace
# my_file2 = open("12.txt", "w")  # creates another file, wow
# my_file3 = open("index.html", "w")  # creates another file, wow

my_file.write("\nToby Star")
# my_file3.write("<p>This is HTML </p>")
my_file.close()
"""

# slice notation, slicing

"""
a = "Anastasia"
#
# print(a[0])  # the first letter
# print(a[-1])  # the last letter
# # a[start:stop:step], stop is not included
# print(a[0:5:2])  # start at index 0, go until 5 (not included), step 2
#
# print(a[-3])  # the 3rd element from the end  - s
# print(a[-3:])  # the last 3 items in the array - sia   (-3: is like go on from -3 till the end)
# print(a[:-3])  # everything except the last 3 items   (:-3 is like go on from the beginning till -3 not including it)
# [:5] not specified beginning -> from 0
# [5:] not specifies ending -> till the end
"""

"""
-3 - ?????? ???????????? ?????????????????????????? ????????????
-3: - ?????????????????? ?????????? -3, ???????????? ???????? ???? -3 ???? ?????????? ?????????????? (?????????????? -3)
:-3 - ?????????????????? ???? -3, ???????????? ???????? ???? ???????????? ???? -3 (???????????????? -3)

?????????????????? ??????????? ??????????????????. 
?????????????????? ????????????? ????????????????. 
"""

"""
print(a[::-1])  # all items reversed
print(a[1::-1])  # the first two items, reversed

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

Reverse an array using slice notation:

[start:stop:step]
|   |   | ?????? ???????????? -1, ?????????? ???????????? ?????? ?????? 1 ?????? ??????????
|   |   ?????? ??????????
| ???? ???????????? ?????????????????
1 - ?????????? ????????????????? 0, 1
"""

"""
c = "Gleb"
print("\n")
print(c + " " + c[2:0:-1]) # Gleb el

b = "Anastasia"
print("\n")
print(b + "-" + b[3:0:-1])  # reverse the part of array that consists of elements 0, 1, 2, 3 but without 0
# Anastasia-san
print("\n")
# Anastasia
# [0; -3]
print(a[1::-1])  # the first two items, reversed
print(a[:-3:-1])  # the last two items, reversed
print(a[-3::-1])  # everything except the last two items, reversed

print(a[::-1])

print(a[:2])

print(a)
"""

# Classes and Objects

"""
# not everything can be covered by built-in data types -> we have classes and objects
# treat them like data types that you can create for anything you want
# you can model anything and create a real world object

from Student import Student
# from the Student file I want to import the Student Class
# an object is just an instance of a Class

student1 = Student("Anastasia", "Computer Science", 9.6, True)
student2 = Student("Pam", "Art", 7.4, False)

print(student1.name, student1.gpa)
print(student2.name, student2.gpa)
"""

# Multiple Choice Quiz

"""
from Question import Question

question_prompts = [
    "What color are apples?\n (a) Red/Green\n (b) Purple\n (c) Orange\n",
    "What color are bananas?\n (a) Teal\n (b) Magenta\n (c) Yellow\n",
    "What color are strawberries?\n (a) Yellow\n (b) Red\n (c) Blue\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(list_of_questions):
    score = 0
    for question in questions:
        try:
            answer = input(question.prompt + "\n")  # print out questions[0]
            if answer == question.answer:
                score += 1
            if answer not in "abc":
                raise ValueError()
        except ValueError:
            print("Please pick \"a\", \"b\" or \"c\".")
            while answer not in "abc":
                answer = input(question.prompt + "\n")  # print out questions[0]
                if answer == question.answer:
                    score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + " correct")


# we keep track of what we ask and what we ask

run_test(question_prompts)
"""

# function objects

"""
from Student import Student

student1 = Student("Anastasia", "Software Engineering", 9.6, True)
student2 = Student("Sam", "History", 10.0, True)

print(student2.on_honor_roll())
"""

# Inheritance
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChineseChef = ChineseChef()
myChef.make_chicken()
myChineseChef.make_chicken()
myChef.make_special_dish()
myChineseChef.make_special_dish()