#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) # Tạo một nút giả để bắt đầu danh sách kết quả
        current = dummy # Biến current sẽ dùng để xây dựng danh sách kết quả
        carry = 0 # Biến carry để lưu trữ giá trị chuyển tiếp khi tổng vượt quá 10

        while l1 or l2 or carry: # Duyệt qua cả hai danh sách và kiểm tra xem có giá trị carry không
            val1 = l1.val if l1 else 0 # Lấy giá trị của nút l1, nếu không có thì dùng 0
            val2 = l2.val if l2 else 0 # Lấy giá trị của nút l2, nếu không có thì dùng 0
            total = val1 + val2 + carry # Tính tổng của hai giá trị và giá trị carry
            carry = total // 10 # Cập nhật giá trị carry
            current.next = ListNode(total % 10) # Tạo nút mới với giá trị là tổng modulo 10
            current = current.next # Di chuyển current đến nút mới
            if l1: # Di chuyển l1 đến nút tiếp theo nếu có
                l1 = l1.next 
            if l2: # Di chuyển l2 đến nút tiếp theo nếu có
                l2 = l2.next

        return dummy.next # Trả về danh sách kết quả bắt đầu từ nút tiếp theo của nút giả