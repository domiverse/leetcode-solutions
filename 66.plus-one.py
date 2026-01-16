#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            n = len(digits) # Lấy độ dài của danh sách
            for i in range(n - 1, -1, -1): # Duyệt từ phải sang trái
                if digits[i] < 9: # Nếu phần tử nhỏ hơn 9
                    digits[i] += 1 # Tăng giá trị phần tử lên 1
                    return digits # Trả về danh sách đã cập nhật
                digits[i] = 0 # Đặt giá trị phần tử thành 0
            return [1] + digits # Thêm 1 vào đầu danh sáchd
# @lc code=end