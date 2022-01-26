"""
61. 旋转链表

给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

示例 2：
输入：head = [0,1,2], k = 4
输出：[2,0,1]

根据规则计算出需要调转到前面的第一个节点，然后进行指针的操作，始终记得链表处理的时候新增一个头节点之前的pre_head节点，操作会比较方便
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None or k == 0:
            return head
        length = 0
        t = head
        pre_head = ListNode(-1, head)
        while t is not None:
            length += 1
            t = t.next
        if k % length == 0:
            return head
        count = length - k % length
        left = pre_head
        right = head
        for i in range(count):
            left = left.next
            right = right.next
        tail = right
        while tail.next is not None:
            tail = tail.next
        pre_head.next = right
        left.next = None
        tail.next = head

        return pre_head.next


if __name__ == '__main__':
    solution = Solution()
    l5 = ListNode(5)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    head = solution.rotateRight(l1, 2)
    while head is not None:
        print(head.val)
        head = head.next
