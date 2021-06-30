#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 目标在于n!中能够分解出多少2和5对，因为偶数中都能分解出2，因此主要就是求能够分解出多少个5
        divisor = 5
        res = 0
        while divisor <= n:
            res += n//divisor
            divisor = divisor * 5
        return res
# @lc code=end

