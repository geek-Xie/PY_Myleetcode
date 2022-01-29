"""
74. 搜索二维矩阵

编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false

可以利用每行从左往右递增的性质进行高效地查找
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False
        row = 0
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                row += 1
        for j in range(len(matrix[0])):
            if target == matrix[row - 1][j]:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
    print(solution.searchMatrix([[1], [3]], 3))
