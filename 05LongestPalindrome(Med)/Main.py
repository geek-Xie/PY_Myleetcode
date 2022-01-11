"""
5. 最长回文子串

给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"

使用动态规划的方法
回文串的判断：
1.首先首尾必须相同
2.首尾相同的情况下，去掉首尾剩下的子串如果是回文串，则该字符串也是回文串

令首尾下标分别为i， j，状态方程为：
dp[i][j] = (s[i] == s[j]) && ((j - i < 3) || dp[i + 1][j - 1])

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        if str_len < 2:
            return s

        begin = 0
        res_len = 1
        dp = []
        for i in range(str_len):
            d = []
            for j in range(str_len):
                d.append(False)
            dp.append(d)

        for index_ in range(str_len):
            dp[index_][index_] = True

        for j in range(1, str_len):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] is True and j - i + 1 > res_len:
                    res_len = j - i + 1
                    begin = i
        return s[begin: begin + res_len]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('babad'))
