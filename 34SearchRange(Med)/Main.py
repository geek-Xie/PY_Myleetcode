"""
34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

进阶：

你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

因为是已经排好序的数组，使用双指针，从首尾两个方向查找target
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target < nums[0] or target > nums[len(nums) - 1]:
            return [-1, -1]
        start_index = -1
        end_index = -1
        left = 0
        right = len(nums) - 1
        left_flag = True
        right_flag = True
        while left <= right and (left_flag or right_flag):
            if nums[left] == target:
                start_index = left
                left_flag = False
            if nums[right] == target:
                end_index = right
                right_flag = False
            if left_flag:
                left += 1
            if right_flag:
                right -= 1
        return [start_index, end_index]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
