#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # DFS
        self.res = []
        track = []
        self.backtrack(track, 0, nums)
        return self.res
    def backtrack(self, track, start, nums):
        self.res.append(list(track))
        for j in range(start, len(nums)):
            track.append(nums[j])
            self.backtrack(track, j+1, nums)
            track.pop()
        



# @lc code=end

