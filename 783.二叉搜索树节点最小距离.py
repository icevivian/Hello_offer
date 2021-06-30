#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = []
        self.inorderTraversal(root)
        maxa = self.res[-1]-self.res[0]
        for i in range(1,len(self.res)):
            maxa = min(maxa, self.res[i]-self.res[i-1])
        return maxa

    def inorderTraversal(self, root):
        if not root:
            return 
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            cur = stk.pop()
            self.res.append(cur.val)
            root = cur.right

# @lc code=end

