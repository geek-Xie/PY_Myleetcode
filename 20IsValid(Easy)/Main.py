"""
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

示例3：
输入：s = "(]"
输出：false

示例4：
输入：s = "([)]"
输出：false

示例5：
输入：s = "{[]}"
输出：true

栈的简单应用
"""


class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        brackets_stack = []
        for bracket in s:
            if bracket in brackets_dict:
                brackets_stack.append(bracket)
            else:
                if len(brackets_stack) == 0:
                    return False
                pop_brack = brackets_stack.pop()
                if brackets_dict[pop_brack] == bracket:
                    continue
                else:
                    return False
        if len(brackets_stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('{[]}'))
