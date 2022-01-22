"""
48. 旋转图像

给定一个 n×n 的二维矩阵matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

示例 2：
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

按照对应的规则进行循环遍历，一层一层地进行旋转
"""


from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for round in range(len(matrix) // 2):
            left_top = matrix[round][round]
            left_bottom = matrix[len(matrix) - round - 1][round]
            right_top = matrix[round][len(matrix) - round - 1]
            right_bottom = matrix[len(matrix) - round - 1][len(matrix) - round - 1]

            matrix[round][round] = left_bottom
            matrix[len(matrix) - round - 1][round] = right_bottom
            matrix[round][len(matrix) - round - 1] = left_top
            matrix[len(matrix) - round - 1][len(matrix) - round - 1] = right_top

            for i in range(len(matrix) - (round * 2) - 2):
                top = matrix[round][i + round + 1]
                right = matrix[i + round + 1][len(matrix) - round - 1]
                bottom = matrix[len(matrix) - round - 1][len(matrix) - round - i - 2]
                left = matrix[len(matrix) - round - i - 2][round]

                matrix[round][i + round + 1] = left
                matrix[i + round + 1][len(matrix) - round - 1] = top
                matrix[len(matrix) - round - 1][len(matrix) - round - i - 2] = right
                matrix[len(matrix) - round - i - 2][round] = bottom

        print(matrix)


if __name__ == '__main__':
    solution = Solution()
    solution.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
