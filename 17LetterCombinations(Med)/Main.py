"""
17. 电话号码的字母组合

给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]

使用递归的思路，一个一个添加，直到当前字符串长度等于给定数字字符串的长度，返回，然后回退一个字符继续递归
"""


from typing import List


class Solution:
    def getComninations(self, num_dict, digits, c_index, c_str, res):
        if c_index == len(digits):
            res.append(c_str)
            return
        cur_word = num_dict[digits[c_index]]
        for w in cur_word:
            c_str += w
            self.getComninations(num_dict, digits, c_index + 1, c_str, res)
            # 回溯
            c_str = c_str[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        if len(digits) == 0:
            return res
        self.getComninations(num_dict, digits, 0, '', res)

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
