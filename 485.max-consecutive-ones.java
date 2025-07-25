/*
 * @lc app=leetcode id=485 lang=java
 *
 * [485] Max Consecutive Ones
 */

// @lc code=start
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0; // Biến để lưu trữ số lượng 1 liên tiếp lớn nhất
        int currentCount = 0; // Biến để đếm số lượng 1 liên tiếp hiện tại
        for (int num : nums) { // Duyệt qua từng phần tử trong mảng
            if (num == 1) { // Nếu phần tử là 1
                currentCount++; // Tăng số lượng 1 liên tiếp hiện tại
            } else { // Nếu phần tử không phải là 1
                maxCount = Math.max(maxCount, currentCount); // Cập nhật số lượng 1 liên tiếp lớn nhất nếu cần
                currentCount = 0; // Đặt lại số lượng 1 liên tiếp hiện tại về 0
            }
        }
        return Math.max(maxCount, currentCount); // Trả về số lượng 1 liên tiếp lớn nhất
    } 
}
// @lc code=end

