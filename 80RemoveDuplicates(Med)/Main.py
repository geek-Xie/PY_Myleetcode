"""
80. 删除有序数组中的重复项 II

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。

在循环遍历数组的时候记录相同数字的开始下标和结束下标，并且记录数字的出现次数，然后在原数组进行位置的变化
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        start_index = 0
        duplicate_num = nums[0]
        duplicate_count = 0
        end_index = 0
        cur_len = len(nums)
        while end_index < cur_len:
            if nums[end_index] == duplicate_num:
                duplicate_count += 1
                end_index += 1
                if duplicate_count > 2 and end_index == cur_len:
                    del_num = end_index - start_index - 2
                    return len(nums[:end_index - del_num])
            else:
                if duplicate_count > 2:
                    del_num = end_index - start_index - 2
                    for i in range(end_index, cur_len):
                        nums[i - del_num] = nums[i]
                    cur_len = cur_len - del_num
                    start_index = start_index + 2
                    end_index = start_index
                    duplicate_count = 1
                    duplicate_num = nums[start_index]
                else:
                    duplicate_num = nums[end_index]
                    start_index = end_index
                    duplicate_count = 1
        return len(nums[:end_index])


if __name__ == '__main__':
    solution = Solution()
    # print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))
    # print(solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(solution.removeDuplicates([1, 1, 1]))
