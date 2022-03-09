# unordered, mutable; key - value pairs; keys cannot be repeated, values can be

my_dict = {"name": "Anastasia", "age": "23", "gender": "female"}
print(my_dict)

my_dict_2 = dict(name="Mary", age="17")

value = my_dict_2["age"]
print(value)
my_dict_2["gender"] = "female"  # add a key - value pair
print(my_dict_2)

# .popitem() removes the last pair since Python 3.7

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)