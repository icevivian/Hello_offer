#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 14:44
# @Author  : Aries
# @Site    : 
# @File    : 14.py
# @Software: PyCharm Community Edition
'''
输入一个链表，输出该链表中倒数第k个结点
解题思路：参考3.py中的问题，可以构建出该链表的反向输出即可。
注意：在这题中，输入变量是head(相当于ListNode.val,也就是链表的头一个参数)，而不是ListNode。
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        L=[]
        while head:
            L.insert(0,head)
            head=head.next
        return L[k-1] if len(L)>=k & k>0 else None