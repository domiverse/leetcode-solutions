/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false; // Số âm không thể là palindrome
        }
        int original = x;
        int reversed = 0;

        while (x > 0) {
            int digit = x % 10; // Lấy chữ số cuối cùng của x
            reversed = reversed * 10 + digit; // Thêm chữ số vào reversed
            x /= 10; // Loại bỏ chữ số cuối cùng khỏi x
        }

        return original == reversed; // Kiểm tra xem số gốc có bằng số đảo ngược không
    }
}
// @lc code=end

