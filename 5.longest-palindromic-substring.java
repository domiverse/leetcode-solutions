/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) {// Trả về chuỗi rỗng nếu s là null hoặc độ dài nhỏ hơn 1
            return ""; // Trả về chuỗi rỗng
        } // Khởi tạo biến để theo dõi vị trí và độ dài của chuỗi đối xứng dài nhất
        int start = 0, end = 0; // Vị trí bắt đầu và kết thúc của chuỗi đối xứng dài nhất
        for (int i = 0; i < s.length(); i++) { // Duyệt qua từng ký tự trong chuỗi
            int len1 = expandAroundCenter(s, i, i); // Kiểm tra đối xứng với một ký tự trung tâm
            int len2 = expandAroundCenter(s, i, i + 1); // Kiểm tra đối xứng với hai ký tự trung tâm
            int len = Math.max(len1, len2); // Lấy độ dài lớn nhất giữa hai trường hợp
            if (len > end - start) { // Nếu độ dài lớn hơn độ dài hiện tại
                start = i - (len - 1) / 2; // Cập nhật vị trí bắt đầu
                end = i + len / 2; // Cập nhật vị trí kết thúc
            }
        }
        return s.substring(start, end + 1);// Trả về chuỗi con từ vị trí bắt đầu đến kết thúc
    }

    private int expandAroundCenter(String s, int left, int right) {// Hàm mở rộng từ trung tâm để tìm chuỗi đối xứng
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {// Kiểm tra điều kiện biên và đối xứng
            left--;// Giảm left để mở rộng về phía bên trái
            right++;// Mở rộng về hai phía
        }
        return right - left - 1;// Trả về độ dài của chuỗi đối xứng tìm được
    }
}
// @lc code=end

