#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate(1, n)
        
    
    def generate(self, left, right):
        # 函数返回的是left,right数能够构成的二叉搜索树的多种组合
        res = []
        # base case
        if left > right:
            res.append(None)
            return res
        # 穷举root节点的所有可能
        for value in range(left, right+1):
            # 递归左右子树的所有合法BST
            leftTree = self.generate(left, value-1)
            rightTree = self.generate(value+1, right)
            for l in leftTree:
                for r in rightTree:
                    # value作为根节点的值
                    newroot = TreeNode(value)
                    newroot.left = l
                    newroot.right = r
                    res.append(newroot)
        return res
# @lc code=end

