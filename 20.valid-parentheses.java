/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        if (s == null || s.length() % 2 != 0) { // kiểm tra độ dài chuỗi
            return false;  // nếu chuỗi null hoặc độ dài lẻ thì không thể là chuỗi hợp lệ
        }
        
        Stack<Character> stack = new Stack<>(); // sử dụng ngăn xếp để kiểm tra tính hợp lệ
        for (char c : s.toCharArray()) { // duyệt từng ký tự trong chuỗi
            if (c == '(' || c == '{' || c == '[') { // nếu là dấu mở ngoặc thì đẩy vào ngăn xếp
                stack.push(c); // đẩy ký tự mở ngoặc vào ngăn xếp
            } else { // nếu là dấu đóng ngoặc
                if (stack.isEmpty()) { // nếu ngăn xếp rỗng thì không có dấu mở ngoặc tương ứng
                    return false; // không có dấu mở ngoặc tương ứng, chuỗi không hợp lệ
                } 
                char top = stack.pop(); // lấy ký tự trên cùng của ngăn xếp
                if ((c == ')' && top != '(') || // kiểm tra xem dấu đóng ngoặc có tương ứng với dấu mở ngoặc không
                    (c == '}' && top != '{') ||// kiểm tra dấu đóng ngoặc nhọn
                    (c == ']' && top != '[')) {// kiểm tra dấu đóng ngoặc vuông
                    return false;// nếu không tương ứng thì chuỗi không hợp lệ
                }
            }
        }
        // sau khi duyệt hết chuỗi, nếu ngăn xếp còn chứa dấu mở ngoặc thì chuỗi không hợp lệ

        return stack.isEmpty(); // nếu ngăn xếp rỗng thì chuỗi là hợp lệ
    }
}
// @lc code=end

