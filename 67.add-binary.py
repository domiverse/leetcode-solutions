#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b: # Nếu một trong hai chuỗi rỗng
            return a or b # Nếu cả hai chuỗi đều rỗng, trả về chuỗi không rỗng
        max_len = max(len(a), len(b)) # Tính chiều dài tối đa
        a = a.zfill(max_len) # Điền thêm số 0 vào đầu chuỗi a
        b = b.zfill(max_len) # Điền thêm số 0 vào đầu chuỗi b
        carry = 0 # Biến nhớ để lưu trữ giá trị nhớ
        result = [] # Danh sách để lưu trữ kết quả
        for i in range(max_len - 1, -1, -1): # Duyệt từ phải sang trái
            total = carry + (1 if a[i] == '1' else 0) + (1 if b[i] == '1' else 0) # Tính tổng
            result.append('1' if total % 2 == 1 else '0') # Thêm bit kết quả vào danh sách
            carry = 1 if total > 1 else 0 # Cập nhật giá trị nhớ
        if carry: # Nếu còn giá trị nhớ
            result.append('1') # Thêm bit nhớ vào danh sách
        return ''.join(reversed(result)) # Trả về chuỗi nhị phân kết quả
# @lc code=end

