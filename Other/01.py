"""
Reversort(L):
  for i := 1 to length(L) - 1
    j := position with the minimum value in L between i and length(L), inclusive
    Reverse(L[i..j])
"""


def reversort(array):
    for i in array:
        print(i)
        print(array[i:])
        # j = min(array[i:])
        # print(j)
        # rev = (array[i:j+1])[::-1]


lala = [4, 1, 2, 3]
reversort(lala)
