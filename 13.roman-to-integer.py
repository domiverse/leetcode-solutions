#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = { # Bản đồ ánh xạ ký tự La Mã sang giá trị số nguyên
            'I': 1, # Một
            'V': 5, # Năm
            'X': 10, # Mười
            'L': 50, # Năm mươi
            'C': 100, # Một trăm
            'D': 500, # Năm trăm
            'M': 1000 # Một nghìn   
        } # Tạo một từ điển để ánh xạ ký tự La Mã sang giá trị số nguyên

        total = 0 # Biến total để lưu trữ tổng giá trị
        prev_value = 0 # Biến prev_value để lưu trữ giá trị của ký tự trước đó

        for char in s: # Duyệt qua từng ký tự trong chuỗi La Mã
            current_value = roman_map[char] # Lấy giá trị của ký tự hiện tại từ bản đồ
            if current_value > prev_value: # Nếu giá trị hiện tại lớn hơn giá trị trước đó
                total += current_value - 2 * prev_value # Trừ đi giá trị trước đó hai lần (vì đã cộng vào trước đó)
            else: # Nếu giá trị hiện tại nhỏ hơn hoặc bằng giá trị trước đó
                total += current_value # Cộng giá trị hiện tại vào tổng
            prev_value = current_value # Cập nhật giá trị trước đó thành giá trị hiện tại
            
        return total # Trả về tổng giá trị của chuỗi La Mã
        
# @lc code=end

