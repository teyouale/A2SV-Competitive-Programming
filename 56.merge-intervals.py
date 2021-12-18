#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            # print(out,i[0]<=out[-1][1])
            if out and i[0] <= out[-1][1]:
                print(out[-1][1])
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += i,
        return out
# @lc code=end
