#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # DFS？
        self.res = []
        trace = []
        self.backtrace(trace,0,0,s) # 表示在start位置开始寻找第segID个分割符
        return self.res

    def backtrace(self, segments, segID, start, s):
        if segID==4 and start==len(s):
            self.res.append('.'.join(segments))
            return
        if segID==4 or start==len(s):
            return
        if s[start]=='0': # 如果第一个开头就是0，那必须单个分割
            segments.append(s[start])
            self.backtrace(segments, segID+1, start+1,s)
            segments.pop()
            return
        for i in range(start, len(s)): # 否则，只要这个数小于255，都可以尝试作为分割符end
            if int(s[start:i+1])<=255:
                segments.append(s[start:i+1])
                self.backtrace(segments, segID+1, i+1,s)
                segments.pop()
            else:
                break
            
# @lc code=end

