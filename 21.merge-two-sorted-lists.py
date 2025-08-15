#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: # Nếu list1 rỗng
            return list2 # Trả về list2     
        if not list2: # Nếu list2 rỗng
            return list1 # Trả về list1
        if list1.val < list2.val: # Nếu giá trị của list1 nhỏ hơn list2
            list1.next = self.mergeTwoLists(list1.next, list2) # Gọi đệ quy với phần còn lại của list1 và toàn bộ list2
            return list1 # Trả về list1
        else: # Nếu giá trị của list1 lớn hơn hoặc bằng list2
            list2.next = self.mergeTwoLists(list1, list2.next) # Gọi đệ quy với toàn bộ list1 và phần còn lại của list2
            return list2 # Trả về list2
# @lc code=end

