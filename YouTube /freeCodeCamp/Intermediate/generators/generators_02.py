# takes a lot of memory
import sys


def first_n(n):  # складываем все числа от введенного вниз до нуля
    nums = []  # we wouldn't need this list in a generator
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def first_n_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(first_n((533350))))
print(sys.getsizeof(first_n_gen((533350))))
print("---------")


def fibbonaci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b  # a = b; b = a + b


# like list comprehension but () instead of []
my_generator = (i for i in range(1000) if i % 2 == 0)
my_list = [i for i in range(1000) if i % 2 == 0]

# print(list(my_generator))

fib = fibbonaci(10)
for i in fib:
    print(i)

print("-------")
print(sys.getsizeof(my_generator))
print(sys.getsizeof(my_list))
