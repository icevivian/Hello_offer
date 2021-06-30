#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left, right = root, root
        hl, hr = 0, 0
        while left:
            left = left.left
            hl+=1
        while right:
            right = right.right
            hr +=1
        if hl == hr:
            return 2**hr-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
# @lc code=end

