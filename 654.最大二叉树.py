#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        maxnum = nums[0]
        maxindex = 0
        for index in range(1,len(nums)):
            if nums[index]>maxnum:
                maxindex = index
                maxnum = nums[index]
        root = TreeNode(maxnum)
        root.left = self.constructMaximumBinaryTree(nums[:maxindex])
        root.right = self.constructMaximumBinaryTree(nums[maxindex+1:]) 
        return root
# @lc code=end

