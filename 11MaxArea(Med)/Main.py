"""
11. 盛最多水的容器

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。

示例 2：
输入：height = [1,1]
输出：1

示例 3：
输入：height = [4,3,2,1,4]
输出：16

示例 4：
输入：height = [1,2,1]
输出：2

首先从首尾开始，因为容器的面积实际上取决于小的一方，因此每次移动指针的时候移动当前值较小的指针，并计算这个时候的容器的面积与最大的面积对比，最后输出最大面积即可
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        first = 0
        end = len(height) - 1
        while first < end:
            cur_area = min(height[first], height[end]) * (end - first)
            if res < cur_area:
                res = cur_area
            if height[first] <= height[end]:
                first += 1
            else:
                end -= 1

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,1]))
