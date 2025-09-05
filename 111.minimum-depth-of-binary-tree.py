#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # Kiêm tra cây rỗng
            return 0 # Chiều sâu của cây rỗng là 0
        if not root.left and not root.right: # Nếu node là lá (không có con trái và con phải)
            return 1 # Chiều sâu tối thiểu là 1
        if not root.left: # Nếu không có con trái
            return 1 + self.minDepth(root.right) # Đệ quy tính chiều sâu bên phải
        if not root.right: # Nếu không có con phải
            return 1 + self.minDepth(root.left) # Đệ quy tính chiều sâu bên trái
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) # Trả về chiều sâu tối thiểu giữa hai cây con
# @lc code=end

