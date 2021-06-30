#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.memo = dict()
        self.res = list()
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return '#'
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        # 后序遍历
        traversevalue = str(left)+','+str(right)+','+str(root.val)
        if traversevalue in self.memo:
            self.memo[traversevalue] += 1
            if self.memo[traversevalue] == 2:
                self.res.append(root)
        else:
            self.memo[traversevalue]=1
        return traversevalue
# @lc code=end

