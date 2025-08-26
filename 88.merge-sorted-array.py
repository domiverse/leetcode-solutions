#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: # Nếu nums2 rỗng
            return # Không làm gì cả
        i, j, k = m - 1, n - 1, m + n - 1 # Khởi tạo các chỉ số
        while j >= 0: # Trong khi còn phần tử trong nums2
            if i >= 0 and nums1[i] > nums2[j]: # So sánh phần tử
                nums1[k] = nums1[i] # Di chuyển phần tử trong nums1
                i -= 1 # Giảm chỉ số i
            else: # Nếu phần tử trong nums2 lớn hơn hoặc bằng
                nums1[k] = nums2[j] # Di chuyển phần tử trong nums2
                j -= 1 # Giảm chỉ số j
            k -= 1 # Giảm chỉ số k

# @lc code=end

