/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        // Kiểm tra xem mảng có rỗng không
        if(strs == null || strs.length == 0){
            return "";
        }
        // Giả sử chuỗi đầu tiên là tiền tố chung
        String prefix = strs[0];
            // So sánh với từng chuỗi trong mảng
                // Nếu không phải tiền tố, cắt bớt
               for(int i = 1; i < strs.length; i++){
                while(strs[i].indexOf(prefix) !=0){
                    prefix = prefix.substring(0, prefix.length()-1);
                }
               }
               return prefix;
    }
}
// @lc code=end

