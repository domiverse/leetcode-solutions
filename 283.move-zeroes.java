/*
 * @lc app=leetcode id=283 lang=java
 *
 * [283] Move Zeroes
 */

// @lc code=start
class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) return; // Kiểm tra mảng rỗng hoặc null
        int lastNonZeroIndex = 0; // Chỉ số của phần tử khác không cuối cùng
        for (int i = 0; i < nums.length; i++) { // Duyệt qua từng phần tử trong mảng
            if (nums[i] != 0) { // Nếu phần tử khác không
                nums[lastNonZeroIndex] = nums[i]; // Đặt phần tử khác không vào vị trí cuối cùng của các phần tử khác không
                lastNonZeroIndex++; // Tăng chỉ số của phần tử khác không cuối cùng
            }
        }
        // Điền các phần tử còn lại bằng 0
        for (int i = lastNonZeroIndex; i < nums.length; i++) {
            nums[i] = 0; // Đặt các phần tử còn lại thành 0
        }
    }
}
// @lc code=end

