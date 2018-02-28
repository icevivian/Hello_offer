#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 20:22
# @Author  : Aries
# @Site    : 
# @File    : 3.py
# @Software: PyCharm Community Edition
'''
输入一个链表，从尾到头打印链表每个节点的值。
解题思路：对该链表使用栈来实现后进先出
代码实现：listNode指单链表中的指针，初始指向链表的头，我们依次将链表中头的数据放置在列表li的最前面，从而实现该链表的逆。
PS：这一题后台创建了一个单链表对象，本人对创建过程不太懂，因此这段代码不能在python中单独运行==，但答案在剑指offer中是通过的。
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        li=[]
        while listNode:
            li.insert(0,listNode.val)
            listNode=listNode.next
        return li
