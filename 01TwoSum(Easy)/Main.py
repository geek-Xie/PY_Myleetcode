from typing import List

"""
1. 两数之和

给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, first in enumerate(nums):
            rest = target - first
            rest_list = nums[idx + 1:]
            index_ = idx + 1
            for second in rest_list:
                if second == rest:
                    return [idx, index_]
                else:
                    index_ += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3, 2, 3], 6))
