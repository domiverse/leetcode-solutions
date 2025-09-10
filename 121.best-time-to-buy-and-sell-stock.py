#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  # Kiểm tra nếu danh sách giá rỗng
            return 0 # Trả về 0 nếu không có giá nào
        min_price = float('inf') # Khởi tạo giá mua tối thiểu với giá vô hạn
        max_profit = 0 # Khởi tạo lợi nhuận tối đa là 0
        for price in prices: # Duyệt qua từng giá trong danh sách
            if price < min_price: # Nếu giá hiện tại thấp hơn giá mua tối thiểu
                min_price = price # Cập nhật giá mua tối thiểu
            elif price - min_price > max_profit: # Nếu lợi nhuận hiện tại lớn hơn lợi nhuận tối đa
                max_profit = price - min_price # Cập nhật lợi nhuận tối đa
        return max_profit # Trả về lợi nhuận tối đa
# @lc code=end