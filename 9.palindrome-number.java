/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false; // Số âm không thể là palindrome
        }
        int nguyenBan = x;
        int daoNguoc = 0;
        
        while(x > 0){
            int donVi = x % 10; // Lấy chữ số cuối cùng của x
            daoNguoc = daoNguoc * 10 + donVi; // Thêm chữ số vào daoNguoc
            x = x / 10; // Loại bỏ chữ số cuối cùng khỏi x
        }
        return nguyenBan == daoNguoc; // Kiểm tra xem số gốc có bằng số đảo ngược không
    }
}
// @lc code=end
