#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def getmin(root):
            while root.left:
                root = root.left
            return root

        if not root:
            return
        if root.val == key:
            # 删除
            if root.left == None and root.right == None:
                return None
            if root.left == None and root.right:
                return root.right
            if root.right == None and root.left:
                return root.left
            if root.right and root.left:
                minr = getmin(root.right)
                root.val = minr.val
                root.right = self.deleteNode(root.right, minr.val)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
        
        
# @lc code=end

