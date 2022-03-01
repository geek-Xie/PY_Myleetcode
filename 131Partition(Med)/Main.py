"""
131. 分割回文串

给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]

首先使用动态规划的方法，找出字符串中所有可能存在的回文串，设置dp[i][j]表示以i开头，j结尾的字符串是否为回文串，
如果s[i] = s[j]，则dp[i][j]取决于dp[i + 1][j - 1]
dp[i][j] = (j - i < 3) || (s[i] = s[j] && dp[i + 1][j - 1])

然后使用dfs对存在的所有回文串组合进行深度优先搜索
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        dp = []
        for i in range(len(s)):
            d = []
            for j in range(len(s)):
                d.append(False)
            dp.append(d)
        for i in range(len(s)):
            dp[i][i] = True
        for j in range(1, len(s)):
            for i in range(j):
                if s[i] != s[j]:
                    continue
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

        self.dfs(res, [], dp, s, 0)
        return res

    def dfs(self, res, cur, dp, s, start):
        if start == len(s):
            res.append(cur[:])
            return
        for end in range(start, len(s)):
            if dp[start][end]:
                cur.append(s[start: end + 1])
                self.dfs(res, cur, dp, s, end + 1)
                cur.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.partition("aab"))
    print(solution.partition("a"))
