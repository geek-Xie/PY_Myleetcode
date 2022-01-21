"""
40. 组合总和 II

给你一个由候选元素组成的集合 candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。

candidates 中的每个元素在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。

示例1:
输入: candidates =[10,1,2,7,6,1,5], target =8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

示例2:
输入: candidates =[2,5,2,1,2], target =5,
输出:
[
[1,2,2],
[5]
]

大体思路与39题类似，但是要求不能重复使用元素，因此每次递归都是用 idx + 1 。另外关键就是返回的答案不能重复， 去重的方法比较关键
"""

import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return

            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]

        freq = sorted(collections.Counter(candidates).items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2([2, 5, 2, 1, 2], 5))
