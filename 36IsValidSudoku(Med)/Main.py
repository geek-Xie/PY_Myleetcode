"""
36. 有效的数独

请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）

注意：

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用'.'表示。

示例 1：
输入：board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true

示例 2：
输入：board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：false
解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

使用遍历的方式在每一行，每一列结束时，每个小九宫格结束时 进行判断
"""

from typing import List


class Solution:
    def checkHorizontal(self, board, i):
        num_list = []
        for l1 in range(len(board)):
            if board[i][l1] in num_list and board[i][l1] != '.':
                return False
            else:
                num_list.append(board[i][l1])
        return True

    def checkVertical(self, board, j):
        num_list = []
        for l1 in range(len(board)):
            if board[l1][j] in num_list and board[l1][j] != '.':
                return False
            else:
                num_list.append(board[l1][j])

        return True

    def checkSudoku(self, board, i, j):
        num_list = []
        for l1 in range(i - 2, i + 1):
            for l2 in range(j - 2, j + 1):
                if board[l1][l2] in num_list and board[l1][l2] != '.':
                    return False
                else:
                    num_list.append(board[l1][l2])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i != 0 and j != 0 and (i + 1) % 3 == 0 and (j + 1) % 3 == 0:
                    if self.checkSudoku(board, i, j) is False:
                        return False
                if j == len(board) - 1 and self.checkHorizontal(board, i) is False:
                    return False
                if i == len(board) - 1 and self.checkVertical(board, j) is False:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

    print(solution.isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."]
                                     , [".", "4", ".", "3", ".", ".", ".", ".", "."]
                                     , [".", ".", ".", ".", ".", "3", ".", ".", "1"]
                                     , ["8", ".", ".", ".", ".", ".", ".", "2", "."]
                                     , [".", ".", "2", ".", "7", ".", ".", ".", "."]
                                     , [".", "1", "5", ".", ".", ".", ".", ".", "."]
                                     , [".", ".", ".", ".", ".", "2", ".", ".", "."]
                                     , [".", "2", ".", "9", ".", ".", ".", ".", "."]
                                     , [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
