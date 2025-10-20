#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root: # Nếu cây rỗng
            return [] # trả về danh sách rỗng
        from collections import defaultdict # Sử dụng defaultdict để đếm tần số
        count = defaultdict(int) # Khởi tạo bộ đếm
        def inorder(node): # Duyệt cây theo thứ tự trung vị
            if not node: # Nếu nút là None
                return # Trả về
            inorder(node.left) # Duyệt con trái
            count[node.val] += 1 # Đếm giá trị nút hiện tại
            inorder(node.right) # Duyệt con phải
        inorder(root) # Bắt đầu duyệt từ gốc
        max_count = max(count.values()) # Tìm tần số lớn nhất
        return [val for val, freq in count.items() if freq == max_count] # Trả về các giá trị có tần số lớn nhất
# @lc code=end

