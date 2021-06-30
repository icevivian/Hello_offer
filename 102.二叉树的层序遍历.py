#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root] # queue存储全部的数据，由ToBePrinted来告诉queue上一层是否打印完毕
        res, subres = [], [] 
        ToBePrinted=1
        NextLevel=0
        while queue:
            node = queue.pop(0)
            ToBePrinted -= 1
            subres.append(node.val)
            if node.left:
                queue.append(node.left)
                NextLevel+=1
            if node.right:
                queue.append(node.right)
                NextLevel+=1
            if ToBePrinted == 0:
                res.append(subres)
                ToBePrinted = NextLevel
                subres = []
                NextLevel = 0
        return res
# @lc code=end

