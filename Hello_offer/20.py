#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 21:25
# @Author  : Aries
# @Site    : 
# @File    : 20.py
# @Software: PyCharm Community Edition
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
解题思路：这道题比较简单了，如果之前有了解栈的知识点的话。
唯一需要注意的是栈对象L的定义要先给出
'''

class Solution:
    def __init__(self):
        self.L=[]
    def push(self, node):
        # write code here
        self.L.append(node)
        return self.L
    def pop(self):
        # write code here
        return self.L.pop()
    def top(self):
        # write code here
        return self.L[0]
    def min(self):
        # write code here
        return min(self.L)

if __name__=='__main__':
    S=Solution()
    print(S.push(3))
    print(S.push(3))

