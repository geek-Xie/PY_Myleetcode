"""
28. 实现 strStr()

实现strStr()函数。

给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for p_haystack in range(len(haystack) - len(needle) + 1):
            checked = True
            for p_needle in range(len(needle)):
                if haystack[p_haystack + p_needle] != needle[p_needle]:
                    checked = False
                    break
            if checked:
                return p_haystack
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr('mississippi', 'issip'))
