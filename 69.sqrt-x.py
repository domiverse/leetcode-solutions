#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: # Kiểm tra trường hợp đặc biệt
            return x # Trả về x nếu x < 2
        left, right = 1, x // 2 # Khởi tạo left và right cho tìm kiếm nhị phân
        while left <= right: # Tiến hành tìm kiếm nhị phân
            mid = (left + right) // 2 # Tính toán giá trị giữa
            if mid * mid == x: # Kiểm tra nếu mid là căn bậc hai chính xác
                return mid # Trả về mid nếu tìm thấy căn bậc hai chính xác
            elif mid * mid < x: # Nếu mid * mid nhỏ hơn x
                left = mid + 1 # Tìm kiếm nửa bên phải
            else: # Nếu mid * mid lớn hơn x
                right = mid - 1 # Tìm kiếm nửa bên trái
        return right # Trả về right vì đây là căn bậc hai lớn nhất không vượt quá x
# @lc code=end

