#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root: #Trường hợp cây rỗng
            return [] #Trả về danh sách rỗng
        stack = []  #Khởi tạo ngăn xếp
        result = [] #Danh sách kết quả
        current = root # Bắt đầu từ nút gốc
        while current or stack: # Lặp cho đến khi không còn nút nào để xử lý
            while current: # Duyệt đến nút trái nhất
                stack.append(current) # Thêm nút hiện tại vào ngăn xếp
                current = current.left # Di chuyển sang nút trái
            current = stack.pop() # Lấy nút trên cùng của ngăn xếp
            result.append(current.val) # Thêm giá trị của nút vào kết quả
            current = current.right # Di chuyển sang nút phải
        return result # Trả về danh sách kết quả
# @lc code=end

