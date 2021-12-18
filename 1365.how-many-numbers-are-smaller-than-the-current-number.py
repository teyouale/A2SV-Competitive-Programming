#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newArray = [0] * len(nums)
        for index, element in list(enumerate(nums)):
            #             print (index)
            for i in range(0, len(nums)):
                if element > nums[i]:
                    newArray[index] += 1
        return newArray

# @lc code=end
