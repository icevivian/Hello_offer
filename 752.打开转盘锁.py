#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getup(curstring, i):
            curlist = list(curstring)
            if curlist[i] == '9':
                curlist[i] = '0'
            else:
                curlist[i] = str(int(curlist[i])+1)
            return ''.join(curlist)

        def getdown(curstring, i):
            curlist = list(curstring)
            if curlist[i] == '0':
                curlist[i] = '9'
            else:
                curlist[i] = str(int(curlist[i])-1)
            return ''.join(curlist)

        q = ['0000']
        visited = set()
        visited.add('0000')
        nums = 0
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if cur == target:
                    return nums
                if cur in deadends:
                    continue
                for i in range(4):
                    up = getup(cur, i)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = getdown(cur, i)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            nums += 1
        return -1
                
# @lc code=end

