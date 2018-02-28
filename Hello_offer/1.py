#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 19:38
# @Author  : Aries
# @Site    : 
# @File    : 1.py
# @Software: PyCharm Community Edition
import numpy
'''
题目1
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
解题思路：以数组中的左下角（或者右上角）的数字作为index与目标值比较，从而一步步缩小比较范围。
代码实现：这里使用一个指针位置来指示左下角的数，根据比较结果挪动该指针。另外应该考虑该数值为空的特殊情况。
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        rows =len(array)
        lines = len(array[0])
        row, line = rows - 1, 0
        while row>=0 and line<=lines-1:
            if array[row][line]==target:
                return True
            if array[row][line]>target:
                row-=1
            else:
                line+=1
        return False

if __name__=='__main__':
    T=[[1,2,3],
       [4,5,6],
       [7,8,9]]
    a=Solution()
    print(a.Find(12, T))
