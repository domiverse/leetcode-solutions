#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        start, end = 0, 0 # Biến start và end để lưu trữ vị trí bắt đầu và kết thúc của chuỗi con đối xứng dài nhất

        for i in range(len(s)): # Duyệt qua từng ký tự trong chuỗi
            len1 = self.expandAroundCenter(s, i, i) # Tính độ dài của chuỗi con đối xứng với i là tâm
            len2 = self.expandAroundCenter(s, i, i + 1) # Tính độ dài của chuỗi con đối xứng với i và i + 1 là tâm
            max_len = max(len1, len2) # Lấy độ dài lớn nhất giữa hai chuỗi con đối xứng
            if max_len > end - start:   # Nếu độ dài lớn nhất lớn hơn độ dài hiện tại
                start = i - (max_len - 1) // 2 # Cập nhật vị trí bắt đầu
                end = i + max_len // 2 

        return s[start:end + 1] # Trả về chuỗi con đối xứng dài nhất

    def expandAroundCenter(self, s, left, right): # Mở rộng từ tâm
        while left >= 0 and right < len(s) and s[left] == s[right]: # Kiểm tra xem hai ký tự ở hai bên có bằng nhau không
            left -= 1 # Giảm left để mở rộng về bên trái
            right += 1 # Tăng right để mở rộng về bên phải
        return right - left - 1 # Trả về độ dài của chuỗi con đối xứng
    # @lc code=end
