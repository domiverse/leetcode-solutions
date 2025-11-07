#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        low, high  = 0, len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return -1
# @lc code=end

