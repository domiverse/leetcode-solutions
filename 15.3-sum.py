#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: # Nếu mảng có ít hơn 3 phần tử, không thể có bộ ba nào
            return [] # Trả về mảng rỗng
        nums.sort() # Sắp xếp mảng để dễ dàng tìm kiếm
        res = []      # Mảng kết quả để lưu các bộ ba
        for i in range(len(nums) - 2): # Duyệt qua mảng, dừng lại ở len(nums) - 2 để tránh tràn
            if i > 0 and nums[i] == nums[i - 1]: # Bỏ qua các phần tử trùng lặp để tránh kết quả trùng
                continue # Bỏ qua phần tử trùng lặp
            left, right = i + 1, len(nums) - 1 # Khởi tạo hai con trỏ
            while left < right: # Duyệt cho đến khi hai con trỏ gặp nhau
                total = nums[i] + nums[left] + nums[right] # Tính tổng của bộ ba
                if total == 0: # Nếu tổng bằng 0, tìm thấy một bộ ba
                    res.append([nums[i], nums[left], nums[right]]) # Thêm bộ ba vào kết quả
                    while left < right and nums[left] == nums[left + 1]: # Bỏ qua các phần tử trùng lặp bên trái
                        left += 1 # Di chuyển con trỏ trái
                    while left < right and nums[right] == nums[right - 1]: # Bỏ qua các phần tử trùng lặp bên phải
                        right -= 1 # Di chuyển con trỏ phải
                    left += 1   # Di chuyển con trỏ trái
                    right -= 1 # Di chuyển con trỏ phải
                elif total < 0: # Nếu tổng nhỏ hơn 0, cần tăng tổng lên
                    left += 1 # Di chuyển con trỏ trái sang phải
                else: # Nếu tổng lớn hơn 0, cần giảm tổng xuống
                    right -= 1 # Di chuyển con trỏ phải sang trái
        return res # Trả về mảng kết quả chứa các bộ ba
    # @lc code=end