#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        sortedpoints = sorted(points, key=lambda x:x[1])
        endx = sortedpoints[0][1]
        res = 1
        for i in range(1, len(sortedpoints)):
            if sortedpoints[i][0]>endx:
                res+=1
                endx = sortedpoints[i][1]
        return res
# @lc code=end

