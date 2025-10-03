#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 0: # kiểm tra nếu số cột không hợp lệ
            return "" # Trả về chuỗi rỗng nếu số cột không hợp lệ
        result = [] # Khởi tạo danh sách để lưu trữ các ký tự
        while columnNumber > 0: # Lặp cho đến khi số cột trở về 0
            columnNumber -= 1 # Giảm số cột đi 1 để xử lý hệ thống 0-indexed
            remainder = columnNumber % 26 # Tính phần dư khi chia cho 26
            char = chr(remainder + ord('A')) # Chuyển phần dư thành ký tự tương ứng
            result.append(char) # Thêm ký tự vào danh sách kết quả
            columnNumber //= 26 # Cập nhật số cột bằng cách chia nguyên cho 26
        return "".join(reversed(result)) # Trả về chuỗi kết quả sau khi đảo ngược danh sách
# @lc code=end

