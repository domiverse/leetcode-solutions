#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  # Nếu cây rỗng
            return None  # Trả về None
        # Hoán đổi con trái và con phải
        root.left, root.right = root.right, root.left 
        # Đệ quy hoán đổi con trái và con phải
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# @lc code=end

