
import java.util.List;

/*
 * @lc app=leetcode id=21 lang=java
 *
 * [21] Merge Two Sorted Lists
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0); // Tạo nút giả để dễ dàng thao tác
        ListNode current = dummy; // Biến current để theo dõi nút cuối cùng
        while (list1 != null && list2 != null) { // Duyệt cả hai danh sách
            if (list1.val <= list2.val) { // So sánh giá trị của hai nút
                current.next = list1; // Gắn nút từ list1 vào danh sách kết quả
                list1 = list1.next; // Di chuyển con trỏ list1
            } else {
                current.next = list2; // Gắn nút từ list2 vào danh sách kết quả
                list2 = list2.next; // Di chuyển con trỏ list2
            }
            current = current.next; // Di chuyển con trỏ current
        }
        // Nếu một trong hai danh sách còn nút, gắn phần còn lại vào danh sách kết quả
        if (list1 != null) {
            current.next = list1; // Gắn phần còn lại của list1
        } else {
            current.next = list2; // Gắn phần còn lại của list2
        }
        return dummy.next; // Trả về danh sách đã hợp nhất, bắt đầu từ nút tiếp theo của nút giả
    }
}
// @lc code=end

