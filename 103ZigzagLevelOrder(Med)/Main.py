"""
103. 二叉树的锯齿形层序遍历

给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]

使用常规的广度优先遍历方法对树进行遍历，然后根据层数调整正序和反序
"""

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = collections.deque([root])
        res = []
        flag = 0

        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if flag % 2 == 0:
                res.append(temp)
            else:
                res.append(temp[::-1])
            flag += 1
        return res


if __name__ == '__main__':
    pass
