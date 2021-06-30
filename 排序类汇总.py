#!/usr/bin/env python
# -*- coding=utf-8 -*-
# 归并排序
def merge_sort(nums, lo, hi):
    if lo < hi:
        mid = lo + (hi-lo)//2
        sort(nums, lo, mid)
        sort(nums, mid+1, hi)
        merge(nums, lo, mid, hi)
    return nums

def merge(nums, lo, mid, hi):
    L = nums[lo:mid+1].copy()
    R = nums[mid+1:hi+1].copy()
    L.append(float('INF'))
    R.append(float('INF'))
    l, r = 0, 0
    for i in range(lo, hi+1):
        if L[l]<=R[r]:
            nums[i] = L[l]
            l += 1
        else:
            nums[i] = R[r]
            r += 1 


# 快速排序
import random
def quick_sort(nums, lo, hi):
    if lo < hi:
        mid = random_partition(nums, lo, hi)
        quick_sort(nums, lo, mid-1)
        quick_sort(nums, mid+1, hi)
    return nums

def random_partition(nums, lo, hi):
    i = random.randint(lo, hi)
    nums[i],nums[lo] = nums[lo], nums[i]
    return partition(nums, lo, hi)

def partition(nums, lo, hi):
    # 使用fast指针去探路，保证[lo+1,...,slow]的数都是小于value的数
    value = nums[lo]
    slow = lo
    fast = lo+1
    while fast <= hi:
        if nums[fast] < value:
            slow += 1
            nums[slow],nums[fast] = nums[fast],nums[slow]
        fast +=1 
    nums[slow],nums[lo] = nums[lo],nums[slow]
    return slow


# 堆排序
def heap_sort(arr):
    if len(arr)<=1:
        return arr
    n = len(arr)
    for i in range(1,n):
        heapInsert(arr, i)
    arr[0], arr[n-1] = arr[n-1], arr[0]
    for size in range(n-1,0,-1):
        heapify(arr, size)
        arr[0], arr[size-1] = arr[size-1], arr[0]
    return arr
    
def heapInsert(arr, i):
    while i>0 and arr[i]>arr[(i-1)//2]:
        arr[i],arr[(i-1)//2] = arr[(i-1)//2], arr[i]
        i = (i-1)//2
    
def heapify(arr, size):
    index = 0
    left = 2*index+1
    while left<size:
        if left+1<size and arr[left+1]>arr[left]:
            largest = left+1
        else:
            largest = left
        if arr[largest]>arr[index]:
            arr[largest], arr[index] = arr[index], arr[largest]
            index = largest
            left = 2*index+1
        else:
            break

A=[13,19,9,5,12,8,7,4,21,2,6,11]
print(heap_sort(A))
