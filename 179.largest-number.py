#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(x, y):
            # print(x,y)
            x = str(x)
            y = str(y)

            tempxy = ''.join([x, y])
            tempyx = ''.join([y, x])
            # print(int(tempxy),int(tempyx))
            if int(tempxy) > int(tempyx):
                return -1
            else:
                return 1
            # print(nums)
            # if x == 30:
                # return -1
        nums = sorted(nums, key=functools.cmp_to_key(comparator))
        if "".join(list(map(str, nums)))[0] == '0':
            return '0'
        return "".join(list(map(str, nums)))
# @lc code=end
