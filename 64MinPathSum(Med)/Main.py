"""
64. 最小路径和

给定一个包含非负整数的 mxn网格grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12

还是使用动态规划的思路，创建一个和grid同样大小的数组，每个位置都代表这到达该位置的最小和，最后返回数组的最后一个元素即可
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                row.append(-1)
            res.append(row)
        for i in range(len(grid)):
            if i == 0:
                res[i][0] = grid[0][0]
            else:
                res[i][0] = res[i - 1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            res[0][j] = res[0][j - 1] + grid[0][j]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]

        return res[len(grid) - 1][len(grid[0]) - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(solution.minPathSum([[1, 2, 3], [4, 5, 6]]))
