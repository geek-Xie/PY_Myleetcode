"""
97. 交错字符串

给定三个字符串s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。

示例 1：
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true

示例 2：
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false

示例 3：
输入：s1 = "", s2 = "", s3 = ""
输出：true

使用动态规划的思路。
设f(i, j)表示以i位置为结束的s1和以j位置为结束的s2能否交错组成以i+j为结尾的s3的字符串
1.首先如果s1[i] == s3[i + j]，那么f(i,j)就取决于f(i - 1, j)
2.如果s2[j] == s3[i + j]，呢么f(i,j)就取决于f(i, j - 1)
即 f(i, j) = (f(i - 1, j) && s1[i - 1] == s3[i + j - 1]) || (f(i, j - 1) && s2[j - 1] == s3[i + j - 1])
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == len(s2) == len(s3) == 0:
            return True
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        list_s1 = []
        list_s2 = []
        list_s3 = []
        for i in range(len(s1)):
            list_s1.append(s1[i])

        for i in range(len(s2)):
            list_s2.append(s2[i])

        for i in range(len(s3)):
            list_s3.append(s3[i])

        if sorted(list_s1 + list_s2) != sorted(list_s3):
            return False
        if len(s3) == 0:
            return False

        dp = []
        for i in range(len(s1) + 1):
            r = []
            for j in range(len(s2) + 1):
                r.append(False)
            dp.append(r)
        dp[0][0] = True

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j == 0:
                    continue
                if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] or dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        return dp[len(s1)][len(s2)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
    print(solution.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
    print(solution.isInterleave('aa', 'ab', 'abaa'))
