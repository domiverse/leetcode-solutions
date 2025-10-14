#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:  # Nếu cây rỗng
            return 0  # Trả về 0    
        if root.left and not root.left.left and not root.left.right:  # Nếu nút trái là lá
            return root.left.val + self.sumOfLeftLeaves(root.right)  # Trả về giá trị của lá trái + đệ quy bên phải
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)  # Đệ quy cả hai bên
# @lc code=end

