#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: # Kiểm tra nếu danh sách rỗng
            return None # Trả về None nếu danh sách rỗng
        num_dict = {} # Sử dụng từ điển để đếm số lần xuất hiện của mỗi số
        for num in nums: # Duyệt qua từng số trong danh sách
            num_dict[num] = num_dict.get(num, 0) + 1  # Đếm số lần xuất hiện
        for num, count in num_dict.items(): # Tìm số xuất hiện một lần
            if count == 1: # Nếu số xuất hiện một lần
                return num # Trả về số đó
        return None # Trả về None nếu không tìm thấy số nào xuất hiện một lần
# @lc code=end