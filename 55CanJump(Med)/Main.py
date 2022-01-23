"""
55. 跳跃游戏

给定一个非负整数数组nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

示例1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

此题与45题的思路类似，只是不再计算步数，只判断能否到达最后一个位置，因此还是在每次的跳跃范围能选择下一步能够跳得最远的位置进行跳跃
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        index_ = 0
        while index_ < len(nums):
            if nums[index_] == 0 and index_ < len(nums) - 1:
                return False
            next_index = []
            next_dict = {}
            for i in range(1, nums[index_] + 1):
                if index_ + i < len(nums) - 1:
                    next_index.append(nums[index_ + i] + i)
                    next_dict[nums[index_ + i] + i] = i
                else:
                    return True
            index_ += next_dict[max(next_index)]
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump([2, 3, 1, 1, 4]))
    print(solution.canJump([3, 2, 1, 0, 4]))
    print(solution.canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))
