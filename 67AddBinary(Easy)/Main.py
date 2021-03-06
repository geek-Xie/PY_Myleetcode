"""
67. 二进制求和

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字1和0。

示例1:
输入: a = "11", b = "1"
输出: "100"

示例2:
输入: a = "1010", b = "1011"
输出: "10101"

使用python自带的进制转化工具，现将二进制数转化为十进制数，进行计算后再转化为二进制数即可
"""


class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("11", "1"))
