#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        minlen = float('INF')
        need = dict()
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        window = dict()
        valid = 0

        while right < len(s):
            word = s[right]
            right += 1
            if word in need:
                if word in window:
                    window[word]+=1
                else:
                    window[word]=1
                if window[word] == need[word]:
                    valid+=1
            
            while valid == len(need):
                if right-left<minlen:
                    minlen = right-left
                    start = left
                word = s[left]
                left += 1
                if word in need:
                    if window[word] == need[word]:
                        valid -= 1
                    window[word]-=1
        return "" if minlen == float('INF') else s[start:start+minlen]                          
# @lc code=end

