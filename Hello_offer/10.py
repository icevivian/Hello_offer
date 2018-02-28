#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 16:37
# @Author  : Aries
# @Site    : 
# @File    : 10.py
# @Software: PyCharm Community Edition
'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
结题思路：考虑每个大矩形最上面的排布只有两种情况：1.最上面使用一个长条的2*1矩阵覆盖，则另外的覆盖方式有f(n-1),2.最上面采用两个竖排的2*1矩阵覆盖，则另外的覆盖方式有f(n-2)，则f(n)=f(n-1)+f(n-2)
求解也是一个斐波那契数列。
'''

class Solution:
    def rectCover(self, number):
        # write code here
        if number<0:
            return None
        L=[1,1]
        if number==0:
            return 0
        if number==1 :
            return L[number]
        else:
            for i in range(1,number):
                L.append(L[-2]+L[-1])
            return L[number]
if __name__=="__main__":
    S=Solution()
    print(S.rectCover(3))