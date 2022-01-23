"""
53. 最大子数组和

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组[4,-1,2,1] 的和最大，为6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23

非常经典的动态规划问题，我们设f(i)为到数组nums的第i个位置为止的最大和，那么每个位置的f(i)，我们就只需考虑是在f(i - 1)的基础上加上nums[i]还是 num[i]单独表示，
取这两者的较大值就是当前位置能够达到的最大的和
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_list = [0 for _ in range(len(nums))]
        max_list[0] = nums[0]
        for index_ in range(1, len(nums)):
            max_list[index_] = max(nums[index_], max_list[index_ - 1] + nums[index_])
        return max(max_list)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1]))
