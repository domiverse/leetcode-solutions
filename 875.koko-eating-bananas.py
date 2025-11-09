#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return False
        low, high = 1, max(piles)
        while low < high:
            middle = low + (high - low) // 2
            k = sum(ceil(p/middle) for p in piles)
            if k <= h:
                high = middle 
            else:
                low = middle + 1
        return low
# @lc code=end

