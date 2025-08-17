#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: # Kiểm tra mảng rỗng
            return 0 # Trả về 0 nếu mảng rỗng
        slow = 0 # Chỉ số cho phần tử khác giá trị val
        for fast in range(len(nums)): # Chỉ số cho phần tử hiện tại
            if nums[fast] != val: # Nếu phần tử hiện tại khác giá trị val
                nums[slow] = nums[fast] # Di chuyển phần tử khác giá trị val về phía trước
                slow += 1 # Tăng chỉ số cho phần tử khác giá trị val
        return slow # Trả về độ dài của mảng sau khi loại bỏ phần tử
# @lc code=end

