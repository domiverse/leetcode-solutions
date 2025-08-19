#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: # Nếu danh sách rỗng
            return 0 # Nếu không có phần tử nào, chèn vào vị trí 0
        low, high = 0, len(nums) - 1 # Khởi tạo chỉ số thấp và cao
        while low <= high: # Tiến hành tìm kiếm nhị phân
            mid = (low + high) // 2 # Tính chỉ số giữa
            if nums[mid] == target: # Nếu tìm thấy phần tử bằng target
                return mid # Trả về chỉ số của phần tử
            elif nums[mid] < target: # Nếu phần tử giữa nhỏ hơn target
                low = mid + 1 # Tìm kiếm ở nửa phải
            else: # Nếu phần tử giữa lớn hơn target
                high = mid - 1 # Tìm kiếm ở nửa trái
        return low # Trả về vị trí chèn
# @lc code=end

