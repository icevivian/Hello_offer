#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 20:46
# @Author  : Aries
# @Site    : 
# @File    : 4.py
# @Software: PyCharm Community Edition
'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
解题思路：首先明白前序遍历与中序遍历:前序遍历是根，左，右；中序遍历是左，根，右。这里的前，中，后都是针对“根”而言的。
        因此前序遍历的第一位数是父节点，然后利用中序遍历序列找到左边树和右边树，对左边树和右边树递归采用该方法直到叶节点。
代码实现：这里的重建二叉树，就是指使用它原本的定义方法，找到每个根的左右节点上的定义。这里应该像上面定义TreeNode一样对每个树节点进行定义。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
            return None
        if len(pre)==1:   #当前序遍历只有一个数时说明找到了根节点，可以返回该根节点TreeNode
            return TreeNode(pre[0])
        else:            #否则递归的构建二叉树，这时的二叉树的左右节点不是None
            flg=TreeNode(pre[0])
            flg.left=self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])])
            flg.right=self.reConstructBinaryTree(pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:])
        return flg