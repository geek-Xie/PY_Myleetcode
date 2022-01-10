"""
2. 两数相加

给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        wei1 = wei2 = 1
        l1_num = l2_num = 0
        while True:
            if l1.next is None:
                l1_num += l1.val * wei1
                break
            l1_num += l1.val * wei1
            wei1 *= 10
            l1 = l1.next

        while True:
            if l2.next is None:
                l2_num += l2.val * wei2
                break
            l2_num += l2.val * wei2
            wei2 *= 10
            l2 = l2.next
        num = l1_num + l2_num
        num_str = str(num)
        pre_node = None
        for st in num_str:
            node = ListNode(int(st), pre_node)
            pre_node = node
        return pre_node


if __name__ == '__main__':
    l13 = ListNode(3)
    l12 = ListNode(4, l13)
    l11 = ListNode(2, l12)
    l23 = ListNode(4)
    l22 = ListNode(6, l23)
    l21 = ListNode(5, l22)
    solution = Solution()
    node = solution.addTwoNumbers(l11, l21)
