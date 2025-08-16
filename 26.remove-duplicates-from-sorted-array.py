#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: # Nếu mảng rỗng
            return 0 # Trả về 0 nếu không có phần tử nào
        last_unique = 0 # Khởi tạo con trỏ cho  phần tử duy nhất cuối cùng
        for i in range(1, len(nums)): # Duyệt qua mảng bắt đầu từ phần tử thứ hai
            if nums[i] != nums[last_unique]: # Nếu phần tử hiện tại khác phần tử duy nhất cuối cùng
                last_unique += 1 # Di chuyển con trỏ đến vị trí tiếp theo
                nums[last_unique] = nums[i] # Cập nhật giá trị phần tử duy nhất cuối cùng
        return last_unique + 1 # Trả về độ dài của mảng không có phần tử trùng lặp
# @lc code=end

