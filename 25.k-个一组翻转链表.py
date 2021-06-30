#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        a,b = head, head
        for i in range(k):
            if not b:
                return head
            b = b.next
        newroot = self.reverse(a,b)
        a.next = self.reverseKGroup(b,k)
        return newroot
    def reverse(self, a, b):
        prev = None
        cur, net = a,a
        while cur != b:
            net = cur.next
            cur.next = prev
            prev = cur
            cur = net
        return prev
# @lc code=end

