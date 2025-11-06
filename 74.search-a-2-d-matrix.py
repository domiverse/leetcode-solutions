#
# @lc app=leetcode id=74 lang=python3
#
# [74]  
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = len(matrix), len(matrix[0])
        left, right = 0, low*high - 1

        while left <= right:
            middle = left + (right - left) // 2
            hang, cot = divmod(middle, high)
            value = matrix[hang][cot]
            if value == target:
                return True
            elif value < target:
                left = middle + 1
            else: 
                right = middle - 1
        return False

# @lc code=end

