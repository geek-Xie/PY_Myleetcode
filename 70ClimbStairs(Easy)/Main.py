"""
70. 爬楼梯

假设你正在爬楼梯。需要 n阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

使用动态规划的方法，创建一个和n相同大小的数组，数组的第i个位置的数字表示到达第i个位置的方法数量
因为每次可以跳一格，也可以跳两格，因此f(i) = f(i - 1) + f(i - 2)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        res[1] = 1
        res[2] = 2
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        return res[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(3))
