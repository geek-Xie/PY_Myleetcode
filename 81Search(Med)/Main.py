"""
81. 搜索旋转排序数组 II

已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，
则返回 true ，否则返回 false 。

你必须尽可能减少整个操作步骤。

示例1：
输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true

示例2：
输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        max_num = nums[len(nums) - 1]
        min_num = nums[0]
        max_index = len(nums) - 1
        min_index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                max_num = nums[i - 1]
                min_num = nums[i]
                max_index = i - 1
                min_index = i
                break
        if target < min_num or target > max_num:
            return False
        if nums[0] <= target <= max_num:
            for i in range(max_index + 1):
                if target == nums[i]:
                    return True
        elif min_num <= target <= nums[len(nums) - 1]:
            for i in range(min_index, len(nums)):
                if target == nums[i]:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([2, 5, 6, 0, 0, 1, 2], 0))
    print(solution.search([2, 5, 6, 0, 0, 1, 2], 3))
    print(solution.search([1, 3], 3))
