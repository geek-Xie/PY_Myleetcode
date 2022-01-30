"""
77. 组合

给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2：
输入：n = 1, k = 1
输出：[[1]]

使用递归回溯的思想，有两种情况，选择当前数字，就把数字加入当前组合，向后递归
回溯后不选择当前数字，则跳过，进入对下一个数字的递归中
"""


from typing import List


class Solution:
    def dfs(self, res, n, k, cur_combine, cur_num):
        if len(cur_combine) == k:
            res.append(cur_combine[:])
            return
        if cur_num > n:
            return
        cur_combine.append(cur_num)
        self.dfs(res, n, k, cur_combine, cur_num + 1)
        cur_combine.pop()
        self.dfs(res, n, k, cur_combine, cur_num + 1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        self.dfs(res, n, k, [], 1)

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
