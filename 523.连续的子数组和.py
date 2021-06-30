#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:
            return False
        sumdict = dict()
        sumdict[0] = -1 # 可以从i=0的位置开始取
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s%k not in sumdict:
                sumdict[s%k]=i
            elif i-sumdict[s%k]>=2:
                return True
        return False
           
# @lc code=end

