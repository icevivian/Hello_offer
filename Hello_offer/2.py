#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 20:16
# @Author  : Aries
# @Site    : 
# @File    : 2.py
# @Software: PyCharm Community Edition
'''
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy
解题思路:使用python中自带的replace功能即可。
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s_r=s.replace(' ', '%20')
        return s_r
if __name__=='__main__':
    s='We are happy'
    a=Solution()
    print(a.replaceSpace(s))