"""
Asterisk
- multiplication,
- power operation,
- creation of lists/tuples,
- *args, **kwargs,
- unpacking lists, tuples or dicts into function argumnets,
- unpacking containers,
- merging containers into a list/dict.
"""

result = 5 * 5
print(result)

result2 = 5 ** 5  # 5 to the power of 5
print(result2)

zeros = [0, 1] * 10  # could have been a tuple or a string
print(zeros)
print(*zeros)
print("-------------")

numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning)  # unpack all except the last one into a list
print(last)


print("-------------")


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
beginning, second, *middle, secondlasdt, last = numbers2
print(beginning)
print(second)
print(middle)
print(secondlasdt)
print(last)


print("-------------")

# Merge iterables into a list

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]  # also works for sets

new_list = [*my_tuple, *my_list]
print(new_list)

dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)