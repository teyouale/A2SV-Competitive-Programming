#
# @lc app=leetcode id=1630 lang=python3
#
# [1630] Arithmetic Subarrays
#

# @lc code=start
def isArt(nums, m):
    # print(m[1],"asdf")
    subarray = nums[m[0]:m[1]+1]
    print(subarray)
    subarray.sort()
    diff = abs(subarray[1] - subarray[0])
    if(diff == 0):
        # print(subarray[0],subarray[1],diff)
        temp = set(subarray)
        print(len(temp))
        # print([True len(temp) == 0 else False])
        return True if len(temp) == 1 else False
        # for i sub
    else:
        exp = [*range(subarray[0], subarray[-1]+1, diff)]
    # print(subarray,exp)
    # print(subarray == exp)
        return subarray == exp


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            # print(l[i],r[i])
            result.append(isArt(nums, [l[i], r[i]]))

        return result
# @lc code=end
