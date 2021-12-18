#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split(' ')
        result = [0] * len(temp)
        for i in temp:
            # print(i.isDigit())
            # print(i.isdigit())
            for j in i:
                if j.isdigit():
                    # i.pop(j)
                    result[int(j)-1] = i[:-1]
                    # result.pop([int(j)-1])
            # print(temp)
        return " ".join(result)
# @lc code=end
