# Work in progress
# "# Сумма каких двух чисел из массива равна третьему?

'''
s = Solution()
nums = [7, 19, 5, 5, 1]
target = 10
s.twoSum(nums, target)
# проблема в том что nums.index() берет первый индекс


def indices(my_list, value):
    return [i for i, x in enumerate(my_list) if x == value]

class Solution(object):

    def twoSum(self, nums, target):
        res = []
        for x in nums:
            for y in nums:
                # print(nums.index(x), nums.index(y))
                # if nums.index(x) != nums.index(y):
                if x + y == target:
                    if x != y:
                        res.append(nums.index(x))
                    else:
                        # print("x = y")
                        res.append(indices(nums, x))
                        return res[0]
        return res


nums = [7, 19, 5, 5, 1]
target = 10

s = Solution()
print(s.twoSum(nums, target))
'''
