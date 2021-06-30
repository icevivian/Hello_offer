#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = []
        q.append(root)
        depth = 1
        while q:
            sz = len(q)
            # 队列中每一个节点进行遍历
            for i in range(sz):
                node = q.pop(0)
                # 判断是否到达终点
                if node.left == None and node.right == None:
                    return depth
                # 将相邻节点放入队列中
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # 步数更新
            depth += 1
        return depth
# @lc code=end

