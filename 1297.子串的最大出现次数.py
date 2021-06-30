#
# @lc app=leetcode.cn id=1297 lang=python3
#
# [1297] 子串的最大出现次数
#

# @lc code=start
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # 如果有字符串满足其出现次数最多，那么其中一定有一个字符串是minSize大小的，所以直接枚举所有长度为minSize大小的子串即可
        left, right = 0,0
        window = dict()
        subs = dict()
        while right<len(s):
            value = s[right]
            right += 1
            if value in window:
                window[value]+=1
            else:
                window[value]=1
            
            if len(window)<=maxLetters and right-left == minSize :
                w = s[left:right]
                if w in subs:
                    subs[w] += 1
                else:
                    subs[w] = 1
            while right-left > minSize:
                value = s[left]
                left += 1
                if window[value] == 1:
                    del window[value]
                else:
                    window[value] -= 1
                if len(window)<=maxLetters and right-left==minSize :
                    w = s[left:right]
                    if w in subs:
                        subs[w] += 1
                    else:
                        subs[w] = 1
        if not subs:
            return 0
        return max(subs.values())
        
# @lc code=end

