#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: # Kiểm tra nếu cây rỗng
            return [] # Trả về danh sách rỗng nếu cây rỗng
        # Truy cập đệ quy vào cây con bên trái và bên phải
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        # Trả về danh sách kết quả theo thứ tự duyệt
        return left + right + [root.val]
# @lc code=end

