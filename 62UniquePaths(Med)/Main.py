"""
62. 不同路径

一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6

使用动态规划的方法，创建一个和网格大小相同的数组，数组的每个位置数字代表到达这个位置的方法的数量。
显然第一行和第一列的位置到达的方法数都是1， 其他位置到达的方法数 f(i, j) = f (i - 1, j) + f (i, j - 1)
最后返回f (m - 1, n - 1)位置的方法数即可
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(1)
            res.append(row)
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 7))
    print(solution.uniquePaths(3, 2))
    print(solution.uniquePaths(7, 3))
    print(solution.uniquePaths(3, 3))
