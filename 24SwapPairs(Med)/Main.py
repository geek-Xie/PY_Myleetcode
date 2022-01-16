"""
24. 两两交换链表中的节点

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

使用一个head的前驱结点来解决这类问题往往会比较方便
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p_head = ListNode(0)
        p_head.next = head
        if head is None:
            return p_head.next
        s_head = p_head
        l_head = head
        r_head = head.next
        index_ = 0
        while l_head is not None and r_head is not None:
            if index_ % 2 == 0:
                t_node = r_head.next
                l_head.next = t_node
                r_head.next = l_head
                t = r_head
                r_head = l_head
                l_head = t
                if index_ == 0:
                    p_head.next = l_head
                else:
                    s_head.next = l_head
            index_ += 1
            l_head = l_head.next
            r_head = r_head.next
            s_head = s_head.next

        return p_head.next


if __name__ == '__main__':
    solution = Solution()
    l4 = ListNode(4)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    head = solution.swapPairs(l1)

    while head is not None:
        print(head.val)
        head = head.next
