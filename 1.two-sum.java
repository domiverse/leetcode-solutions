/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Tạo HashMap để lưu trữ giá trị và chỉ số của các phần tử
        Map<Integer, Integer> numToIndex = new HashMap<>();
        // Duyệt qua mảng nums
        for(int i = 0; i < nums.length; i++) {
            // Tính toán giá trị cần tìm
            int phanBu = target - nums[i];
            // Kiểm tra xem giá trị cần tìm đã có trong HashMap chưa
            if (numToIndex.containsKey(phanBu)) {
                // Nếu có, trả về chỉ số của hai phần tử
                return new int[] { numToIndex.get(phanBu), i };
            }
            
            // Nếu không, lưu trữ giá trị và chỉ số hiện tại vào HashMap
            numToIndex.put(nums[i], i);
        }
        // Nếu không tìm thấy cặp nào, trả về mảng rỗng
        return new int[] {};

    }
}
// @lc code=end

        // // Kiểm tra đầu vào
        // if (nums == null || nums.length < 2) {
        //     return new int[] {}; // Trả về mảng rỗng nếu không đủ phần tử
        // }
        // // Kiểm tra xem mảng có chứa ít nhất hai phần tử không
        // if (nums.length < 2) {
        //     return new int[] {}; // Trả về mảng rỗng nếu không đủ phần tử
        // }  
        // // Kiểm tra xem target có phải là một số nguyên không
        // if (target != (int) target) {
        //     return new int[] {}; // Trả về mảng rỗng nếu target không phải là số nguyên
        // }
        // // Kiểm tra xem mảng có chứa các phần tử hợp lệ không
        // for (int num : nums) {
        //     if (num < Integer.MIN_VALUE || num > Integer.MAX_VALUE) {
        //         return new int[] {}; // Trả về mảng rỗng nếu có phần tử không hợp lệ
        //     }
        // }   
        // // Kiểm tra xem mảng có chứa các phần tử trùng lặp không
        // for (int i = 0; i < nums.length; i++) {
        //     for (int j = i + 1; j < nums.length; j++) {
        //         if (nums[i] == nums[j]) {
        //             return new int[] {}; // Trả về mảng rỗng nếu có phần tử trùng lặp
        //         }
        //     }
        // }
        // // Kiểm tra xem mảng có chứa các phần tử âm không
        // for (int num : nums) {
        //     if (num < 0) {
        //         return new int[] {}; // Trả về mảng rỗng nếu có phần tử âm
        //     }
        // }
        // // Kiểm tra xem mảng có chứa các phần tử lớn hơn 100 không
        // for (int num : nums) {
        //     if (num > 100) {
        //         return new int[] {}; // Trả về mảng rỗng nếu có phần tử lớn hơn 100
        //     }
        // }
        // // Kiểm tra xem mảng có chứa các phần tử nhỏ hơn 0 không
        // for (int num : nums) {
        //     if (num < 0) {
        //         return new int[] {}; // Trả về mảng rỗng nếu có phần tử nhỏ hơn 0
        //     }
        // }   
