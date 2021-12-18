#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1
        one = -1
        for i in range(0, len(nums)):
            if nums[i] < 2:
                one += 1

            if nums[i] == 0:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]

            if nums[i] == 1:
                nums[one], nums[i] = nums[i], nums[one]
# @lc code=end
