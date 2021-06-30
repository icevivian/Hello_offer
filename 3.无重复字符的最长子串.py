#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        window = dict()
        res = 0
        while right < len(s):
            word = s[right]
            right += 1
            # 窗口内更新
            window[word] = window.get(word,0)+1           
            while window[word]>1:
                word2 = s[left]
                left += 1
                # 窗口内更新
                window[word2] = window[word2]-1           
            res = max(res, right-left)
            
        return res
# @lc code=end

