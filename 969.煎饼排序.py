#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

# @lc code=start
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 1:
            return []
        self.res = []
        self.sort(arr, n)
        return self.res
    
    def sort(self, arr, n):
        if n == 0:
            return
        # 先找到最大的数
        maxindex = 0
        maxvalue = 0
        for i in range(n):
            if arr[i]>maxvalue:
                maxvalue = arr[i]
                maxindex = i
        self.reverse(arr, 0, maxindex)
        self.res.append(maxindex+1)
        self.reverse(arr, 0, n-1)
        self.res.append(n)

        self.sort(arr, n-1)
    
    def reverse(self, arr, l, r):
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

# @lc code=end

