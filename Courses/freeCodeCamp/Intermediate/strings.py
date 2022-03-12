# strings are immutable
from timeit import default_timer as timer


my_string = "      Hello World    "
print(my_string.strip())  # removed extra space surrounding the string
# it doesn't change the original string though, strings are immutable
print(my_string.strip().startswith("H"))
print(my_string.endswith(" "))
print(my_string.strip().find("d"))  # returns the first index with d
print(my_string.find("d"))  # returns the first index with d
print(my_string.count(" "))
print(my_string.strip().count(" "))
print(my_string.replace("Hello", "Hi"))

my_string2 = "random letters"
my_list = my_string2.split() # ['random', 'letters'] - the default delimiter is a space
print(my_list)
my_list2 = my_string2.split(",")  # no commas - no delimiting - returns the full string
print(my_list2)
new_string = ' '.join(my_list)  # concat; ' ' here space is needed to have it in between
print(new_string)

# way cleaner and faster than for loop in this context
start = timer()
a_list = ['a'] * 6
a_string = ''.join(a_list)
print(a_string)
stop = timer()
print(stop-start)

# formatting strings

var = "Hello"
my_sentence = "the variable's value is \"%s\"" % var
print("----" + my_sentence)

# % (the very old way)
var2 = 3.12345678
my_var2 = "the variable is %.2f" % var2  # %.2f - how many digits we want after comma
print(my_var2)

# format() - the old way

my_var3 = "the variable is {}".format(var2)
print(my_var3)

my_var4 = "the variables are {:.2f} and {}".format(var2, var)  # specify how many digits by "... is {:.2f}".format
print(my_var4)

# f-Strings (the very NEW way, since Python 3.6)

my_var5 = f"the variables are {var2:.2f} and {var}"
print(my_var4)

