#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        # 左右节点分别遍历
        leftNode = self.flatten(root.left)
        rightNode = self.flatten(root.right)
        
        # 后序遍历：先把展开的左边接到右节点，然后把原本的右节点接到当前右节点的下面
        root.right = leftNode
        root.left = None

        p = root
        while p.right:
            p = p.right 
        p.right = rightNode
        return root


# @lc code=end

