"""
19. 删除链表的倒数第 N 个结点

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p_head = head
        length = 1
        while p_head.next is not None:
            length += 1
            p_head = p_head.next
        p_head = head
        if length == n and length > 1:
            return head.next
        for i in range(length - n - 1):
            p_head = p_head.next
        if p_head.next is None:
            return None
        else:
            p_head.next = p_head.next.next

        return head


if __name__ == '__main__':
    solution = Solution()
    # l5 = ListNode(5)
    # l4 = ListNode(4, l5)
    # l3 = ListNode(3, l4)
    # l2 = ListNode(2, l3)
    l2 = ListNode(2)
    l1 = ListNode(1, l2)
    head = solution.removeNthFromEnd(l1, 2)
    while head is not None:
        print(head.val)
        head = head.next
