"""
6. Z 字形变换

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z 字形排列。

比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        num_matrix = []
        for row in range(numRows):
            line = []
            num_matrix.append(line)
        line_count = 0
        increase = True
        for word in s:
            if line_count == numRows - 1:
                increase = False
            if line_count == 0:
                increase = True
            num_matrix[line_count].append(word)
            if increase:
                line_count += 1
            else:
                line_count -= 1

        res_str = ''
        for line in num_matrix:
            for word in line:
                res_str += word
        return res_str


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert('AB', 1))
