/*
 * @lc app=leetcode id=35 lang=java
 *
 * [35] Search Insert Position
 */

// @lc code=start
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0; // Khởi tạo chỉ số trái
        int right = nums.length - 1; // Khởi tạo chỉ số phải
        while (left <= right) { // Khi chỉ số trái không vượt quá chỉ số phải
            int mid = left + (right - left) / 2; // Tính chỉ số giữa
            if (nums[mid] == target) { // Nếu phần tử giữa bằng target
                return mid; // Trả về chỉ số giữa
            } else if (nums[mid] < target) { // Nếu phần tử giữa nhỏ hơn target
                left = mid + 1; // Di chuyển chỉ số trái sang phải
            } else { // Nếu phần tử giữa lớn hơn target
                right = mid - 1; // Di chuyển chỉ số phải sang trái
            }
        }
        return left; // Nếu không tìm thấy, trả về chỉ số chèn
    }
}
// @lc code=end

