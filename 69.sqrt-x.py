#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x//2
        while left <= right:
            middle = left + (right - left) //2
            square = middle * middle
            if square == x:
                return middle
            elif square < x:
                left = middle + 1
            else:
                right = middle - 1
        return right
# @lc code=end

