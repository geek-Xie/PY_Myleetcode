"""
94. 二叉树的中序遍历

给定一个二叉树的根节点 root ，返回它的 中序遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[2,1]

示例 5：
输入：root = [1,null,2]
输出：[1,2]
"""

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, res, root):
        if root.left is not None:
            self.dfs(res, root.left)
        res.append(root.val)

        if root.right is not None:
            self.dfs(res, root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        self.dfs(res, root)

        return res


if __name__ == '__main__':
    solution = Solution()
    t3 = TreeNode(3)
    t2 = TreeNode(2, t3, None)
    t1 = TreeNode(1, None, t2)
    print(solution.inorderTraversal(t1))
