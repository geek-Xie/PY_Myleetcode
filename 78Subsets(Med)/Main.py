"""
78. 子集

给你一个整数数组nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

和77题组合的思路类似，区别在于子集不需要对当前组合的长度有要求，只要不重复就可以添加到结果之中
"""

from typing import List


class Solution:
    def dfs(self, res, nums, cur_combine, cur_index):
        if cur_combine[:] not in res:
            res.append(cur_combine[:])
        if cur_index >= len(nums):
            return

        cur_combine.append(nums[cur_index])
        self.dfs(res, nums, cur_combine, cur_index + 1)
        # print(cur_combine)
        # exit()
        cur_combine.pop()
        self.dfs(res, nums, cur_combine, cur_index + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.dfs(res, nums, [], 0)

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
