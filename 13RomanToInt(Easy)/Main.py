"""
罗马数字包含以下七种字符：I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。
这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。

示例1:
输入:s = "III"
输出: 3

示例2:
输入:s = "IV"
输出: 4

示例3:
输入:s = "IX"
输出: 9

示例4:
输入:s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例5:
输入:s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

首先还是建立一个罗马数字和整数的对应字典，然后对于输入的罗马数字依次使用从大到小的罗马数字表示进行匹配，直到将罗马数字遍历完全
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        s_index = 0
        res = 0
        while s_index < len(s):
            for key in roman_dict.keys():
                if s[s_index: s_index + len(key)] == key:
                    res += roman_dict[key]
                    s_index += len(key)
                    break
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt('LVIII'))
