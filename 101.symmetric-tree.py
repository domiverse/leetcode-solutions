#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isMirror(root, root) # Kiểm tra xem cây có đối xứng hay không   

    def isMirror(self, t1, t2):  # Hàm kiểm tra xem hai cây con có đối xứng hay không
        if not t1 and not t2: # Nếu cả hai nút đều là None, chúng là đối xứng
            return True # Nếu cả hai nút đều là None, chúng là đối xứng
        if not t1 or not t2: # Nếu một trong hai nút là None, chúng không đối xứng
            return False   # Nếu một trong hai nút là None, chúng không đối xứng
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left) # So sánh giá trị của hai nút và đệ quy kiểm tra các nút con bên trái và bên phải
# @lc code=end

