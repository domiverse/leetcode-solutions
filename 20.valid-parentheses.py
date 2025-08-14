#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: # Nếu chuỗi rỗng  
            return True #trả về True nếu chuỗi rỗng
        stack = [] # Khởi tạo stack
        mapping = {")": "(", "}": "{", "]": "["} # Khởi tạo mapping
        for char in s: # Duyệt từng ký tự trong chuỗi
            if char in mapping: # Nếu ký tự là dấu ngoặc đóng
                top_element = stack.pop() if stack else "#" # Lấy phần tử trên cùng của stack
                if mapping[char] != top_element: # Nếu không khớp với dấu ngoặc mở
                    return False # Trả về False nếu không khớp
            else: # Nếu ký tự là dấu ngoặc mở
                stack.append(char) # Thêm dấu ngoặc mở vào stack
        return not stack # Trả về True nếu stack rỗng, ngược lại trả về False
# @lc code=end

