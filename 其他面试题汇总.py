#!/usr/bin/env python
# -*- coding=utf-8 -*-
# 搜狗
# 蛇形打印矩阵
def help(s,i,j):
    res = []
    while i<=len(s)-1 and i>=0 and j >=0 and j<=len(s)-1:
        res.append(s[i][j])
        i += 1
        j -= 1
    return res

def printmatrix(s):
    n = len(s)
    flag = 0
    res = []
    for i in range(n):
        subres = help(s,0,i)
        if flag == 1:
            res.extend(subres)
            flag = 1-flag
        else:
            res.extend(reversed(subres))
            flag = 1-flag
    for i in range(1,n):
        subres = help(s,i,n-1)
        if flag == 1:
            res.extend(subres)
            flag = 1-flag
        else:
            res.extend(reversed(subres))
            flag = 1-flag
    return res
    
# s=[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]]
# print(printmatrix(s))

# 贝壳
# 数组A由N个随机正整数(int)组成，设计算法，给定整数n，在A中找出符合如下等式：n=Ai+Aj 的所有 i 和 j 的下标组合。
def getindex(arr, n):
    N = len(arr)
    pos = dict()
    res = []
    for i in range(N):
        value = n-arr[i]
        if value in pos:
            for index in pos[value]:
                res.append([index,i])
        if arr[i] not in arr:
            pos[arr[i]] = [i]
        else:
            pos[arr[i]].append(i)
    return res

####################### 微软 ######################################

# 给出一个数组，随机返回其中N个元素。要求数组中每个元素返回的概率相等
import random
def getrandom(arr, N):
    res = []
    for i in arr:
        res.append((i,random.random()))
    nums = sorted(res, key=lambda x:x[1])
    return [x[0] for x in nums[:N]]
# arr = [1,4,2,5,3,5]
# N = 3
# print(getrandom(arr, N))

# 将数组分成两部分，使得这两部分的和的差最小。返回分割后的两个数组
# 思路：转化为背包问题就是，背包容量sum/2的情况下，能装下的最大价值。其实这里容量和价值是一样的
def split_list(arr):
    s = sum(arr)//2
    n = len(arr)
    dp = [[0 for i in range(s+1)] for j in range(n+1)] # dp[i][j]表示前i个物品，当前容量为j时，能装下的最大价值
    dp_index = [[0 for i in range(s+1)] for j in range(n+1)] # 表示构成dp[i][j]时，第i个物品是否加入，1表示加入，0表示没有
    res1 = []
    res2 = []
    for i in range(1, n+1):
        for j in range(1, s+1):
            if j>=arr[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1]]+arr[i-1])
            else:
                dp[i][j] = dp[i-1][j]
            if dp[i][j]>dp[i-1][j]:
                dp_index[i][j] = 1
    while n>0 and s>0:
        if dp_index[n][s]==1:
            res1.append(arr[n-1])
            s = s-arr[n-1]
        n = n-1
    res2 = [x for x in arr if x not in res1]
    return res1, res2


# arr = [1,15,6,20]
# print(split_list(arr))

    
# 美团
# 子数组的最大累加和的最长子数组 
def getmax(arr):
    n = len(arr)
    if n<=1:
        return arr
    dp = [0 for i in range(n)]
    dp_index = [0 for i in range(n)]
    dp[0] = arr[0]
    dp_index[0] = 0
    res = -float('INF')
    for i in range(1,n):
        if dp[i-1]<0:
            dp[i] = arr[i]
            dp_index[i] = i
        else:
            dp[i] = dp[i-1]+arr[i]
            dp_index[i] = dp_index[i-1]
        if dp[i]>=res:
            start = dp_index[i]
            end = i
            res = max(res, dp[i])
    return arr[start:end+1]

# arr = [1,3,-5,4,2,-1,2]
# arr = [-4,1,3,-1,-3,1,3]
# print(getmax(arr))

###################### 百度 ##################################
# 计算auc
# 思路：auc实际表示的就是正例在负例前面的pair对占全部pair对的比例
arr = [[1,0.9],[1,0.8],[1,0.7],[1,0.7],[1,0.4],[0,0.6],[0,0.5],[0,0.3]]
def getauc(arr):
    n = len(arr)
    pos = []
    neg = []
    for i in range(n):
        if arr[i][0] == 1:
            pos.append(arr[i][1])
        else:
            neg.append(arr[i][1])
    res = 0
    for i in range(len(pos)):
        for j in range(len(neg)):
            if pos[i]>neg[j]:
                res += 1
    res = res/(len(pos)*len(neg))
    return res
# print(getauc(arr))

# 输入为多个有序数组，输出为合并的一个有序数组
class node(object):
    def __init__(self, value, k, j):
        self.value = value
        self.out_index = k
        self.in_index = j
        
class solution():
    def MergeArr(self, arr, n, m):
        nums = []
        for i in range(n):
            nums.append(node(arr[i][0], i, 0))
        for i in range(n):
            self.heapInsert(nums, i)
        res = []
        for i in range(n*m):
            value = nums[0].value
            res.append(value)
            k = nums[0].out_index
            j = nums[0].in_index
            if j+1<m:
                nums[0] = node(arr[k][j+1], k, j+1)
            else:
                nums[0] = node(float('INF'), k, j+1)
            self.heapify(nums)
        return res

    def heapInsert(self, nums, i):
        '''
        构建堆，自下而上
        '''
        while i>0 and nums[i].value<nums[(i-1)//2].value:
            nums[i],nums[(i-1)//2] = nums[(i-1)//2], nums[i]
            i = (i-1)//2
             
    def heapify(self, nums):
        '''
        重建堆，自上而下
        '''
        n = len(nums)
        index = 0
        left = 2*index+1
        while left<n:
            if left+1<n and nums[left+1].value<nums[left].value:
                smallest = left+1
            else:
                smallest = left
            if nums[smallest].value<nums[index].value:
                nums[smallest], nums[index] = nums[index], nums[smallest]
                index = smallest
                left = 2*index+1
            else:
                break

############################ 头条 #######################################
# A表示工区位置，B表示路由器位置，求每个路由器最小的档数（覆盖范围）x
# 思路：对工区来说，计算它被路由器覆盖时最小的覆盖档位，然后对所有工区的最小取最大，复杂度为O（mn），应该有简化版的方法
def getmin(A,B):
    n = len(A)
    m = len(B)
    res = []
    for i in range(n):
        value = float('INF')
        for j in range(m):
            value = min(value, abs(B[j]-A[i]))
        res.append(value)
    return max(res)

# A = [1,2,3,4,5,7,9]
# B = [1,4]
# # A = [1,5,9]
# # B = [1,5,9]
# print(getmin(A, B))

# 每个字符串中的?可替换成0，1，2中的任意一种，求已知字符输入s，其？替换之后，相邻字符均不同的字符组合共有几种？
def getnum(s):
    n = len(s)
    dp = [[0 for i in range(3)] for j in range(n)]  
    for i in range(n):
        for j in range(3):
            if s[i]!='?':
                if s[i] == str(j):
                    if i==0:
                        dp[i][j] = 1
                        continue
                    for k in range(3):
                        if k!=j:
                            dp[i][j] += dp[i-1][k]
                else:
                    dp[i][j]=0
            else:
                for k in range(3):
                    if k!=j:
                        dp[i][j] += dp[i-1][k]
    return sum(dp[n-1])

              
# dp[i][j] = sum(dp[i-1][!j]) 
# if s[i]!='?',j==s[i]时上式成立，j!=s[i]时，上式为0
# else j可为0，1，2       
s = '0?0??'
print(getnum(s))

