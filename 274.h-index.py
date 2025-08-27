#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: # Kiểm tra danh sách trống
            return 0 # Trả về 0 nếu không có tài liệu nào
        citations.sort(reverse=True)  # Sắp xếp theo thứ tự giảm dần
        for i, c in enumerate(citations): # Duyệt qua từng tài liệu
            if i + 1 > c: # Nếu số lượng tài liệu đã duyệt lớn hơn số trích dẫn
                return i # Trả về chỉ số tài liệu
        return len(citations) # Trả về số lượng tài liệu nếu không tìm thấy chỉ số nào
# @lc code=end

