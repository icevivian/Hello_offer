#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valuedict = dict()
        for i in range(len(nums)):
            value = target - nums[i] 
            if value in valuedict:
                return [valuedict[value],i]
            valuedict[nums[i]] = i
        # 这种方法用了字典来存储之前的数据

# @lc code=end

