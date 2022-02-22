"""
118. 杨辉三角

给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

示例2:
输入: numRows = 1
输出: [[1]]
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            row = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    row.append(1)
                else:
                    row.append(res[i - 2][j - 1] + res[i - 2][j])
            res.append(row)

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(6))
    print(solution.generate(7))
