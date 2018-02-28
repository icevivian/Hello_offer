#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 16:08
# @Author  : Aries
# @Site    : 
# @File    : 8.py
# @Software: PyCharm Community Edition
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
注意：假设n=3,方法（2,1）和（1,2）算两种不同的跳法
解题思路：当青蛙跳n级台阶的时候，如果最后一步跳了1阶，则前面共有f(n-1)种跳法，如果最后一步跳了2阶，则前面共有f(n-2)中跳法，因此f(n)=f(n-1)+f(n-2),这是一个斐波那契数列。
代码实现：参考7.py
'''

class Solution:
    def jumpFloor(self, number):
        # write code here
        if number<1:
            return None
        L=[1,1]
        if number==1 :
            return L[number]
        else:
            for i in range(1,number):
                L.append(L[-2]+L[-1])
            return L[number]

if __name__=="__main__":
    S=Solution()
    print(S.jumpFloor(3))
