# Homework 2.2
"""
Ex. 1
Write a program that will that will transform an array of strings
to a single string, where all items will be separated by comma ,
also last element should be separated by keyword and.
(Ex: [“apples”, “bananas”, “cats”] -> “apples, bananas and cats”)
"""

fruits = ["apples", "bananas", "pineapples", "oranges", "lemons"]


def make_a_sentence(words):
    upd_words = ', '.join(words)  # create a string with commas
    # find the last comma to replace it with an "and "
    last_comma_index = upd_words.rfind(",")  # last comma index = 36
    upd_words = upd_words[:last_comma_index] + " and" + upd_words[last_comma_index + 1:] # replace
    #                          [0, 36)           [36]                   [37, -1]
    upd_words = upd_words.capitalize() + "."  # first letter is uppercase, last symbol is .
    return upd_words


print(make_a_sentence(fruits))
print("-----------------")

""" Ex. 2
Write a program that will show all elements from a dictionary 
and will calculate their total sum.
Ex, {‘scanue’: 33, ‘,mese’: 22}
Items:  ‘scaune’, ‘mese’
total : 55
"""

ikea = {'tables': 247, 'sofas': 24}


def count_total(items):
    key_list = []
    total = 0

    for key in items.keys():  # add item names to a list
        key_list.append(key)

    for value in ikea.values():  # calculate the sum of the values
        total += int(value)

    answer = "Items: " + ', '.join(key_list) + ". Total amount: " + str(total)
    return answer


print(count_total(ikea))

