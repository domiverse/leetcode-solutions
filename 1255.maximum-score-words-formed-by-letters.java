

/*
 * @lc app=leetcode id=1255 lang=java
 *
 * [1255] Maximum Score Words Formed by Letters
 */

// @lc code=start
class Solution {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
             int W = words.length; // Lấy độ dài của mảng words
        int[] freq = new int[26]; // Mảng để lưu trữ tần suất của các chữ cái trong mảng letters
        for (char c : letters) { // Duyệt qua từng chữ cái trong mảng letters
            // Tăng tần suất của chữ cái tương ứng trong mảng freq
            freq[c - 'a']++; // Chuyển đổi ký tự thành chỉ số tương ứng trong mảng freq
        }
        int maxScore = 0 ; // Biến để lưu trữ điểm số lớn nhất
        // Duyệt qua tất cả các tập con của từ
        // Iterate over every subset of words
        int[] subsetLetters = new int[26]; // Mảng để lưu trữ tần suất của các chữ cái trong tập con từ
        for (int mask = 0; mask < 1 << W; mask++) { // Duyệt qua tất cả các mặt nạ từ 0 đến 2^W - 1
            // Reset the subsetLetters array 
            Arrays.fill(subsetLetters, 0); // Đặt lại mảng subsetLetters về 0
            for (int i = 0; i < W; i++) { // Duyệt qua từng từ
                if ((mask & (1 << i)) > 0) { // Kiểm tra xem từ i có được chọn trong tập con hay không
                    // Nếu từ i được chọn, cập nhật tần suất của các chữ cái trong mảng subsetLetters
                    int L = words[i].length(); // Lấy độ dài của từ i
                    for (int j = 0; j < L; j++) { // Duyệt qua từng ký tự trong từ i
                        subsetLetters[words[i].charAt(j) - 'a']++; // Tăng tần suất của ký tự tương ứng trong mảng subsetLetters
                    } // Cập nhật tần suất của các chữ cái trong mảng subsetLetters
                } // Nếu từ i không được chọn, không làm gì cả
            } // Tính điểm số của tập con từ hiện tại
            maxScore = Math.max( // Cập nhật điểm số lớn nhất
                maxScore, // So sánh điểm số hiện tại với điểm số lớn nhất
                subsetScore(subsetLetters, score, freq) // Tính điểm số của tập con từ hiện tại
            ); // Cập nhật điểm số lớn nhất nếu cần
        } // Trả về điểm số lớn nhất
        return maxScore; // Trả về điểm số lớn nhất
    } // Hàm tính điểm số của tập con từ

    private int subsetScore(int[] subsetLetters, int[] score, int[] freq) { // Hàm tính điểm số của tập con từ
        int totalScore = 0; // Biến để lưu trữ tổng điểm số của tập con từ
        // Duyệt qua từng chữ cái trong bảng chữ cái
        for (int c = 0; c < 26; c++) { // Duyệt qua từng chữ cái từ 'a' đến 'z'
            totalScore += subsetLetters[c] * score[c]; // Tính điểm số của chữ cái c trong tập con từ
            // Kiểm tra xem chúng ta có đủ mỗi chữ cái để tạo thành tập con từ này không
            if (subsetLetters[c] > freq[c]) { // Nếu tần suất của chữ cái c trong tập con từ lớn hơn tần suất trong mảng letters
                return 0; // Trả về 0 nếu không đủ chữ cái để tạo thành tập con từ
            } // Nếu đủ chữ cái, tiếp tục tính điểm số
        } // Trả về tổng điểm số của tập con từ
        return totalScore; // Trả về tổng điểm số của tập con từ
    } // Hàm tính điểm số của tập con từ
} 
// @lc code=end

