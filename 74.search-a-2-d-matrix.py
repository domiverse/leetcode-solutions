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
        soHang, soCot = len(matrix), len(matrix[0])
        low, high = 0, soHang * soCot - 1
        while low <= high:
            middle = low + (high - low) // 2
            r, c = divmod(middle, soCot)
            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                low = middle + 1
            else:
                high = middle - 1
        return False



# @lc code=end

