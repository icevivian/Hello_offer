#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        res = self.help(root)
        return True if res else False
        
    def help(self, root):
        if not root:
            return [True, float('INF'),-float('INF')]
        l = self.help(root.left)
        r = self.help(root.right)
        if l and r and l[0] and r[0] and root.val>l[2] and root.val<r[1]:
            return [True, min(root.val, l[1]), max(root.val, r[2])]
        
# @lc code=end

