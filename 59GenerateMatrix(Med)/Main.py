"""
59. 螺旋矩阵 II

给你一个正整数n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的n x n 正方形矩阵 matrix 。

示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]

通过对过程进行模拟实现
"""


from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            res.append(row)
        count = 1
        rounds = 0
        right = True
        down = False
        left = False
        up = False
        r = 0
        c = 0
        while count <= n * n:
            if right:
                res[r][c] = count
                count += 1
                if c == len(res) - 1 - rounds:
                    right = False
                    down = True
                    r += 1
                else:
                    c += 1
            elif down:
                res[r][c] = count
                count += 1
                if r == len(res) - 1 - rounds:
                    down = False
                    left = True
                    c -= 1
                else:
                    r += 1
            elif left:
                res[r][c] = count
                count += 1
                if c == rounds:
                    left = False
                    up = True
                    r -= 1
                else:
                    c -= 1
            elif up:
                res[r][c] = count
                count += 1
                if r == rounds + 1:
                    up = False
                    right = True
                    c += 1
                    rounds += 1
                else:
                    r -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(3))
    print(solution.generateMatrix(1))
