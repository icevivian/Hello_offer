#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        stk = []
        while root or stk:
            while root:
                res.append(root.val) 
                stk.append(root)
                root = root.left
            root = stk.pop() 
            root = root.right
        return res
# @lc code=end

