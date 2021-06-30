#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#

# @lc code=start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # 求最短路径，用BFS
        if len(arr)<=1:
            return 0
        indexdict = {}
        for i in range(len(arr)):
            if arr[i] not in indexdict:
                indexdict[arr[i]] = [i]
            elif arr[i]!=arr[i-1] or (i+1<len(arr) and arr[i]!=arr[i+1]): # 剪枝，连续相同值只保留最左或最右的值
                indexdict[arr[i]].append(i)       
        q = list()
        visited = set()
        q.append(0)
        visited.add(0)
        step = 0
        while q:
            sz = len(q)
            for i in range(sz):  # 对队列中这一层所有数进行遍历
                cur = q.pop(0)
                if cur == len(arr)-1:
                    return step
                same = indexdict[arr[cur]]
                same.extend([cur-1, cur+1])
                for i in same:
                    if i >=0 and i<=len(arr)-1 and i not in visited:
                        q.append(i)
                        visited.add(i)
            step += 1
        return step     
# @lc code=end

