# sets = unordered, mutable BUT doesn't store duplicate elements unlike tuples and lists

mySet = {1, 2, 3, 2}
print(mySet)

mySet2 = set([1, 2, 3])
print(mySet2)

mySet3 = set("Hello") # a nice trick to find out how many different characters are in your word
print(mySet3)

emptyDictionary = {}
emptySet = set()

print(type(emptyDictionary))
print(type(emptySet))

emptySet.add(1)
print(emptySet)

# множества
odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}
prime = {2, 3, 5, 7}

u = odd.union(even)  # объединение
print(u)

i = odd.intersection(prime)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13, 14}

d = setA.difference(setB)  # difference
print(d)  # what is in setA but is not in set B

d2 = setB.difference(setA)  # difference
print(d2)  # what is in setA but is not in set B

sd = setB.symmetric_difference(setA) # elements that are different in both set A and set B
print(sd)

# aka just like the sum of d and d2
d3 = d2.union(d)
print(d3)

setA.update(setB) # updates setA by adding the elements found in setB
# setA.intersection(setB)  # now only the elements that were in both setA and setB are in setA
