#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: # Kiêm tra cây rỗng
            return True # Cây rỗng được coi là cân bằng
        def height(node): # Hàm đệ quy để tính chiều cao của cây con
            if not node: # Nếu node là None, trả về chiều cao 0
                return 0 # Chiều cao của cây rỗng là 0
            left_height = height(node.left) # Tính chiều cao của cây con bên trái
            if left_height == -1: # Nếu cây con bên trái không cân bằng, trả về -1
                return -1 # Cây không cân bằng
            right_height = height(node.right) # Tính chiều cao của cây con bên phải
            if right_height == -1: # Nếu cây con bên phải không cân bằng, trả về -1
                return -1 # Cây không cân bằng
            if abs(left_height - right_height) > 1: # Kiểm tra sự chênh lệch chiều cao giữa hai cây con
                return -1 # Cây không cân bằng
            return max(left_height, right_height) + 1 # Trả về chiều cao của cây hiện tại   
        return height(root) != -1 # Kiểm tra nếu cây cân bằng hay không
# @lc code=end

