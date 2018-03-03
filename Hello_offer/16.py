#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 16:50
# @Author  : Aries
# @Site    : 
# @File    : 16.py
# @Software: PyCharm Community Edition
'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
解题思路：对一个数据结构做任意操作的最简单方法是重新构造另外一个数据结构，这里我们构造一个新的链表来存放合并后的链表节点。
         比较两个链表的值，将更小的一个值放入新的链表，当一个链表比较结束之后，直接链接到创建的最终链表
代码实现：这里善于使用了and, or这两个关键词，达到了if...then..的选择效果。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head=ListNode(0)
        res=head
        while pHead1 and pHead2:
            if pHead1.val>=pHead2.val:
                head.next=pHead2
                pHead2=pHead2.next
            else:
                head.next=pHead1
                pHead1=pHead1.next
            head=head.next
        head.next= pHead1 or pHead2
        return res.next
