"""
43. 字符串相乘

给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例2:
输入: num1 = "123", num2 = "456"
输出: "56088"

使用模拟竖式乘法的方式
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        result_list = []
        weishu = 1
        for i in range(len(num1)):
            int_1 = int(num1[len(num1) - i - 1]) * int(num2)
            result_list.append(int_1 * weishu)
            weishu = weishu * 10
        res = 0
        for n in result_list:
            res += n
        return str(res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.multiply('123', '456'))
