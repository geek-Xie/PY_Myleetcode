"""
57. 插入区间

给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例1：
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

示例 2：
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10]重叠。

示例 3：
输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]

示例 4：
输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]

示例 5：
输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]

模拟判断过程，分为当前区间在新加入区间左侧，右侧以及有交集三种情况进行判断
"""


from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        left = newInterval[0]
        right = newInterval[1]
        placed = False

        for l, r in intervals:
            if r < left:
                res.append([l, r])
            elif l > right:
                if not placed:
                    res.append([left, right])
                    placed = True
                res.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)

        if not placed:
            res.append([left, right])

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.insert([[1, 3], [6, 9]], [2, 5]))
    print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9]))
    print(solution.insert([[1, 5]], [2, 3]))
    print(solution.insert([[1, 5]], [2, 7]))
    print(solution.insert([[1, 5]], [6, 8]))
