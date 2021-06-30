#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==1:
            return 0
        sortintervals = sorted(intervals, key=lambda x:x[1])
        res=0
        xend = sortintervals[0][1]
        for i in range(1, len(intervals)):
            if sortintervals[i][0]<xend:
                res+=1
            else:
                xend = sortintervals[i][1]
        return res
        # 贪心算法，先把list按照结束时间排序，选择第一个的结束时间与其他的开始时间进行对比，重叠的则进行删除
# @lc code=end

