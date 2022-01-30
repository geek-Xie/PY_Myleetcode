"""
79. 单词搜索

给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

使用递归，i，j表示当前的坐标，k表示单词的第k个位置，我们从当前(i,j)位置的四个方向进行探索
如果碰到不匹配的直接返回False，匹配的话就观察单词的下一个字母是否匹配，直到检查完整个单词
"""

from typing import List


class Solution:
    def find(self, visited, i, j, k, board, word):
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        visited[i][j] = True
        result = False
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in direction:
            newi, newj = i + di, j + dj
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                if visited[newi][newj] is False:
                    if self.find(visited, newi, newj, k + 1, board, word):
                        result = True
                        break
        visited[i][j] = False
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = []
        for _ in range(len(board)):
            row = []
            for _ in range(len(board[0])):
                row.append(False)
            visited.append(row)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.find(visited, i, j, 0, board, word):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED'))
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'SEE'))
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCB'))
    print(solution.exist([["A"]], 'A'))
    print(solution.exist([["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]], 'abcdefg'))
