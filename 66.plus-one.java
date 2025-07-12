/*
 * @lc app=leetcode id=66 lang=java
 *
 * [66] Plus One
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {
        if(digits == null || digits.length == 0){
            return new int[]{1}; // Trả về mảng mới với giá trị 1 nếu mảng rỗng
        }
        int n = digits.length;
        for(int i = n - 1; i >= 0; i--){
            if(digits[i] < 9){
                digits[i]++;
                return digits; // Nếu không phải 9, chỉ cần cộng 1 và trả về
            }
            digits[i] = 0; // Nếu là 9, đặt thành 0 và tiếp tục
        }
        // Nếu tất cả các phần tử đều là 9
        int[] newNumber = new int[n + 1];
        newNumber[0] = 1;
        return newNumber;
    }
}
// @lc code=end

