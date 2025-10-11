#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums: # kiểm tra danh sách rỗng
            return [] # Trả về danh sách rỗng nếu đầu vào rỗng
        running_sum = [nums[0]] # Khởi tạo danh sách chạy
        for i in range(1, len(nums)): # Tính tổng dồn
            running_sum.append(running_sum[i - 1] + nums[i]) # Cập nhật tổng dồn
        return running_sum # Trả về danh sách tổng dồn
# @lc code=end

