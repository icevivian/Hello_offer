#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        sortednum = sorted(nums)
        pos = 0
        while pos < len(nums)-2:
            value = sortednum[pos]
            subres = self.twoSum(sortednum, pos+1, -value)
            for i in subres:
                res.append(list([value]+i))
            while pos<len(nums) and sortednum[pos]==value :
                pos+=1  
        return res       
            

    def twoSum(self, nums, start, target):
        left = start
        right = len(nums)-1
        subres = []
        while left < right:
            leftvalue = nums[left]
            rightvalue = nums[right]
            if nums[left]+nums[right]==target:
                subres.append(list([leftvalue, rightvalue]))
                while left< right and nums[left] == leftvalue:
                    left+=1
                while left< right and nums[right] == rightvalue:
                    right-=1
            elif nums[left]+nums[right]>target:
                while left< right and nums[right] == rightvalue:
                    right -= 1
            else:
                while left< right and nums[left] == leftvalue:
                    left += 1
        return subres
# @lc code=end

