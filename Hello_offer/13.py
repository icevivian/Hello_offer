#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 15:24
# @Author  : Aries
# @Site    : 
# @File    : 13.py
# @Software: PyCharm Community Edition
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
解题思路：将原始数值中的奇数挑选出来存入一个新数组，并在原始数组中移除该奇数，最后将奇偶两部分合并。
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd=[]
        even=array[:]
        for i in array:
            if i%2==1:
                even.remove(i)
                odd.append(i)
        return odd+even

if __name__=='__main__':
    print(Solution().reOrderArray([1,2,4,6,7,5,9]))
