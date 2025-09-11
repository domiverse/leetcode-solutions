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
        s = s.lower()  # Chuyển đổi chuỗi thành chữ thường
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():  # Bỏ qua ký tự không phải chữ cái hoặc số
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:  # So sánh ký tự ở hai đầu
                return False
            left += 1
            right -= 1
        return True # Trả về True nếu tất cả ký tự khớp
# @lc code=end