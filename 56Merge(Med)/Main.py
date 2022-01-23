"""
56. 合并区间

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

先将数组列表按照第一个元素的大小进行从小到大的排序，然后从头往后遍历，保存每次遍历之后的最大值和最小值，然后进行判断是否并入一个区间中
"""


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        res = []
        start = 0
        end = 0
        min_num = intervals[0][0]
        max_num = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= max_num:
                end = i
                min_num = min(min_num, intervals[i][0])
                max_num = max(max_num, intervals[i][1])
            else:
                temp_list = [min_num, max_num]
                res.append(temp_list)
                start = i
                end = i
                min_num = intervals[i][0]
                max_num = intervals[i][1]
        if end == len(intervals) - 1:
            min_num = intervals[start][0]
            max_num = intervals[end][1]
            for c_i in range(start, end + 1):
                if intervals[c_i][0] < min_num:
                    min_num = intervals[c_i][0]
                if intervals[c_i][1] > max_num:
                    max_num = intervals[c_i][1]
            temp_list = [min_num, max_num]
            res.append(temp_list)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solution.merge([[1, 4], [0, 0]]))
    print(solution.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
