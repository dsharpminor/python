# Lists is ordered and mutable
# can contain different data types in one list
# []
myList = ['banana', 'cherry', 'apple']
print(myList)

item = myList[0]  # banana
item = myList[-1]  # the last item - apple

for i in myList:
    print(i)

myList2 = list()  # creates an empty list
myList2.append(118)
myList2.append(-2)
print(myList2)

item = myList.pop() # returns the last element AND removes it, woah
print(item) # cool
print(myList)

myList.sort() # changes the list
newList = sorted(myList2) # doesn't change the List2
print(myList)
print(myList2)
print(newList)

zeroList = [0] * 5
print(zeroList)

anotherList = zeroList + newList
print(anotherList)

# slicing
# [:5] not specified beginning -> from 0
# [5:] not specifies ending -> till the end

numbersList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slicing1 = numbersList[::1]  # normal list
print(slicing1)
slicing2 = numbersList[::2]  # step 2
print(slicing2)
slicing3 = numbersList[::-2]  # step -2
print(slicing3)
slicing4 = numbersList[:2]  # step -2; prints 0, 1 (2 isn't included)
print(slicing4)


# be careful with copying lists

list_org = ["one", "two", "three"]
# list_cop = list_org  # assignment = both lists refer to the same one inside of the memory
# list_cop = list_org.copy()  # makes a good new copy
# list_cop = list(list_org)   # also makes a good new copy
list_cop = list_org[:]   # also makes a good new copy but with the help of slicing
list_cop.append("four")

print(list_org)
print(list_cop)

# list comprehension

a = [1, 2, 3, 4, 5]
b = [i*i for i in a]  # a list of squares of a elements'
print(a)
print(b)
