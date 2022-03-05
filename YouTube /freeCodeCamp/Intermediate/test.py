# a = 1
# b = 2 - 1
# print(a is b)
#
# a = 'ab'
# b = 'a' + 'b'
# print(a is b)

# def is_palindrome(text):
#     return text == text[::-1]
#
# print(is_palindrome("lalal"))

#
# palindrome = lambda text: text == text[::-1]
# print(palindrome("heheh"))

a = ([],)
a[0].extend([1])
print(a[0] == [1])

"""
Tuples всегда immutable, то есть кортежи модифицировать нельзя. 
Однако, список, на который ссылаются из кортежа, не является частью кортежа. 
Он не "знает", что находится в кортеже, так что .extend() сработает. Поэтому True"""

T = (4, 2, 3)
L = (1)
print(type(T))

