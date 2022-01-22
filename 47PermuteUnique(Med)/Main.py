"""
47. 全排列 II

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

与46题目思路相同，在添加的时候多一个判定重复的环节
"""


from typing import List


class Solution:
    def dfs(self, res, cur, nums, marked):
        if len(cur) == len(nums):
            if cur not in res:
                res.append(cur[:])
            return

        for i in range(len(nums)):
            if marked[i] is True:
                continue
            cur.append(nums[i])
            marked[i] = True
            self.dfs(res, cur, nums, marked)
            marked[i] = False
            cur.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        marked = [False for _ in range(len(nums))]

        self.dfs(res, [], nums, marked)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))
