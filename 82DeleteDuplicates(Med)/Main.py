"""
82. 删除排序链表中的重复元素 II

给定一个已排序的链表的头head ，删除原始链表中所有重复数字的节点，只留下不同的数字。返回 已排序的链表。

示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：
输入：head = [1,1,1,2,3]
输出：[2,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre_head = ListNode(-1, head)
        start = head
        if head is None:
            return head
        end = head.next
        pre_start = pre_head
        while end is not None:
            if end.val == start.val:
                end = end.next
            else:
                if start.next == end:
                    pre_start = pre_start.next
                    start = start.next
                    end = end.next
                else:
                    pre_start.next = end
                    start = end
        if start.next is not None:
            pre_start.next = None

        return pre_head.next


if __name__ == '__main__':
    solution = Solution()

    # l7 = ListNode(5)
    # l6 = ListNode(4, l7)
    # l5 = ListNode(4, l6)
    # l4 = ListNode(3, l5)
    # l3 = ListNode(3, l4)
    # l2 = ListNode(2, l3)
    # l1 = ListNode(1, l2)

    # l5 = ListNode(3)
    # l4 = ListNode(2, l5)
    # l3 = ListNode(1, l4)
    # l2 = ListNode(1, l3)
    # l1 = ListNode(1, l2)

    l2 = ListNode(1)
    l1 = ListNode(1, l2)

    head = solution.deleteDuplicates(l1)
    while head is not None:
        print(head.val)
        head = head.next
