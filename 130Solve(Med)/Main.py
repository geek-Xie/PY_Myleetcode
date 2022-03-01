"""
130. 被围绕的区域

给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例 1：
输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

示例 2：
输入：board = [["X"]]
输出：[["X"]]

根据题目的意思，可以理解到，只要是最终能够延伸到数组边界的"O"都不会被标记为"X"， 没有办法延伸到数组边界的"O"就会被"X"包围，变成"X"
因此我们首先对数组的边界进行遍历，从数组边界的"O"开始，进行深度优先搜索，标记到的位置为"A"
对边界完成遍历之后，我们把数组中的"O"变为"X"， 把这时的"A"恢复为"O"
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            self.dfs(board, i, 0)
            self.dfs(board, i, len(board[0]) - 1)

        for j in range(len(board[0])):
            self.dfs(board, 0, j)
            self.dfs(board, len(board) - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"

    def dfs(self, board, i, j):
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] != "O":
            return
        if board[i][j] == 'O':
            board[i][j] = "A"

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
