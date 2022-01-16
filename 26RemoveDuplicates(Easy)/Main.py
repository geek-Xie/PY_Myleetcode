"""
26. 删除有序数组中的重复项

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

注意题目要求的是在原数组上进行修改，而不是新建一个数组存储结果
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res_len = 1
        cur_num = nums[0]
        cur_index = 1

        for i in range(1, len(nums)):
            if nums[i] == cur_num:
                continue
            nums[cur_index] = nums[i]
            res_len += 1
            cur_num = nums[i]
            cur_index += 1
        return res_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([]))
    print(solution.removeDuplicates([1, 1, 2]))
