#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = right = 0
        self.res = list()
        need = dict()
        for i in p:
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
            
            while right-left>=len(p):
                if valid == len(need):
                    self.res.append(left)
                word = s[left]
                left += 1
                if word in need:
                    if window[word] == need[word]:
                        valid -= 1
                    window[word]-=1
        return self.res
# @lc code=end

