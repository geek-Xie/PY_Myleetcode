"""
33. 搜索旋转排序数组

整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ...
nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为[4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回-1。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1

可以使用暴力搜索的方式，但是可能会超出时间限制
因此可以利用数组排序反转的特性，减少不必要的时间损耗
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        large_index = len(nums) - 1
        small_index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                large_index = i - 1
                small_index = i
        if nums[large_index] < target or nums[small_index] > target:
            return -1
        if nums[0] <= target <= nums[large_index]:
            for i in range(large_index + 1):
                if nums[i] == target:
                    return i
        elif nums[small_index] <= target <= nums[len(nums) - 1]:
            for i in range(small_index, len(nums)):
                if target == nums[i]:
                    return i

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 4))
