"""
86. 分隔链表

给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

示例 1：
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]

示例 2：
输入：head = [2,1], x = 2
输出：[1,2]

使用两个list分别保存大于等于和小于特定值的节点值，然后按顺序构建新的链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = []
        right = []
        while head is not None:
            if head.val < x:
                left.append(head.val)
            else:
                right.append(head.val)
            head = head.next

        pre_head = ListNode(-1)
        p = pre_head
        for l_val in left:
            node = ListNode(l_val)
            p.next = node
            p = p.next
        for r_val in right:
            node = ListNode(r_val)
            p.next = node
            p = p.next

        return pre_head.next


if __name__ == '__main__':
    solution = Solution()
    # l6 = ListNode(2)
    # l5 = ListNode(5, l6)
    # l4 = ListNode(2, l5)
    # l3 = ListNode(3, l4)
    # l2 = ListNode(4, l3)
    # l1 = ListNode(1, l2)

    l2 = ListNode(1)
    l1 = ListNode(2, l2)

    head = solution.partition(l1, 2)
    while head is not None:
        print(head.val)
        head = head.next
