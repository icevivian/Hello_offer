#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 16:22
# @Author  : Aries
# @Site    : 
# @File    : 9.py
# @Software: PyCharm Community Edition
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
解题思路：按照上例分析，这一个实例的f(n)=f(0)+f(1)+...+f(n-1),后边的各项可以解释为青蛙一次跳n个台阶、青蛙最后一次跳n-1个台阶...青蛙最后一次跳1个台阶。其中f(0)=1.
代码实现：按照上面的公式计算出前面几个数字之后发现数列为1,2,4,8，...因此得出结果为2的n-1次幂
'''

class Solution:
    def jumpFloorII(self, number):
        if number<1:
            return None
        else:
            return 2**(number-1)

if __name__=='__main__':
    S=Solution()
    print(S.jumpFloorII(3))