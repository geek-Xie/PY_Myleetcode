"""
46. 全排列

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]

非常非常经典的回溯递归题目，设定一个标记数组来记录当前位置的元素是否被选到
"""

from typing import List


class Solution:
    def dfs(self, marked, nums, res, cur):
        if len(cur) == len(nums):
            res.append(cur[:])
            return
        for i in range(len(nums)):
            if marked[i] is True:
                continue
            marked[i] = True
            cur.append(nums[i])
            self.dfs(marked, nums, res, cur)
            marked[i] = False
            cur.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        marked = [False for _ in range(len(nums))]

        self.dfs(marked, nums, res, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
