#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: # Nếu rowIndex là 0, trả về hàng đầu tiên
            return [1] # Hàng đầu tiên chỉ có một phần tử là 1
        row = [1] # Khởi tạo hàng đầu tiên
        for i in range(1, rowIndex + 1): # Duyệt qua các hàng tiếp theo
            # Tính toán các giá trị trong hàng tiếp theo
            new_row = [1] * (i + 1) # Tạo hàng mới với tất cả các phần tử là 1
            for j in range(1, i): # Lặp qua các phần tử từ 1 đến i - 1 (bỏ qua hai đầu là 1)
                new_row[j] = row[j - 1] + row[j] # Mỗi phần tử là tổng của hai phần tử phía trên nó trong tam giác
            row = new_row # Cập nhật hàng hiện tại  
        return row # Trả về hàng cuối cùng
# @lc code=end

