/*
 * @lc app=leetcode id=1295 lang=java
 *
 * [1295] Find Numbers with Even Number of Digits
 */

// @lc code=start
class Solution {
    private boolean hasEvenDigits(int num) {
    int demSoChan = 0; // Biến để đếm số chữ số chẵn
    while( num != 0){  // Duyệt qua từng chữ số của số num
        demSoChan++; // Tăng biến đếm mỗi khi có một chữ số
        num = num / 10; // Chia số num cho 10 để loại bỏ chữ số cuối cùng
    } // Kiểm tra xem số chữ số chẵn có phải là số chẵn hay không
    return (demSoChan & 1) == 0; // Sử dụng toán tử AND để kiểm tra tính chẵn lẻ của số chữ số
    } // Hàm kiểm tra xem số có số chữ số chẵn hay không

    public int findNumbers(int[] nums) { // Hàm chính để tìm số lượng số có số chữ số chẵn
        int tongCacSoChan = 0; // Biến để lưu trữ tổng số lượng số có số chữ số chẵn
        for(int num : nums){ // Duyệt qua từng số trong mảng nums
            if(hasEvenDigits(num)) // Kiểm tra xem số hiện tại có số chữ số chẵn hay không
            tongCacSoChan++; // Nếu có, tăng biến đếm tổng số lượng số có số chữ số chẵn
        }  //   Trả về tổng số lượng số có số chữ số chẵn
        return tongCacSoChan; // Trả về tổng số lượng số có số chữ số chẵn
    } // Hàm chính để tìm số lượng số có số chữ số chẵn
} 
// @lc code=end

