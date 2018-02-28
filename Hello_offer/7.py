#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 15:21
# @Author  : Aries
# @Site    : 
# @File    : 7.py
# @Software: PyCharm Community Edition
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39
解题思路：斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368
特别指出：第0项是0，第1项是第一个1。
代码实现：使用一个序列L记录整个序列，需要知道第n项则导出L序列的第n项
'''

#第一个想法，使用递归，但该方法运行时间太长
class Solution_1:
    def Fibonacci(self, n):
        # write code here
        if n<0:
            return None
        L=[0,1]
        if n==0 or n==1:
            return L[n]
        else:
            a=self.Fibonacci(n-1)+self.Fibonacci(n-2)
            return a

#最终解法：使用一个序列L记录整个序列，需要知道第n项则导出L序列的第n项
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<0:
            return None
        L=[0,1]
        if n==0 or n==1:
            return L[n]
        else:
            for i in range(1,n):
                L.append(L[-2]+L[-1])
            return L[n]

if __name__=="__main__":
    S=Solution()
    print(S.Fibonacci(3))