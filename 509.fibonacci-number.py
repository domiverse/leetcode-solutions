#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:  # nếu n là 0 hoặc 1
            return n  # Trả về n
        return self.fib(n - 1) + self.fib(n - 2)  # Tính toán số Fibonacci
# @lc code=end

