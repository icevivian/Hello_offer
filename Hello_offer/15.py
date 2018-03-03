#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 15:02
# @Author  : Aries
# @Site    : 
# @File    : 15.py
# @Software: PyCharm Community Edition
'''
输入一个链表，反转链表后，输出链表的所有元素.'
注意：与3.py不同的是，这道题输出的还是一个链表，因此我们要改变链表中节点的指向，也就是pHead.next
解题思路：采用循环，每次改变相邻两个节点之间的指向，并为下一次循环设置定位点。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        # pHead 指的是首节点
        if pHead==None or pHead.next==None:
            return pHead    #如果PHead为空或者只有一个节点，则返回该节点本身
        last=None
        while pHead:        #在这个循环中，通过例子说明，假设链表为1->2->3,pHead=1
            Next=pHead.next #Next=2,     第二次循环：Next=2.next=3,
            pHead.next=last #1.next=None,   第二次循环：2.next=1
            last=pHead      #last=1,       第二次循环：last=2
            pHead=Next      #pHead=2  第一次循环之后链表就成了1->None,  第二次循环：pHead=3,第二次循环之后链表为2->1，直到最后一次循环完成，last为最后一个节点，即新链表的第一个节点
        return last
