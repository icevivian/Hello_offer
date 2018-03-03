#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 15:17
# @Author  : Aries
# @Site    : 
# @File    : 12.py
# @Software: PyCharm Community Edition
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
解题思路： 并不需要思路==
'''
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base**exponent
if __name__=='__main__':
    base=2.3
    exponent=int(3)
    print(Solution().Power(base,exponent))