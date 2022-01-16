"""
31. 下一个排列

实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

示例 4：
输入：nums = [1]
输出：[1]

首先分两步找到i和j
1.从后往前遍历数组，找到第一个比后一个数小的数，为i，即i之后为降序序列
2.在i之后的序列从后往前遍历，找到第一个比i大的数，为j
3.对换i和j的位置
4，将i之后的序列反转，即将降序序列转变为升序序列
"""

from typing import List


class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            t = nums[start]
            nums[start] = nums[end]
            nums[end] = t
            start += 1
            end -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        right = -1
        no = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            if nums[len(nums) - i - 1] < no:
                left = len(nums) - i - 1
                break
            else:
                no = nums[len(nums) - i - 1]
        if left == -1:
            self.reverse(nums, left + 1, len(nums) - 1)
            return
        for i in range(left, len(nums)):
            if nums[len(nums) - i + left - 1] > nums[left]:
                right = len(nums) - i + left - 1
                break
        t = nums[left]
        nums[left] = nums[right]
        nums[right] = t

        self.reverse(nums, left + 1, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    solution.nextPermutation([1, 3, 2])
