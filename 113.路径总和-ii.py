#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # DFS
        if not root:
            return []
        trace = [root.val]
        self.res = []
        self.backtrace(root, trace, targetSum)
        return self.res

    def backtrace(self, root, trace, targetSum):
        if root.left is None and root.right is None:
            if sum(trace)==targetSum:
                self.res.append(list(trace))
            return
        if root.left:
            trace.append(root.left.val)
            self.backtrace(root.left, trace, targetSum)
            trace.pop()
        if root.right:
            trace.append(root.right.val)
            self.backtrace(root.right, trace, targetSum)
            trace.pop()
# @lc code=end

