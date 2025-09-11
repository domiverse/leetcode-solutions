#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:  # Kiểm tra nếu chuỗi rỗng
            return True  # Trả về True nếu chuỗi rỗng
        s = ''.join(c.lower() for c in s if c.isalnum())  # Lọc và chuyển đổi thành chữ thường
        left, right = 0, len(s) - 1 # Khởi tạo hai con trỏ
        while left < right: # Duyệt từ hai đầu chuỗi
            if s[left] != s[right]: # So sánh ký tự hai đầu
                return False # Trả về False nếu không khớp
            left += 1 # Di chuyển con trỏ bên trái sang phải
            right -= 1 # Di chuyển con trỏ bên phải sang trái
        return True # Trả về True nếu tất cả ký tự khớp
# @lc code=end

