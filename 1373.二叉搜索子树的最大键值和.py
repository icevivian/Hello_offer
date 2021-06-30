#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.maxsum = 0
        self.traverse(root)
        return self.maxsum
    
    def traverse(self, root):
        # 返回值为[a,b,c,d]，a表示以root为根的子树是否为BST，b表示二叉树的最小值，c表示二叉树的最大值，d表示二叉树所有节点之和
        if not root:
            return [1, float('INF'), -float('INF'), 0]
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        res = [0 for i in range(4)]
        if left[0] and right[0] and root.val > left[2] and root.val < right[1]:
            res[0] = 1
            res[1] = min(left[1], root.val)
            res[2] = max(root.val, right[2])
            res[3] = left[3]+right[3]+root.val
            self.maxsum = max(self.maxsum, res[3])
        return res      
# @lc code=end

