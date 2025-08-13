#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:  # Tìm chiều sâu tối đa
            return 0  # Chiều sâu tối đa của cây rỗng là 0
        left_depth = self.maxDepth(root.left)  # Chiều sâu tối đa của cây con bên trái
        right_depth = self.maxDepth(root.right)  # Chiều sâu tối đa của cây con bên phải
        return 1 + max(left_depth, right_depth)  # Chiều sâu tối đa của cây là 1 + chiều sâu tối đa của cây con
# @lc code=end

