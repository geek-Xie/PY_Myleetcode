"""
49. 字母异位词分组

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]

使用字典，根据包含的字母作为字典的key值把单词进行分类
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        res = []
        words_dict = {}
        for word in strs:
            char_list = []
            for c in word:
                char_list.append(c)
            char_list.sort()
            char_key = ''
            for char in char_list:
                char_key += char
            if char_key not in words_dict:
                words_dict[char_key] = []
                words_dict[char_key].append(word)
            else:
                words_dict[char_key].append(word)
        for key in words_dict.keys():
            sub_res = []
            for word in words_dict[key]:
                sub_res.append(word)
            res.append(sub_res)

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
