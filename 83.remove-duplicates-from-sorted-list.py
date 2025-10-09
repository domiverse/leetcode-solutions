#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: # kiểm tra nếu danh sách rỗng
            return head # Trả về danh sách rỗng
        current = head # Khởi tạo con trỏ hiện tại
        while current and current.next: # Lặp qua danh sách
            if current.val == current.next.val: # Nếu giá trị của nút hiện tại bằng giá trị của nút tiếp theo
                current.next = current.next.next # Bỏ qua nút tiếp theo
            else: # Nếu không
                current = current.next # Di chuyển con trỏ hiện tại đến nút tiếp theo
        return head # Trả về đầu danh sách đã được xử lý
# @lc code=end

