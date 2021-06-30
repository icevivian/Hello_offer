# 归并排序
def sort(nums, lo, hi):
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

print(sort([1,3,5,7,11,10,6],0,6))

# 快速排序
def quick_sort(nums, lo, hi):
    if lo < hi:
        mid = partition(nums, lo, hi)
        quick_sort(nums, lo, mid-1)
        quick_sort(nums, mid+1, hi)
    return nums

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

A=[13,19,9,5,12,8,7,4,21,2,6,11]
print(quick_sort(A,0,len(A)-1))

# 堆排序