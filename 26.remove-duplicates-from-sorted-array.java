
import java.util.Arrays;

/*
 * @lc app=leetcode id=26 lang=java
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) { // Kiểm tra mảng rỗng
            return 0; // Trả về 0 nếu mảng rỗng
        } // Nếu mảng không rỗng, bắt đầu xử lý
        // Biến uniqueCount để đếm số lượng phần tử duy nhất
        int uniqueCount = 1; // Biến đếm số lượng phần tử duy nhất, bắt đầu từ 1 vì phần tử đầu tiên luôn duy nhất
        for (int i = 1; i < nums.length; i++) { // Duyệt từ phần tử thứ hai
            // So sánh với phần tử trước đó
            if (nums[i] != nums[uniqueCount - 1]) { // Nếu phần tử hiện tại khác phần tử cuối cùng duy nhất
                // Gán phần tử hiện tại vào vị trí tiếp theo của mảng duy nhất
                nums[uniqueCount] = nums[i]; // Ghi đè phần tử tại vị trí uniqueCount
                // Tăng biến đếm số lượng phần tử duy nhất
                uniqueCount++; // Tăng số lượng phần tử duy nhất
            } // Nếu phần tử hiện tại bằng phần tử cuối cùng duy nhất, không làm gì cả
        } // Kết thúc vòng lặp, mảng đã được xử lý
        // Mảng nums đã được cập nhật với các phần tử duy nhất ở đầu mảng
        return uniqueCount; // Trả về số lượng phần tử duy nhất
    }
}
// @lc code=end

