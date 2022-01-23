"""
54. 螺旋矩阵

给你一个 m 行 n 列的矩阵matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

本题根据对应的规则，使用循环和一些方向标志位对遍历过程进行判断，注意判断临界条件即可
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = len(matrix)
        col = len(matrix[0])
        m, n = 0, 0
        right = True
        down = False
        left = False
        up = False
        count = 0
        round = 0
        while True:
            if count == row * col:
                break
            if right:
                res.append(matrix[m][n])
                count += 1
                if n == col - 1 - round:
                    right = False
                    down = True
                    m += 1
                else:
                    n += 1
            elif down:
                res.append(matrix[m][n])
                count += 1
                if m == row - 1 - round:
                    down = False
                    left = True
                    n -= 1
                else:
                    m += 1
            elif left:
                res.append(matrix[m][n])
                count += 1
                if n == round:
                    left = False
                    up = True
                    m -= 1
                else:
                    n -= 1
            elif up:
                res.append(matrix[m][n])
                count += 1
                if m == round + 1:
                    up = False
                    right = True
                    n += 1
                    round += 1
                else:
                    m -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
