"""
73. 矩阵置零

给定一个m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

示例 1：
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]

示例 2：
输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

按照规则找出应该置0的行和列即可
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = []
        zero_cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_rows and j in zero_cols:
                    continue
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        for zero_row in zero_rows:
            for j in range(len(matrix[0])):
                matrix[zero_row][j] = 0

        for zero_col in zero_cols:
            for i in range(len(matrix)):
                matrix[i][zero_col] = 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(solution.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
