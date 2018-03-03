#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 16:55
# @Author  : Aries
# @Site    : 
# @File    : 17.py
# @Software: PyCharm Community Edition
'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
解题思路：这道题肯定需要使用递归的方法，先找到两棵树中相同数值的第一个节点，再顺着该节点比较下去，若结构相同则返回True,若不同，则放弃开始的这一个相同数值的节点，往下接着寻找同数值的树节点进行比较。
因此这里给出两个函数：一个用于寻找第一个相同数值的树节点，第二个判断相同数值的树节点下的左右数是否相同。
在使用递归的时候，我们必须明确的是停止该递归的条件是什么，这里是：当比较两棵树的节点时：1.出现tree2节点为None的情况，返回True;2.出现tree1节点为None的情况，返回False;3.两棵树节点出现数值不同的情况，返回False;
'''

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):    #这个函数用于寻找第一个相同数值的树节点
        # write code here
        result=False
        if pRoot1 and pRoot2:
            if pRoot1.val==pRoot2.val:
                result=self.IsSubtree(pRoot1,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
            return result
    def IsSubtree(self,pRoot1,pRoot2):   #这个函数判断相同数值的树节点下的左右数是否相同
        if not pRoot2:
            return True
        if not pRoot1 or pRoot1.val!=pRoot2.val:
            return False
        else:
            return self.IsSubtree(pRoot1.left,pRoot2.left) and self.IsSubtree(pRoot1.right,pRoot2.right)