/*
 * @lc app=leetcode id=83 lang=java
 *
 * [83] Remove Duplicates from Sorted List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null; // Nếu danh sách rỗng, trả về null
        ListNode current = head; // Khởi tạo con trỏ current tại đầu danh sách
        while (current != null && current.next != null) { // Duyệt qua danh sách
            if (current.val == current.next.val) { // Nếu giá trị của nút hiện tại bằng giá trị của nút tiếp theo
                current.next = current.next.next; // Bỏ qua nút tiếp theo
            } else { // Nếu giá trị khác nhau
                current = current.next; // Di chuyển con trỏ đến nút tiếp theo
            }
        } // Kết thúc vòng lặp khi không còn nút tiếp theo hoặc đã duyệt hết danh sách
        return head; // Trả về đầu danh sách đã được loại bỏ các phần tử trùng lặp
    }
}
// @lc code=end

