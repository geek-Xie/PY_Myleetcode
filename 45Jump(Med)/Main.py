"""
45. 跳跃游戏 II

给你一个非负整数数组nums ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

示例 1:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。

示例 2:
输入: nums = [2,3,0,1,4]
输出: 2

本题使用贪心的思想，从左到右遍历数组，在每一步的范围内搜寻下一步的落脚点时，优先考虑走得远的为下一步的落脚点
"""


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


if __name__ == '__main__':
    solution = Solution()
    print(solution.jump([2, 3, 1, 1, 4]))
