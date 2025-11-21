
import java.util.Arrays;

/*
 * @lc app=leetcode id=274 lang=java
 *
 * [274] H-Index
 */

// @lc code=start

class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations); // xếp mảng citations theo thứ tự tăng dần
        int n = citations.length; // Lấy độ dài của mảng citations
        for (int i = 0; i < n; i++) { // Duyệt qua từng phần tử trong mảng
            if (citations[i] >= n - i) { // Kiểm tra nếu số lượng trích dẫn của phần tử hiện tại lớn hơn hoặc bằng số lượng bài báo còn lại
                return n - i; // Trả về chỉ số h-index, tức là số lượng bài báo có ít nhất h trích dẫn
            }
        }
        return 0; // Nếu không tìm thấy h-index, trả về 0
    }
}
// @lc code=end

