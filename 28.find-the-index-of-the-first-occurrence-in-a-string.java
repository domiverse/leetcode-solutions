/*
 * @lc app=leetcode id=28 lang=java
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) { // Kiểm tra nếu needle là chuỗi rỗng
            return 0; // Trả về 0 nếu needle là chuỗi rỗng
        }
        int haystackLength = haystack.length(); // Lấy độ dài của haystack
        int needleLength = needle.length(); // Lấy độ dài của needle
        // Duyệt qua haystack từ đầu đến cuối, nhưng dừng trước khi đến vị trí mà needle có thể bắt đầu
        for (int i = 0; i <= haystackLength - needleLength; i++) {
            // So sánh phần con của haystack với needle
            if (haystack.substring(i, i + needleLength).equals(needle)) {
                return i; // Trả về chỉ số nếu tìm thấy needle
            }
        }
        return -1; // Nếu không tìm thấy, trả về -1
    }
}
// @lc code=end

