/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)){
            return false;
        }
        int soDao = 0;
        while(x > soDao){
            int soHangDonVi = x % 10;
            soDao = soDao * 10 + soHangDonVi;
            x = x / 10;
        }
        return x == soDao || x == soDao / 10;
    }
}
// @lc code=end

