#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 我们维护一个候选众数 candidate 和它出现的次数 count
        # 我们遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，如果 count 的值为 0，我们先将 x 的值赋予 candidate，随后我们判断 x：
        # 如果 x 与 candidate 相等，那么计数器 count 的值增加 1；
        # 如果 x 与 candidate 不等，那么计数器 count 的值减少 1。
        count = 1
        candidate = nums[0]
        for i in range(1, len(nums)): 
            if count == 0:
                candidate = nums[i]   
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate            
# @lc code=end

