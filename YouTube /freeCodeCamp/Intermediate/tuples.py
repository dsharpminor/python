# tuples are immutable, their elements cannot be changed
# tuples do not support item assignment after they were created
# (), but you can omit the parentheses
# lists are larger even if they have the same amount of elements as tuples
# creating a tuple is about up to 2 times after than creating a list

myTuple = ("Sydney",)  # a comma is needed for it to be recognized as a tuple
my2Tuple = tuple(["Max", 23, "False"])  # creates a tuple from a list
print(my2Tuple)

item = my2Tuple[0]
print(item)

#  .index() returns the index of the first occurance of the given element

cool_tuple = "Anastasia", 23, "Berlin"
name, age, city = cool_tuple
print(name)
print(age)
print(city)

# check if is in list/tuple
print(23 in cool_tuple)

cool_tuple2 = (0, 1, 2, 3, 4)
i1, *i2, i3 = cool_tuple2
print(i1)
print(i3)
print(i2)

