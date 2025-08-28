#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: # Kiểm tra mảng rỗng
            return # Nếu mảng rỗng thì dừng
        last_non_zero = 0 # Chỉ số của phần tử khác 0 cuối cùng
        for i in range(len(nums)): # Duyệt qua từng phần tử trong mảng
            if nums[i] != 0: # Nếu phần tử khác 0
                nums[last_non_zero] = nums[i] # Di chuyển phần tử khác 0 về phía trước
                last_non_zero += 1 # Cập nhật chỉ số của phần tử khác 0 cuối cùng
        for i in range(last_non_zero, len(nums)): # Đặt tất cả các phần tử còn lại thành 0
            nums[i] = 0 # Đặt phần tử thành 0

# @lc code=end

