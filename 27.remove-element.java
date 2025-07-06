
import java.util.HashMap;

/*
 * @lc app=leetcode id=27 lang=java
 *
 * [27] Remove Element
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        int soBatDau = 0; // Biến để đếm số lượng phần tử khác giá trị val
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != val){ // Nếu phần tử hiện tại không bằng val
                // Đặt phần tử khác val vào vị trí soBatDau
                nums[soBatDau] = nums[i]; // Cập nhật mảng tại vị trí soBatDau
                // Tăng biến soBatDau để chỉ đến vị trí tiếp theo
                soBatDau++;// Tăng số lượng phần tử khác val
            }
        }
        return soBatDau;
    }
}
// @lc code=end

