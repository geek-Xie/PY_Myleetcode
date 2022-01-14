"""
16. 最接近的三数之和

给你一个长度为 n 的整数数组nums和 一个目标值target。请你从 nums 中选出三个整数，使它们的和与target最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

示例 2：
输入：nums = [0,0,0], target = 1
输出：0

思路与三数之和类似，只是增加了一个临界点时候的绝对值差距大小判断
"""


import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        mini = sys.maxsize
        res = 0
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            rest = target - nums[first]
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                third = len(nums) - 1
                if second == third:
                    break
                while second < third and nums[second] + nums[third] > rest:
                    if second == third - 1:
                        break
                    third -= 1

                    if nums[second] + nums[third] < rest:
                        c_mini = min(abs(nums[first] + nums[second] + nums[third] - target),
                                         abs(nums[first] + nums[second] + nums[third + 1] - target))
                        if c_mini < mini:
                            mini = c_mini
                            if abs(nums[first] + nums[second] + nums[third] - target) < abs(nums[first] + nums[second] + nums[third + 1] - target):
                                res = nums[first] + nums[second] + nums[third]
                            else:
                                res = nums[first] + nums[second] + nums[third + 1]

                c_mini = abs(nums[first] + nums[second] + nums[third] - target)
                if c_mini < mini:
                    mini = c_mini
                    res = nums[first] + nums[second] + nums[third]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([1, 2, 5, 10, 11], 12))
