#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        occ = Counter(nums)
        for k, i in occ.items():
            # n * (n – 1) // 2
            temp = i * (i-1) // 2
            count += temp
            # print(i)

        # print(count)
        return count
# @lc code=end
