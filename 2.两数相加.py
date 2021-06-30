#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # sign表示前一次相加的进位，l1, l2依次向后走
        sign = 0
        newhead = ListNode(0)
        head = newhead
        while l1 or l2:
            if l1 is None:
                value = l2.val + sign
                l1 = None
                l2 = l2.next 
            elif l2 is None:
                value = l1.val + sign
                l1 = l1.next
                l2 = None
            else:
                value = l1.val + l2.val + sign
                l1 = l1.next
                l2 = l2.next 
            n =  value%10
            sign = value//10   
            newhead.next = ListNode(n)
            newhead = newhead.next
        if sign:
            newhead.next = ListNode(sign)
        return head.next
# @lc code=end

