#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: # Kiểm tra nếu danh sách rỗng
            return None # Trả về None nếu danh sách rỗng
        count = 0 # Biến đếm để theo dõi số lần xuất hiện của phần tử
        candidate = None # Biến để lưu trữ phần tử ứng cử viên
        for num in nums: # Duyệt qua từng phần tử trong danh sách
            if count == 0: # Nếu biến đếm bằng 0, cập nhật phần tử ứng cử viên
                candidate = num # Cập nhật phần tử ứng cử viên
            count += (1 if num == candidate else -1) # Tăng hoặc giảm biến đếm
        return candidate # Trả về phần tử ứng cử viên
# @lc code=end