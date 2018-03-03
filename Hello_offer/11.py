#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 14:49
# @Author  : Aries
# @Site    : 
# @File    : 11.py
# @Software: PyCharm Community Edition
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示.
解题思路：首先将整数转换为二进制，整数大于0时直接转换，整数小于0时用其绝对值的二进制的补码表示。
特别注意：这里使用补码实现时，二进制编码是4个字节的，所以将负数n表示成补码时用bin(n+2**32)
代码实现：bin（n）
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n).count('1') if n>=0 else bin(n+2**32).count('1')
if __name__=='__main__':
    S=Solution()
    print(S.NumberOf1(4))