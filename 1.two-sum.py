#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:  # Kiểm tra xem danh sách có rỗng không
            return [] # Trả về danh sách rỗng nếu rỗng
        num_dict = {} # Tạo một từ điển để lưu trữ các số và chỉ mục của chúng
        for i, num in enumerate(nums):  # Duyệt qua từng số trong danh sách
            complement = target - num # Tính toán số cần tìm để đạt được tổng
            if complement in num_dict:  # Kiểm tra xem số cần tìm đã có trong từ điển chưa
                return [num_dict[complement], i] # Nếu có, trả về chỉ mục của nó và chỉ mục hiện tại
            num_dict[num] = i # Lưu số hiện tại và chỉ mục của nó vào từ điển
        return [] # Trả về danh sách rỗng nếu không tìm thấy cặp nào
# @lc code=end

