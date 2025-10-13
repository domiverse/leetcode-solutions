#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:  # Kiểm tra nếu cây rỗng
            return 0  # Trả về 0 nếu cây rỗng
        left_depth = self.getDepth(root.left) # Độ sâu bên trái
        right_depth = self.getDepth(root.right) # Độ sâu bên phải
        if left_depth == right_depth: # Nếu độ sâu bên trái và bên phải bằng nhau
            return (1 << left_depth) + self.countNodes(root.right) # Tính số nút
        else: # Nếu độ sâu bên trái và bên phải không bằng nhau
            return (1 << right_depth) + self.countNodes(root.left) # Tính số nút

    def getDepth(self, node: Optional[TreeNode]) -> int: # Hàm tính độ sâu
        depth = 0 # Khởi tạo độ sâu
        while node: # Duyệt cây bên trái
            depth += 1 # Tăng độ sâu
            node = node.left # Chuyển sang nút bên trái
        return depth # Trả về độ sâu
# @lc code=end

