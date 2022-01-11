"""
9. 回文数

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

示例 1：
输入：x = 121
输出：true

示例2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。

示例 4：
输入：x = -101
输出：false

将数字转化为字符串判断回文串的形式不满足空间要求
对数字进行纯数字为的运算判断又有可能会溢出数字大小
因此选择判断数字的一半，如果数字的一半与另一半相同则就是回文数
"""
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_len = len(str(x))
        if str_len == 1:
            return True

        behind = []
        front = []
        front_num = x
        behind_num = x
        for i in range(str_len // 2):
            front.append(int(front_num // int(math.pow(10, str_len - i - 1))))
            behind.append(int(behind_num % 10))
            front_num = front_num % int(math.pow(10, str_len - i - 1))
            behind_num = behind_num // 10

        return behind == front


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(12211221))
