/*
 * @lc app=leetcode id=66 lang=java
 *
 * [66] Plus One
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {
        if (digits == null || digits.length == 0) { // Kiểm tra mảng rỗng hoặc null
            return new int[]{1}; // Trả về mảng chứa 1 nếu mảng rỗng
        }
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) { // Duyệt từ phải sang trái
            if (digits[i] < 9) { // Nếu phần tử nhỏ hơn 9
                digits[i]++; // Tăng phần tử lên 1
                return digits; // Trả về mảng đã cập nhật
            }
            digits[i] = 0; // Nếu phần tử bằng 9, đặt thành 0
        }
        // Nếu tất cả các phần tử đều là 9
        int[] newNumber = new int[n + 1];
        newNumber[0] = 1; // Đặt phần tử đầu tiên là 1
        return newNumber; // Trả về mảng mới
    }
}
// @lc code=end

