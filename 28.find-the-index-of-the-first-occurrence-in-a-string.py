#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: # Nếu needle rỗng, trả về 0
            return 0 # Nếu needle rỗng, trả về 0
        for i in range(len(haystack) - len(needle) + 1): # Duyệt qua từng vị trí có thể của needle trong haystack
            if haystack[i:i + len(needle)] == needle: # Nếu tìm thấy needle trong haystack
                return i # Trả về vị trí tìm thấy
        return -1 # Nếu không tìm thấy needle, trả về -1
# @lc code=end

