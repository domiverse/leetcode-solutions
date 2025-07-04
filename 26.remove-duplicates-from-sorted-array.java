
import java.util.Arrays;

/*
 * @lc app=leetcode id=26 lang=java
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0; // Trả về 0 nếu mảng rỗng
        }

        int uniqueCount = 1; // Đếm số lượng phần tử duy nhất, bắt đầu từ 1 vì phần tử đầu tiên luôn duy nhất

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[uniqueCount - 1]) { // So sánh với phần tử cuối cùng đã duy nhất
                nums[uniqueCount] = nums[i]; // Cập nhật phần tử duy nhất tiếp theo
                uniqueCount++; // Tăng số lượng phần tử duy nhất
            }
        }

        return uniqueCount; // Trả về số lượng phần tử duy nhất
    }
}
// @lc code=end

