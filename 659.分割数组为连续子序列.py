#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = dict()
        need = dict()
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in nums:
            if freq[i] == 0:
                continue
            if i in need and need[i]>0: # 是否可以接到序列后面
                freq[i]-=1
                need[i] = need[i]-1
                need[i+1] = need.get(i+1,0)+1
            elif freq[i]>0 and i+1 in freq and freq[i+1]>0 and i+2 in freq and freq[i+2]>0: #是否可以重起一个头
                freq[i]-=1
                freq[i+1]-=1
                freq[i+2]-=1
                need[i+3]=need.get(i+3,0)+1
            else:
                return False
        return True


# @lc code=end

