#
# @lc app=leetcode.cn id=593 lang=python3
#
# [593] 有效的正方形
#

# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 先把四个节点按照升序排列
        ps1, ps2, ps3, ps4 = sorted([p1, p2, p3, p4], key=lambda x:(x[0],x[1]))
        
        # 判断是否为正方形的方式就是：四个边长相等且两条对角线相等
        return self.distance(ps1, ps2)!=0 and self.distance(ps1, ps2)==self.distance(ps2, ps4) and self.distance(ps2, ps4)==self.distance(ps4, ps3) and self.distance(ps4, ps3)==self.distance(ps1, ps3) and self.distance(ps1, ps4)==self.distance(ps2, ps3)

    def distance(self, n1, n2):
        return (n1[0]-n2[0])**2+(n1[1]-n2[1])**2
# @lc code=end

