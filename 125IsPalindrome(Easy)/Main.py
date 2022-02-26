"""
125. 验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串

示例 2:
输入: "race a car"
输出: false
解释："raceacar" 不是回文串
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s.strip()
        res_s = ""
        for c in s:
            if '0' <= c <= '9' or 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                res_s += c
        res_s = res_s.lower()
        start = 0
        end = len(res_s) - 1
        while start < end:
            if res_s[start] != res_s[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
