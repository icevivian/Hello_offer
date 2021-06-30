#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        while n:
            fast = fast.next
            n -= 1
        if fast == None:
            return head.next # 如果快指针已经走到头了，说明头节点就是需要删除的节点
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        last = slow.next.next
        slow.next = last
        return head
# @lc code=end

