/*
 * @lc app=leetcode id=70 lang=java
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) { // Trả về n nếu n nhỏ hơn hoặc bằng 2
            return n;
        }
        int[] dp = new int[n + 1]; // Tạo mảng dp để lưu số cách leo cầu thang
        dp[1] = 1; // Có 1 cách để leo 1 bậc
        dp[2] = 2; // Có 2 cách để leo 2 bậc
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2]; // Công thức quy hoạch động
        }
        return dp[n]; // Trả về số cách leo n bậc
    }
}
// @lc code=end

