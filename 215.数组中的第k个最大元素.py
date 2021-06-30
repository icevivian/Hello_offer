#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 最坏的时间复杂度是O（n^2）,因此为了增大随机，增加了一个random操作，平均时间复杂度为O（n）
        n = len(nums)
        k = n-k
        lo = 0
        hi = n-1
        while lo<=hi:
            q = self.random_partition(nums, lo, hi)
            if q==k:
                return nums[q]
            elif q>k:
                hi = q-1
            else:
                lo = q+1
        return -1

    def random_partition(self, nums, lo, hi):
        rand = random.randint(lo, hi)
        nums[lo], nums[rand] = nums[rand], nums[lo]
        return self.partition(nums, lo, hi)

    def partition(self, nums, lo, hi):
        value = nums[lo]
        slow = fast = lo
        while fast <= hi:
            if nums[fast] < value:
                slow += 1
                nums[slow],nums[fast]=nums[fast],nums[slow]
            fast+=1
        nums[slow],nums[lo] = nums[lo], nums[slow]
        return slow


# @lc code=end

