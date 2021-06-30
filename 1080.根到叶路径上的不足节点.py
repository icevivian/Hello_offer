#
# @lc app=leetcode.cn id=1080 lang=python3
#
# [1080] 根到叶路径上的不足节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        # 怎么判读一个叶节点该不该删除：当叶节点的总和小于limit的时候。
        # 怎么判断一个非叶节点该不该删除：当它所有的子节点都该删除的时候
        if self.postorder(root, 0, limit):
            return None
        return root
        

    def postorder(self, root, value, limit): # 含义：节点是否要被删除
        if root.left == None and root.right == None:
            return value+root.val < limit 
        left_deleted = True
        right_deleted = True
        if root.left:
            left_deleted = self.postorder(root.left, value+root.val, limit)
        if left_deleted:
            root.left = None
        if root.right:
            right_deleted = self.postorder(root.right, value+root.val, limit)
        if right_deleted:
            root.right = None
        return left_deleted and right_deleted
        

        
# @lc code=end

