
import java.util.List;


/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
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
    public ListNode addTwoNumbers(ListNode hangToa1, ListNode hangToa2) {
        ListNode dummyHead = new ListNode(0); // Tạo nút giả để dễ quản lý
        ListNode current = dummyHead; // Biến để duyệt qua danh sách mới   
        int carry = 0; // Biến để lưu trữ giá trị nhớ khi cộng
        while (hangToa1 != null || hangToa2 != null || carry >
                0) { // Tiếp tục khi còn nút trong danh sách hoặc còn giá trị nhớ
            int sum = carry; // Bắt đầu với giá trị nhớ
            if (hangToa1 != null) { // Nếu còn nút trong danh sách đầu tiên
                sum += hangToa1.val; // Cộng giá trị của nút vào tổng
                hangToa1 = hangToa1.next; // Di chuyển đến nút tiếp theo
            }
            if (hangToa2 != null) { // Nếu còn nút trong danh sách thứ hai
                sum += hangToa2.val; // Cộng giá trị của nút vào tổng
                hangToa2 = hangToa2.next; // Di chuyển đến nút tiếp theo
            }
            carry = sum / 10; // Tính giá trị nhớ cho lần cộng tiếp theo
            current.next = new ListNode(sum % 10); // Tạo nút mới với giá trị là phần dư
            current = current.next; // Di chuyển đến nút mới
        }
        return dummyHead.next; // Trả về danh sách kết quả (bỏ qua nút giả)
    }
}

// @lc code=end

