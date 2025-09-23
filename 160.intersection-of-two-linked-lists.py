#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: # Kiểm tra nếu một trong hai danh sách liên kết rỗng
            return None # Trả về None nếu một trong hai danh sách liên kết rỗng
        pointerA, pointerB = headA, headB # Khởi tạo hai con trỏ cho hai danh sách liên kết
        while pointerA != pointerB: # Lặp cho đến khi hai con trỏ gặp nhau
            pointerA = pointerA.next if pointerA else headB # Di chuyển con trỏ A hoặc chuyển sang đầu danh sách B nếu đã đến cuối
            pointerB = pointerB.next if pointerB else headA # Di chuyển con trỏ B hoặc chuyển sang đầu danh sách A nếu đã đến cuối
        return pointerA # Trả về nút giao nhau hoặc None nếu không có giao nhau
# @lc code=end

