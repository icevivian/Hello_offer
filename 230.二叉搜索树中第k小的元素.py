#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = 0
        self.help(root)
        return self.res

    def help(self, root):
        if not root:
            return 
        self.help(root.left)
        # 中序遍历
        self.k -= 1
        if self.k == 0:
            self.res = root.val
        self.help(root.right) 
            
# @lc code=end

