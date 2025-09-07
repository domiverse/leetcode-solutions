#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: # Nếu numRows là 0, trả
            return [] # Trả về danh sách rỗng
        triangle = [] # Khởi tạo danh sách để lưu các hàng của tam giác
        for i in range(numRows): # Lặp qua số hàng từ 0 đến numRows - 1
            row = [1] * (i + 1) # Tạo hàng mới với tất cả các phần tử là 1
            for j in range(1, i): # Lặp qua các phần tử từ 1 đến i - 1 (bỏ qua hai đầu là 1)
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]    # Mỗi phần tử là tổng của hai phần tử phía trên nó trong tam giác
            triangle.append(row) # Thêm hàng mới vào tam giác
        return triangle # Trả về tam giác hoàn chỉnh
# @lc code=end

