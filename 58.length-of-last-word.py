#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: # Kiểm tra chuỗi rỗng
            return 0 # Trả về 0 nếu chuỗi rỗng
        words = s.split() # Tách chuỗi thành danh sách các từ
        return len(words[-1]) if words else 0 # Trả về độ dài của từ cuối cùng
# @lc code=end

