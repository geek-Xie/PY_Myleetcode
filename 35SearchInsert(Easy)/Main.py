"""
35. 搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4

示例 4:
输入: nums = [1,3,5,6], target = 0
输出: 0

示例 5:
输入: nums = [1], target = 0
输出: 0

因为有时间复杂度要求，所以不能采用从头开始循环遍历的方法，使用折半查找
"""


from typing import List


class Solution:
    def getIndex(self, res, nums, start, end, target):
        mid = int((start + end) / 2)
        if nums[mid] == target:
            res.append(mid)
            return
        if start == end:
            if target > nums[end]:
                res.append(len(nums))
                return
            res.append(mid)
            return
        if nums[mid] > target:
            self.getIndex(res, nums, start, mid, target)
        else:
            self.getIndex(res, nums, mid + 1, end, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        res = []
        self.getIndex(res, nums, 0, len(nums) - 1, target)
        return res[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 7))
