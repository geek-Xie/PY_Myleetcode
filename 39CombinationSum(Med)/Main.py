"""
39. 组合总和

给你一个 无重复元素 的整数数组candidates 和一个目标整数target，找出candidates中可以使数字和为目标数target 的 所有不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为target 的不同组合数少于 150 个。

示例1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

示例2：
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：
输入: candidates = [2], target = 1
输出: []

示例 4：
输入: candidates = [1], target = 1
输出: [[1]]

示例 5：
输入: candidates = [1], target = 2
输出: [[1,1]]

还是一个递归的思路，此题需要多看多理解多记忆！
"""

from typing import List


class Solution:
    def findCombination(self, res, cur, candidates, target, idx):
        if target == 0:
            res.append(cur[:])
            return
        if idx == len(candidates):
            return
        self.findCombination(res, cur, candidates, target, idx + 1)

        if target - candidates[idx] >= 0:
            cur.append(candidates[idx])
            self.findCombination(res, cur, candidates, target - candidates[idx], idx)
            cur.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        self.findCombination(res, [], candidates, target, 0)

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 5], 8))
