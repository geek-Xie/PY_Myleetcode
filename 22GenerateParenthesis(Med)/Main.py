"""
22. 括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

同样适用的是递归的思想
"""


from typing import List


class Solution:
    def checked(self, s):
        stack = []
        for p in s:
            if p == ')' and len(stack) == 0:
                return False
            if p == '(':
                stack.append(p)
            else:
                par = stack.pop()
                if par != '(':
                    return False
                else:
                    continue
        if len(stack) == 0:
            return True
        else:
            return False

    def generate(self, res, s, n, left, right):
        if len(s) == 2 * n and self.checked(s):
            res.append(s)
            return
        if left > n or right > n:
            return
        self.generate(res, s + '(', n, left + 1, right)
        self.generate(res, s + ')', n, left, right + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        self.generate(res, '', n, 0, 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
