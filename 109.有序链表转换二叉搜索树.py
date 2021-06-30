#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        slow1, slow2, fast = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow1 = slow2
            slow2 = slow1.next
        newhead = TreeNode(slow2.val)
        print(slow2.val)
        slow1.next = None
        right = slow2.next
        newhead.left = self.sortedListToBST(head)
        newhead.right = self.sortedListToBST(right)
        return newhead
# @lc code=end

