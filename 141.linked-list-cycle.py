#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:  # Kiểm tra nếu danh sách rỗng
            return False  # Trả về False nếu danh sách rỗng
        slow = head  # Khởi tạo con trỏ chậm
        fast = head  # Khởi tạo con trỏ nhanh
        while fast and fast.next:  # Lặp cho đến khi con trỏ nhanh hoặc con trỏ tiếp theo là None
            slow = slow.next  # Di chuyển con trỏ chậm một bước
            fast = fast.next.next  # Di chuyển con trỏ nhanh hai bước
            if slow == fast:  # Nếu hai con trỏ gặp nhau
                return True  # Trả về True nếu có vòng lặp
        return False  # Trả về False nếu không có vòng lặp
# @lc code=end

