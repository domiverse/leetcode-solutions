
import java.awt.font.NumericShaper;

/*
 * @lc app=leetcode id=1480 lang=java
 *
 * [1480] Running Sum of 1d Array
 */

// @lc code=start
class Solution {
    public int[] runningSum(int[] nums) {
        int[] result = new int[nums.length]; // Tạo mảng kết quả cùng kích thước với mảng nums
        result[0] = nums[0]; // Gán giá trị đầu tiên của mảng kết quả bằng giá trị đầu tiên của mảng nums

        for (int i = 1; i < nums.length; i++) { // Duyệt qua các phần tử từ chỉ số 1 đến cuối mảng
            result[i] = result[i - 1] + nums[i]; // Cộng giá trị hiện tại với giá trị trước đó trong mảng kết quả
        }

        return result; // Trả về mảng kết quả
    }
}
// @lc code=end

