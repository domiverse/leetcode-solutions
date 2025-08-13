#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:  # Kiểm tra xem danh sách có rỗng không
            return ""  # Nếu rỗng, trả về chuỗi rỗng
        min_str = min(strs)  # Tìm chuỗi nhỏ nhất trong danh sách
        max_str = max(strs)  # Tìm chuỗi lớn nhất trong danh sách
        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:  # So sánh từng ký tự
                return min_str[:i]  # Trả về tiền tố chung
        return min_str  # Nếu không có khác biệt, trả về chuỗi nhỏ nhất
# @lc code=end
