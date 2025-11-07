#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] == target:
                left = right = middle
                while left > 0 and nums[left - 1] == target:
                    left = left - 1
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right = right + 1
                return [left, right]
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return [-1, -1]
# @lc code=end