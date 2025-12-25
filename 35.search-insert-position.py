#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] == target: 
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return low #kh
# @lc code=end

