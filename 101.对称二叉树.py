#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return bool(self.helper(root.left, root.right))  # python3需要转换为bool

    def helper(self, leftnode, rightnode):
        if not leftnode and not rightnode:
            return True
        if leftnode and rightnode and leftnode.val == rightnode.val:
            return self.helper(leftnode.left, rightnode.right) and self.helper(leftnode.right, rightnode.left)         
# @lc code=end

