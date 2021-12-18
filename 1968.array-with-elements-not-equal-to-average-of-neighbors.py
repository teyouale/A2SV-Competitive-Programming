#
# @lc app=leetcode id=1968 lang=python3
#
# [1968] Array With Elements Not Equal to Average of Neighbors
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)-1):
            pre = nums[i-1]
            current = nums[i]
            next = nums[i+1]
            if (pre < current < next) or (pre > current > next):
                nums[i+1], nums[i] = nums[i], nums[i+1]

        return nums
# @lc code=end
