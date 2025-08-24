#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: # trường hợp cơ bản
            return n # trả về n
        first = 1 # số cách để lên bậc 1
        second = 2 # số cách để lên bậc 2
        for i in range(3, n + 1): # lặp từ bậc 3 đến bậc n
            third = first + second # số cách để lên bậc i là tổng số cách để lên bậc i-1 và i-2
            first = second # cập nhật số cách để lên bậc i-1
            second = third # cập nhật số cách để lên bậc i-2
        return second # trả về số cách để lên bậc n
# @lc code=end

