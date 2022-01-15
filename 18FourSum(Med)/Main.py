"""
18. 四数之和

给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]（若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d< n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

原理同三数之和
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            rest_1 = target - nums[first]
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                rest_2 = rest_1 - nums[second]
                for third in range(second + 1, len(nums)):
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        continue
                    forth = len(nums) - 1
                    while third < forth and nums[third] + nums[forth] > rest_2:
                        forth -= 1
                    if third == forth:
                        break
                    if nums[third] + nums[forth] == rest_2:
                        res.append([nums[first], nums[second], nums[third], nums[forth]])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
