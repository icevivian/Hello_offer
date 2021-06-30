#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxnum = -float('INF')
        self.help(root)
        return self.maxnum

    def help(self, root):
        # 函数输入为root，输出为该节点下的单侧最大值
        if not root:
            return 0
        left = max(self.help(root.left), 0)
        right = max(self.help(root.right), 0)
        self.maxnum = max(self.maxnum, left+right+root.val)
        return max(left, right)+root.val
# @lc code=end

