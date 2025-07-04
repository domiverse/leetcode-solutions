
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
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;

        while (hangToa1 != null || hangToa2 != null || carry > 0) {
            int sum = carry;
            if (hangToa1 != null) {
                sum += hangToa1.val;
                hangToa1 = hangToa1.next;
            }
            if (hangToa2 != null) {
                sum += hangToa2.val;
                hangToa2 = hangToa2.next;
            }

            carry = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;
        }

        return dummy.next;
    }
}

// @lc code=end

