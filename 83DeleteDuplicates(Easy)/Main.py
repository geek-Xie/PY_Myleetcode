"""
83. 删除排序链表中的重复元素

给定一个已排序的链表的头head，删除所有重复的元素，使每个元素只出现一次。返回 已排序的链表。

示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]
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
        end = head

        if head is None:
            return head

        while end is not None:
            if end.val == start.val:
                end = end.next
            else:
                start.next = end
                start = end

        if start.next is not None:
            start.next = None
        return pre_head.next


if __name__ == '__main__':
    solution = Solution()
    l3 = ListNode(2)
    l2 = ListNode(1, l3)
    l1 = ListNode(1, l2)
    head = solution.deleteDuplicates(l1)

    while head is not None:
        print(head.val)
        head = head.next
