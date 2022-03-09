import sys

# Tuples:
a = (1, 2, 3, 4)
b = [1, 2, 3, 4]

print(sys.getsizeof(a))
print(sys.getsizeof(b))
# so tuples are more light-weight, but immutable


# Dictionaries:
d = {'name': 'Bob', 'age': 44}
e = {'profile': {'name': 'Bob', 'age': 44}}
print(d['name'])
print(d.get('age'))

print(e['profile']['name'])

# Sets:

set1 = {1, 2, 3}
set2 = {3, 4, 5}

"""
There are a large number of set operations, including 
union ( | ), 
difference ( - ),
intersection ( & ), 
symmetric difference ( ^ ).
"""
print(set1 | set2)  # all values of set 1 and set 2
print(set1 - set2)  # values of set 1 that are not in set 2
print(set1 & set2)  # only common values
print(set1 ^ set2)  # only not common values, same as (set1 - set2) | (set2 - set1)

"""
Ex. 1
Write a program that will that will transform an array of strings 
to a single string, where all items will be separated by comma , 
also last element should be separated by keyword and. 
(Ex: [“apples”, “bananas”, “cats”] -> “apples, bananas and cats”)
"""

# Ex 1, first try

words = ["apples", "bananas", "pineapples", "oranges", "lemons"]   # create a list of words
upd_words = ', '.join(words)  # join the words with a comma
last_comma_index = upd_words.rfind(",")  # find the last comma's index
print(upd_words)
print(last_comma_index)
upd_words = upd_words[:last_comma_index] + " and" + upd_words[last_comma_index + 1:]  # replace the last comma
#                     [0, 36)           [36]               [37, -1]
#                     index 36 used to start with "," and now it starts with " and"
# print(upd_words[(last_comma_index + 1)])  # this will show "a"
print(upd_words)
# Let's make the first letter of the first word upper case too!
upd_words = upd_words.capitalize()
print(upd_words)
# Let's add a point in the end
upd_words = upd_words + "."
print(upd_words)


# Ex 1, second try
# Make a function out of it
"""
print("-----------------")
fruits = ["apples", "bananas", "pineapples", "oranges", "lemons"]


def make_a_sentence(words):
    upd_words = ', '.join(words)
    last_comma_index = upd_words.rfind(",")
    upd_words = upd_words[:last_comma_index] + " and" + upd_words[last_comma_index + 1:]
    upd_words = upd_words.capitalize() + "."
    return upd_words


print(make_a_sentence(fruits))
print("-----------------")
"""
""" Ex. 2
Write a program that will show all elements from a dictionary 
and will calculate their total sum.
Ex, {‘scanue’: 33, ‘,mese’: 22}
Items:  ‘scaune’, ‘mese’
total : 55"""

# Ex 2, first try

ikea = {'tables': 247, 'sofas': 24}
# key_list = []
#
# for key in ikea.keys():
#     key_list.append(key)
#
# print("Items: " + ', '.join(key_list))
#
# sum = 0
#
# for value in ikea.values():
#     sum += value
#
# print("Total: " + str(sum))

# Ex 2, second try


"""def count_total(items):
    key_list = []
    sum = 0

    for key in items.keys():
        key_list.append(key)

    for value in ikea.values():
        sum += value

    answer = "Items: " + ', '.join(key_list) + ". Total: " + str(sum)
    return answer


print(count_total(ikea))
"""
