#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 17:44
# @Author  : Aries
# @Site    : 
# @File    : 18.py
# @Software: PyCharm Community Edition
'''
操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
解题思路：使用递归，交换每个节点及节点的左右子节点，直到其左右子节点为空
注意：这道题因为写了“返回镜像树的根节点”，所以一直考虑返回值的问题，而实际上是不用自己来定义==
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root!=None:
            root.right, root.left=root.left, root.right
            self.Mirror(root.right)
            self.Mirror(root.left)