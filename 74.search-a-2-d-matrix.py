#
# @lc app=leetcode id=74 lang=python3
#
# [74]  Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        noR, noC = len(matrix), len(matrix[0])
        low, high = 0, (noR * noC) - 1
        while low <= high:
            middle = low + (high - low) // 2
            row, col = divmod(middle, noC)
            req = matrix[row][col]
            if req == target:
                return True
            elif req < target:
                low = middle + 1
            else: 
                high = middle - 1
        return False



# @lc code=end
