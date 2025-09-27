#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if not columnTitle: # kiểm tra nếu chuỗi rỗng
            return 0 # Trả về 0 nếu chuỗi rỗng
        result = 0 # Biến để lưu trữ kết quả
        for char in columnTitle: # Duyệt qua từng ký tự trong chuỗi
            result = result * 26 + (ord(char) - ord('A') + 1) # Cập nhật kết quả theo hệ cơ số 26
        return result # Trả về kết quả cuối cùng
# @lc code=end

