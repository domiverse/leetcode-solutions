#
# @lc app=leetcode id=1255 lang=python3
#
# [1255] Maximum Score Words Formed by Letters
#

# @lc code=start
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if not words or not letters:  # Kiểm tra đầu vào
            return 0  # Trả về 0 nếu không có từ hoặc chữ cái

        letter_count = Counter(letters)  # Đếm số lượng chữ cái
        max_score = 0  # Điểm số tối đa

        def backtrack(index, current_score, current_count):  # Hàm quay lui
            nonlocal max_score  # Tham chiếu đến biến max_score bên ngoài
            if index == len(words):  # Nếu đã duyệt hết các từ
                max_score = max(max_score, current_score)  # Cập nhật điểm số tối đa
                return  # Trả về nếu đã duyệt hết các từ

            # Skip the current word
            backtrack(index + 1, current_score, current_count)  # Bỏ qua từ hiện tại

            # Include the current word
            word = words[index]  # Lấy từ hiện tại
            word_count = Counter(word)  # Đếm số lượng chữ cái trong từ
            if all(word_count[c] <= letter_count[c] for c in word_count):  # Kiểm tra xem có thể tạo từ không
                # Update the letter count
                for c in word_count:  # Cập nhật số lượng chữ cái
                    letter_count[c] -= word_count[c]  # Giảm số lượng chữ cái đã sử dụng
                backtrack(index + 1, current_score + sum(score[ord(c) - ord('a')] for c in word), current_count + 1)  # Gọi đệ quy với từ hiện tại
                # Backtrack the letter count
                for c in word_count:  # Khôi phục số lượng chữ cái
                    letter_count[c] += word_count[c]  # Khôi phục số lượng chữ cái

        backtrack(0, 0, 0)  # Bắt đầu quay lui từ chỉ số 0
        return max_score  # Trả về điểm số tối đa
# @lc code=end

