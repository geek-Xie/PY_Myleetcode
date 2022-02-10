"""
95. 不同的二叉搜索树 II

给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

示例 1：
输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

示例 2：
输入：n = 1
输出：[[1]]

通过遍历所有节点作为根结点，选择出当前根结点所有的左子树和右子树，然后进行拼接成为当前的一种情况
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generating(self, start, end):
        allTrees = []
        if start > end:
            allTrees.append(None)
            return allTrees
        for i in range(start, end + 1):
            leftTrees = self.generating(start, i - 1)

            rightTrees = self.generating(i + 1, end)

            for left in leftTrees:
                for right in rightTrees:
                    currNode = TreeNode(i)
                    currNode.left = left
                    currNode.right = right
                    allTrees.append(currNode)

        return allTrees

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.generating(1, n)


if __name__ == '__main__':
    solution = Solution()
    trees = solution.generateTrees(3)
