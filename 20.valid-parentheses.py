#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, str: str) -> bool:
        openRule = ['(', '{', '[']
        closeRule = [')', '}', ']']
        # print(rule)
        stack = []

        result = True

        if len(str) % 2 != 0:
            return False

        for i in str:
            if i in openRule:
                stack.append(i)
            elif i in closeRule:
                temp = closeRule.index(i)
                Item = openRule[temp]
                if stack:
                    # print(stack)
                    popItem = stack.pop()
                # print(temp,Item,popItem,stack)
                # print(popItem == Item)
                    if Item != popItem:
                        return False
                else:
                    result = False
            else:
                return False
        # print(stack,len(stack))
        if len(stack) != 0:
            return False

        return result

# @lc code=end
