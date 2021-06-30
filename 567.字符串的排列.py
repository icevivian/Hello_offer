#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = right = 0
        minlen = float('INF')
        need = dict()
        for i in s1:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        window = dict()
        valid = 0

        while right < len(s2):
            word = s2[right]
            right += 1
            if word in need:
                if word in window:
                    window[word]+=1
                else:
                    window[word]=1
                if window[word] == need[word]:
                    valid+=1
            
            while right-left>=len(s1):
                if valid == len(need):
                    return True
                word = s2[left]
                left += 1
                if word in need:
                    if window[word] == need[word]:
                        valid -= 1
                    window[word]-=1
        return False
# @lc code=end

