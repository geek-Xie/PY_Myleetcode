"""
15. 三数之和

给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]

首先要求不重复，因此使用三重循环很有可能超出时间范围，因此使用排序+指针的思路
首先固定第一个数first，然后第二重循环中，第二个数second正向走，第三个third数倒着走
每一次先验证first和second是否和之前一样，一样的话直接continue
然后根据数组已经排序的特性，可以对一些情况进行优点的判断。
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = len(nums) - 1
            target = -nums[first]
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if third == second:
                    break
                if nums[second] + nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([]))
    print(solution.threeSum([0]))
