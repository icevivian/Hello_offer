#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        self.successor = None
        if left==1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

    def reverseN(self, head, n):
        # 翻转head为头节点的链表的前n个节点，并返回头节点
        if n==1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last
# @lc code=end

