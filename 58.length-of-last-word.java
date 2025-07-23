/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        if(s == null || s.isEmpty()) {//Kiểm tra chuỗi null hoặc rỗng
            return 0;//Khi chuỗi null hoặc rỗng thì trả về 0
        }
        int length = 0;//Biến để lưu độ dài của từ cuối cùng
        //Bắt đầu từ cuối chuỗi và bỏ qua các khoảng trắng
        int i = s.length() - 1;//Chỉ số bắt đầu từ cuối chuỗi
        //Bỏ qua các khoảng trắng ở cuối chuỗi
        while(i >= 0 && s.charAt(i) == ' ') {//Kiểm tra xem ký tự có phải là khoảng trắng không
            i--;//Giảm chỉ số i nếu ký tự là khoảng trắng
        }//Nếu i < 0 thì chuỗi chỉ có khoảng trắng
        //Đếm độ dài của từ cuối cùng   
        while(i >= 0 && s.charAt(i) != ' ') {//Kiểm tra xem ký tự có phải là khoảng trắng không
            length++;//Nếu ký tự không phải là khoảng trắng thì tăng độ dài
            i--;//Giảm chỉ số i để kiểm tra ký tự tiếp theo
        }//Khi i < 0 thì đã kiểm tra hết chuỗi
        //Trả về độ dài của từ cuối cùng
        return length;
    }
}
// @lc code=end

