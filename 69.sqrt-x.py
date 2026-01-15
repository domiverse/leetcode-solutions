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
        low, high = 2, x//2
        while low <= high:
            middle = low + (high - low) // 2
            square = middle * middle
            if square == x:
                return middle
            elif square < x:
                low = middle + 1
            else:
                high = middle - 1
        return high #asddS
# @lc code=end

