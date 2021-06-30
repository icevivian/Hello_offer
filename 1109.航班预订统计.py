#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0 for i in range(n)]
        dif = difference(nums)
        for booking in bookings:
            dif.increase(booking)
        return dif.result()
        

class difference(object):
    def __init__(self, nums):
        self.nums = nums
        self.diff = [nums[0] for i in range(len(nums))]
        for i in range(1, len(nums)):
            self.diff[i]=nums[i]-nums[i-1]
        
    def increase(self, bookinglist):
        first = bookinglist[0]-1
        last = bookinglist[1]-1
        value = bookinglist[2]
        self.diff[first]+=value
        if last<len(self.nums)-1:
            self.diff[last+1]-=value
        
    def result(self):
        result = [0 for i in range(len(self.nums))]
        result[0] = self.diff[0]
        for i in range(1, len(self.nums)):
            result[i]=result[i-1]+self.diff[i]
        return result
        
# @lc code=end

