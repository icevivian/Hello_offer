#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # bucket表示桶内的数字，记录路径
        bucket = [0 for i in range(k)]
        if sum(nums)%k != 0:
            return False
        self.target = sum(nums)/k
        self.nums = sorted(nums, reverse=True)  # 对nums进行排序，先对最大的数做选择
        return self.backtrack(bucket, 0)
    
    def backtrack(self, bucket, index):
        if index == len(self.nums): # 结束条件：已经遍历完全部数组
            for value in bucket:
                if value != self.target:
                    return False
            return True
        for k in range(len(bucket)):  # 选择进入哪一个桶
            if bucket[k]+self.nums[index] > self.target:
                continue
            bucket[k] = bucket[k]+self.nums[index]
            if self.backtrack(bucket, index+1):
                return True
            bucket[k] = bucket[k]-self.nums[index]
        return False
# @lc code=end

