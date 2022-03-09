"""
Counter     - to count elements, find the most common one, etc.
namedtuple  - to create tuples with named fields, a lightweight object type similar to a struct,
              creates a class with fields,
OrderedDict - just like a regular dictionary, but it remembers the order in which the items were inserted
              (since Python 3.7 the built-in Dictionary class also has the ability to remember it, so
              it has become less important),
defaultdict - it will have a default value if the key has not been set yet,
deque       - double ended queue that allows to add/remove elements to/from both ends
"""

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
# !!! make sure your file isn't named "collections" !!!

# Counter
var = "aaaaabbcccccccccccc"
my_counter = Counter(var)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))  # top1 most common (a list of tuples)
print(my_counter.most_common(1)[0])  # top1 most common tuple
print(my_counter.most_common(1)[0][0])  # top1 most common element

print(list(my_counter.elements()))

# namedtuple

Point = namedtuple("Point", "x,y")  # creates a class Point with fields x and y
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# OrderedDict (not needed since Python 3.7)

o_d = OrderedDict()
o_d["b"] = 2
o_d["c"] = 3
o_d["a"] = 1
print(o_d)

# defaultdict

d = defaultdict(int)  # int as default type
d["a"] = 1
d["b"] = 2
print(d['c'])  # will print 0, the default value of an integer

# deque - double ended queue

de = deque()
de.append(1)  # appends to the right side
de.append(2)
print(de)
de.appendleft(0)  # appends to the left side
print(de)
de.popleft()
print(de)
de.extendleft([0, -1, -2, -3])  # -3 being the most left element
de.extend([3, 4, 5])
print(de)
de.rotate()  # every element makes a step to the right
print(de)
# de.rotate(2)  # every element makes 2 steps to the right
# de.rotate(-1)  # every element makes a step to the left
print(de)