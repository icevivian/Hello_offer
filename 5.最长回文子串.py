#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i+1)
            res = res if len(res)>len(s1) else s1
            res = res if len(res)>len(s2) else s2
        return res

    def palindrome(self, s, l, r):
        while l<=r and l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
# @lc code=end

