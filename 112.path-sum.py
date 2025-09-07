#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # Nếu node hiện tại là None, trả về False
            return False # Không có đường đi nào
        if not root.left and not root.right: # Nếu node hiện tại là lá (không có con)
            return targetSum == root.val # Kiểm tra nếu targetSum trừ đi giá trị node hiện tại bằng 0
        targetSum -= root.val # Giảm targetSum bằng giá trị của node hiện tại
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)   # Đệ quy kiểm tra con trái và con phải với targetSum đã giảm
# @lc code=end

