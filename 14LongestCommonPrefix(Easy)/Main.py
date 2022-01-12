"""
14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

使用列表中最短字符串的长度进行逐个匹配
"""

import sys
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        min_len = sys.maxsize
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)
        for i in range(min_len):
            s = strs[0][i]
            for word in strs:
                if word[i] != s:
                    return res
            res += s
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
