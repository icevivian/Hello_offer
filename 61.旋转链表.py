#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        slow, fast = head, head

        # fast前进k步，但是有可能链表长度小于k
        for i in range(k):
            fast = fast.next
            if fast == None:       
                step = k%(i + 1)
                fast = head
                for i in range(step):
                    fast = fast.next
                break

        if fast == slow:
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead
            
# @lc code=end

