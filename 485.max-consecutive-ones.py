#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums: # Kiểm tra danh sách rỗng
            return 0 # Trả về 0 nếu danh sách rỗng
        max_count = 0 # Biến lưu trữ số 1 liên tiếp lớn nhất
        current_count = 0 # Biến lưu trữ số 1 liên tiếp hiện tại
        for num in nums: # Duyệt qua từng phần tử trong danh sách
            if num == 1: # Nếu phần tử là 1
                current_count += 1 # Tăng số 1 liên tiếp hiện tại
                max_count = max(max_count, current_count) # Cập nhật số 1 liên tiếp lớn nhất
            else: # Nếu phần tử không phải là 1
                current_count = 0 # Đặt lại số 1 liên tiếp hiện tại
        return max_count # Trả về số 1 liên tiếp lớn nhất
# @lc code=end

