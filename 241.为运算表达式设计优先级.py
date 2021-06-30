#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 分治的思想
        n = len(expression)
        res = []
        for i in range(n):
            if expression[i] == '+' or expression[i]=='-' or expression[i] == '*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:n])
                for l in left:
                    for r in right:
                        if expression[i] == '+':
                            res.append(l+r)
                        elif expression[i] == '-':
                            res.append(l-r)
                        else:
                            res.append(l*r)
        if res == []:
            return [int(expression)]
        return res
                        
# @lc code=end

