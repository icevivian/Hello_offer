#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue,queue2 = [root],[]
        res, subres = [], []
        flag = 1
        while queue:
            p = queue.pop()
            subres.append(p.val)
            if flag == 1:
                if p.left:
                    queue2.append(p.left)
                if p.right:
                    queue2.append(p.right)
            else:
                if p.right:
                    queue2.append(p.right)
                if p.left:
                    queue2.append(p.left)
            if not queue:
                res.append(subres)
                queue = queue2
                queue2 = []
                subres = []
                flag = 1-flag             
        return res
# @lc code=end

