"""
63. 不同路径 II

一个机器人位于一个m x n网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

示例 2：
输入：obstacleGrid = [[0,1],[0,0]]
输出：1

和62题思路一致，使用动态规划的思路，多了一个判断障碍的环节
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1:
            return 0
        res = []
        for i in range(len(obstacleGrid)):
            row = []
            for j in range(len(obstacleGrid[0])):
                row.append(0)
            res.append(row)
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                res[0][i] = 0
                break
            else:
                res[0][i] = 1
        for j in range(len(obstacleGrid)):
            if obstacleGrid[j][0] == 1:
                res[j][0] = 0
                break
            else:
                res[j][0] = 1
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(solution.uniquePathsWithObstacles([[0, 1], [0, 0]]))
