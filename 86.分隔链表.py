#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return
        smallnode = ListNode(0)
        largenode = ListNode(0)
        small = smallnode
        large = largenode
        while head:
            print(head.val)
            if head.val >= x:
                large.next = head
                large = large.next
            else:
                small.next = head
                small = small.next
            head = head.next
        large.next = None # 一定要把最后的large之后置为空
        small.next = largenode.next
        return smallnode.next
        
# @lc code=end

