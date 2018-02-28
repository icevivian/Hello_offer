#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 21:20
# @Author  : Aries
# @Site    : 
# @File    : 5.py
# @Software: PyCharm Community Edition
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
解题思路：实现队列的push和pop，也就是说要使的pop出的是队头的元素而不是队尾.
代码实现：用两个栈的pop来实现队列的先进先出。具体方法是一个栈负责进数据，一个栈负责出数据。
          在进了数据之后需要出数据的时候就将栈1中的数据逆向转入栈2中，然后出栈2中的数据，当栈2的数据都出完了再继续导入栈1中进来的数据。
'''


class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)   #当push进数据时，数据都存入栈1
    def pop(self):
        #当pop数据时，如果栈2为空，则将栈1中的数据逆向过来存储，然后导出，若栈2中仍留有数据则直接从栈2出。
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else "None"




if __name__=="__main__":
    a=Solution()
    a.push(1)
    a.push(2)
    print(a.pop())
    a.push(3)
    print(a.pop())
    print(a.pop())
    print(a.pop())
