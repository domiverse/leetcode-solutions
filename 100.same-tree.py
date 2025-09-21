#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q: # nếu cả hai nút đều là None, chúng là giống nhau
            return True # Nếu cả hai nút đều là None, chúng là giống nhau
        if not p or not q: # Nếu một trong hai nút là None, chúng không giống nhau
            return False # Nếu một trong hai nút là None, chúng không giống nhau
        if p.val != q.val: # Nếu giá trị của hai nút khác nhau, chúng không giống nhau
            return False # Nếu giá trị của hai nút khác nhau, chúng không giống nhau
        # Kiểm tra các nút con
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # Đệ quy kiểm tra các nút con bên trái và bên phải

# @lc code=end

