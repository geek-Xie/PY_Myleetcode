"""
113. 路径总和 II

给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：[]

示例 3：
输入：root = [1,2], targetSum = 0
输出：[]
"""

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(res, path, root, targetSum)

        return res

    def dfs(self, res, path, root, targetSum):
        if root is None:
            return
        path.append(root.val)
        targetSum -= root.val
        if root.left is None and root.right is None and targetSum == 0:
            res.append(path[:])
        self.dfs(res, path, root.left, targetSum)
        self.dfs(res, path, root.right, targetSum)
        path.pop()


if __name__ == '__main__':
    pass
