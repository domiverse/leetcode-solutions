#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2: # Kiểm tra nếu cả hai danh sách đều rỗng
            raise ValueError("Both arrays are empty") # In ra lỗi
        merged = sorted(nums1 + nums2) # Gộp và sắp xếp hai danh sách
        n = len(merged) # Lấy độ dài của danh sách đã gộp
        if n % 2 == 1: # Nếu độ dài là số lẻ
            return merged[n // 2] # Trả về phần tử giữa
        else: # Nếu độ dài là số chẵn
            return (merged[n // 2 - 1] + merged[n // 2]) / 2 # Trả về trung bình của hai phần tử giữa
# @lc code=end

