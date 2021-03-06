"""
120. 三角形最小路径和

给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

示例 1：
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

示例 2：
输入：triangle = [[-10]]
输出：-10

使用动态规划的方法，创建一个和 triangle 一样大小的列表，每个位置存储到达当前位置的最小和。
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for i in range(len(triangle)):
            r = []
            for j in range(len(triangle[i])):
                r.append(0)
            dp.append(r)
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0:
                    dp[i][j] = triangle[i][j]
                    continue
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][0]
                    continue
                if j == len(dp[i]) - 1:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                    continue
                dp[i][j] = triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])

        res = dp[-1][0]
        for d in dp[-1]:
            if d < res:
                res = d

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(solution.minimumTotal([[-10]]))
