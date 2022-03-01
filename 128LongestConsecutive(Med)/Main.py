"""
128. 最长连续序列

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。


示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_len = 0
        cur_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1

        max_len = max(max_len, cur_len)

        return max_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(solution.longestConsecutive([1, 2, 0, 1]))
