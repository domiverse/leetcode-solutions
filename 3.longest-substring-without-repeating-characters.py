#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {} # Sử dụng từ điển để lưu trữ vị trí của các ký tự
        left = 0 # Biến left để đánh dấu vị trí bắt đầu của chuỗi con không lặp lại
        max_length = 0 # Biến max_length để lưu trữ độ dài lớn nhất của chuỗi con không lặp lại

        for right in range(len(s)): # Duyệt qua từng ký tự trong chuỗi
            if s[right] in char_map: # Nếu ký tự đã xuất hiện trong từ điển
                left = max(left, char_map[s[right]] + 1) # Cập nhật vị trí bắt đầu của chuỗi con không lặp lại
            char_map[s[right]] = right # Cập nhật vị trí của ký tự hiện tại trong từ điển
            max_length = max(max_length, right - left + 1) # Cập nhật độ dài lớn nhất của chuỗi con không lặp lại

        return max_length # Trả về độ dài lớn nhất của chuỗi con không lặp lại
     # @lc code=end