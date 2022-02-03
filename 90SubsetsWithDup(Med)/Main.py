"""
90. 子集 II

给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

使用dfs的思路，每次有一个新组合就进行去重的添加，然后对于当前坐标下的数字，可以选择添加与不添加两种方式
"""

from typing import List


class Solution:
    def dfs(self, res, nums, cur_subset, cur_index):
        if cur_subset not in res:
            res.append(cur_subset[:])
        if cur_index == len(nums):
            return
        self.dfs(res, nums, cur_subset, cur_index + 1)
        cur_subset.append(nums[cur_index])
        self.dfs(res, nums, cur_subset, cur_index + 1)
        cur_subset.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(res, nums, [], 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([1, 2, 2]))
    print(solution.subsetsWithDup([0]))
