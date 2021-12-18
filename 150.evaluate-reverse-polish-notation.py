#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rules = ['+', '-', '*', '/']
        ops = {"+": (lambda x, y: x+y), "-": (lambda x, y: x-y),
               "*": (lambda x, y: x * y), "/": (lambda x, y: int(x/y))}
        stack = deque()

        for i in tokens:
            if i in rules:
                x = int(stack.pop())
                y = int(stack.pop())
                print(ops[i](y, x), y, x, i)
                stack.append(ops[i](y, x))
                print(stack)
            else:
                stack.append(i)

        return stack.pop()

# @lc code=end
