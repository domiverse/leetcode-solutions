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
        ListNode dauTau = new ListNode(0);
        ListNode anhBocHang = dauTau;
        int hangTon = 0;
        while(hangToa1 != null || hangToa2 != null || hangTon != 0){
            int bangKiemToa1 = (hangToa1 != null) ? hangToa1.val : 0;
            int bangKiemToa2 = (hangToa2 != null) ? hangToa2.val : 0;
            int tongHang = bangKiemToa1 + bangKiemToa2 + hangTon;
            hangTon = tongHang / 10;
            anhBocHang.next = new ListNode(tongHang % 10);
            anhBocHang = anhBocHang.next;
            if(hangToa1 != null) hangToa1 = hangToa1.next;
            if(hangToa2 != null) hangToa2 = hangToa2.next;
        }
        return dauTau.next;
    }
}
// @lc code=end

