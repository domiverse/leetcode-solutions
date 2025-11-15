#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if not nums: # kiểm tra danh sách rỗng
            return 0 # Trả về 0 nếu danh sách rỗng 
        count = 0 # Khởi tạo biến đếm
        for num in nums: # Duyệt qua từng số trong danh sách
            if len(str(num)) % 2 == 0: # Kiểm tra số chữ số
                count += 1 # Tăng biến đếm nếu số có số chữ số chẵn
        return count # Trả về số lượng số có số chữ số chẵn
# @lc code=end

