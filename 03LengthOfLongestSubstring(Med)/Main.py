"""
3.重复字符的最长子串

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)
        max_count = 0
        if str_len == 0:
            return 0
        if str_len == 1:
            return 1
        for i in range(str_len):
            word_set = set()
            word_set.add(s[i])
            count = 1
            for j in range(i + 1, str_len):
                if s[j] not in word_set:
                    word_set.add(s[j])
                    count += 1
                else:
                    break
            if max_count < count:
                max_count = count
        return max_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("au"))
