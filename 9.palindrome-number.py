#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: # Số âm không thể là đối xứng
            return False #  Trả về False nếu x là số âm
        elif x < 10: # Số đơn vị (0-9) luôn là đối xứng
            return True # Trả về True nếu x là số đơn vị
        elif x == 0: # Số 0 cũng là đối xứng
            return True # Trả về True nếu x là số 0
        else: # Với các số lớn hơn 9
            reversed_num = 0 # Biến để lưu trữ số đảo ngược
            original_num = x # Lưu trữ giá trị ban đầu của x
            while x > 0: # Lặp cho đến khi x trở về 0
                digit = x % 10 # Lấy chữ số cuối cùng của x
                reversed_num = reversed_num * 10 + digit # Thêm chữ số vào số đảo ngược
                x //= 10 # Loại bỏ chữ số cuối cùng khỏi x
            return original_num == reversed_num # So sánh số ban đầu với số đảo ngược để kiểm tra đối xứng

# @lc code=end

