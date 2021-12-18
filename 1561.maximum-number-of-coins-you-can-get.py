#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        index = len(piles)//3
        while (index > 0):
            A = piles.pop(-1)

            y = piles.pop(-1)
            count += y

            C = piles.pop(0)

            index -= 1
        return count
# @lc code=end
