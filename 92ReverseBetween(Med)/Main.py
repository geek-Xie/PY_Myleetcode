"""
92. 反转链表 II

给你单链表的头指针 head 和两个整数left 和 right ，其中left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例 1：
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

示例 2：
输入：head = [5], left = 1, right = 1
输出：[5]

使用一个额外的列表空间存储要反转的节点，然后按照倒序的顺序对节点进行放置
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        pre_head = ListNode(-1, head)
        pre_start = pre_head
        start = pre_head
        last = pre_head
        be_last = pre_head
        for _ in range(left - 1):
            pre_start = pre_start.next
        for _ in range(left):
            start = start.next
        for _ in range(right):
            last = last.next
        for _ in range(right + 1):
            be_last = be_last.next
        nodes = []
        while start != last:
            nodes.append(start)
            start = start.next
        nodes.append(last)
        pre_start.next = nodes[len(nodes) - 1]
        pre_start = pre_start.next
        for i in range(1, len(nodes)):
            pre_start.next = nodes[len(nodes) - i - 1]
            pre_start = pre_start.next
        pre_start.next = be_last

        return pre_head.next


if __name__ == '__main__':
    solution = Solution()
    l5 = ListNode(5)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    head = solution.reverseBetween(l1, 2, 4)
    while head is not None:
        print(head.val)
        head = head.next
