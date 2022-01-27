"""
66. 加一

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

模拟竖式加法的过程即可
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        jinwei = False
        jinwei_num = 0
        for i in range(len(digits)):
            num = digits[len(digits) - 1 - i]
            if i == 0:
                num += 1

            if jinwei:
                num += jinwei_num
            if num >= 10:
                jinwei_num = num // 10
                jinwei = True
            else:
                jinwei_num = 0
                jinwei = False
            digits[len(digits) - i - 1] = num % 10
        if jinwei:
            digits.insert(0, jinwei_num)
        return digits


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
    print(solution.plusOne([9]))
