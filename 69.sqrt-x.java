/*
 * @lc app=leetcode id=69 lang=java
 *
 * [69] Sqrt(x)
 */

// @lc code=start
class Solution {
    public int mySqrt(int x) {
        if (x < 2) { // Trả về x nếu x nhỏ hơn 2
            return x;
        }
        int left = 2, right = x / 2; // Thiết lập giới hạn tìm kiếm
        while (left <= right) { // Vòng lặp tìm kiếm nhị phân
            int mid = left + (right - left) / 2; // Tính giá trị giữa
            long square = (long) mid * mid; // Tính bình phương của mid
            if (square == x) { // Nếu bình phương bằng x, trả về mid
                return mid;
            } else if (square < x) { // Nếu bình phương nhỏ hơn x, cập nhật left
                left = mid + 1;
            } else { // Nếu bình phương lớn hơn x, cập nhật right
                right = mid - 1;
            }
        }
        return right; // Trả về giá trị gần nhất dưới căn bậc hai của x
    } 
}
// @lc code=end

