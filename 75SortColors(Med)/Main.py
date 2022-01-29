"""
75. 颜色分类

给定一个包含红色、白色和蓝色、共n 个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。

必须在不使用库的sort函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

分两次循环，第一次循环先处理2的位置，第二次循环处理1的位置
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        last = len(nums) - 1
        # [2, 0, 2, 1, 1, 0]
        while first < last:
            while nums[first] != 2 and first < last:
                first += 1
            while nums[last] == 2 and first < last:
                last -= 1
            t = nums[last]
            nums[last] = nums[first]
            nums[first] = t
            first += 1
            last -= 1

        first = 0
        last = len(nums) - 1
        while first < last:
            while nums[first] != 1 and first < last:
                first += 1
            while nums[last] >= 1 and first < last:
                last -= 1
            t = nums[last]
            nums[last] = nums[first]
            nums[first] = t
            first += 1
            last -= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortColors([2, 0, 2, 1, 1, 0]))
    print(solution.sortColors([2, 0, 1]))
