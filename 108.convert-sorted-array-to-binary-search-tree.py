#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: # Kiểm tra mảng rỗng
            return None # Trả về None nếu mảng rỗng
        mid = len(nums) // 2 # Tìm chỉ số giữa
        root = TreeNode(nums[mid]) # Tạo nút gốc
        root.left = self.sortedArrayToBST(nums[:mid]) # Tạo cây con bên trái
        root.right = self.sortedArrayToBST(nums[mid + 1:]) # Tạo cây con bên phải
        return root # Trả về nút gốc
# @lc code=end

