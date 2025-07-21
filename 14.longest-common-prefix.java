/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        // Kiểm tra xem mảng có rỗng không
        if (strs == null || strs.length == 0) {
            return ""; // Trả về chuỗi rỗng nếu mảng rỗng
        }
        String prefix = strs[0]; // Giả sử chuỗi đầu tiên là tiền tố chung
        for (int i = 1; i < strs.length; i++) { // Duyệt qua các chuỗi còn lại
            while (strs[i].indexOf(prefix) != 0) { // Kiểm tra xem tiền tố có phải là tiền tố chung không
                prefix = prefix.substring(0, prefix.length() - 1); // Nếu không, giảm dần độ dài của tiền tố
                if (prefix.isEmpty()) { // Nếu tiền tố trở thành rỗng
                    return ""; // Trả về chuỗi rỗng
                }
            }
        }
        return prefix; // Trả về tiền tố chung dài nhất
    }
}
// @lc code=end

