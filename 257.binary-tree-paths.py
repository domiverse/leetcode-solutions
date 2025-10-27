#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: # Nếu cây rỗng
            return [] # Trả về danh sách rỗng
        paths = [] # Khởi tạo danh sách đường dẫn
        self.dfs(root, "", paths) # Gọi hàm dfs để tìm đường dẫn
        return paths # Trả về danh sách đường dẫn

    def dfs(self, node: Optional[TreeNode], path: str, paths: List[str]): # Hàm dfs để tìm đường dẫn
        if not node: # Nếu nút rỗng
            return # Trả về
        path += str(node.val) # Thêm giá trị nút vào đường dẫn
        if not node.left and not node.right:  # Leaf node (nút lá)
            paths.append(path) # Thêm đường dẫn vào danh sách
        else: # Nếu không phải nút lá
            path += "->" # Thêm "->" vào đường dẫn
            self.dfs(node.left, path, paths) # Gọi đệ quy cho nút bên trái
            self.dfs(node.right, path, paths) # Gọi đệ quy cho nút bên phải
# @lc code=end