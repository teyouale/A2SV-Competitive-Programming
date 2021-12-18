#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        occ = Counter(nums)
        print(occ)

        for i in list(occ.keys()):
            temp = k - i

            print(temp)
            if i == k/2 and temp in occ.keys():
                print(occ[i])
                count += occ[i]//2

            elif temp in occ.keys():
                count += min(occ[i], occ[temp])
                del occ[i]
                del occ[temp]

        return count

# @lc code=end
