"""
105. 从前序与中序遍历序列构造二叉树

给定两个整数数组preorder 和 inorder，其中preorder 是二叉树的先序遍历， inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

示例 2:
输入: preorder = [-1], inorder = [-1]
输出: [-1]

使用递归的方法，对树进行构建
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        node_dict = {}
        for i in range(n):
            node_dict[inorder[i]] = i

        return self.mybuildTree(node_dict, preorder, inorder, 0, n - 1, 0, n - 1)

    def mybuildTree(self, node_dict, preorder, inorder, preorder_left, preorder_right, inorder_left,
                    inorder_right) -> TreeNode:
        if preorder_left > preorder_right:
            return None
        preorder_root = preorder_left
        inorder_root = node_dict[preorder[preorder_root]]

        root = TreeNode(preorder[preorder_root])
        left_tree_size = inorder_root - inorder_left
        root.left = self.mybuildTree(node_dict, preorder, inorder, preorder_left + 1, preorder_left + left_tree_size,
                                     inorder_left, inorder_root - 1)
        root.right = self.mybuildTree(node_dict, preorder, inorder, preorder_left + left_tree_size + 1, preorder_right,
                                      inorder_root + 1, inorder_right)
        return root


if __name__ == '__main__':
    solution = Solution()
