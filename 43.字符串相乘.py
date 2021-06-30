#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        res = [0 for i in range(m+n)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                p1 = i+j
                p2 = i+j+1
                mul = int(num1[i])*int(num2[j])
                sum1 = mul+res[p2]
                res[p2]=sum1%10
                res[p1]=res[p1]+sum1//10
        index = 0
        while index<m+n and res[index]==0:
            index += 1
        for i in range(index,m+n):
            res[i]=str(res[i])
        return ''.join(res[index:]) if res[index:] else '0'

# @lc code=end

