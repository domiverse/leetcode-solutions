/*
 * @lc app=leetcode id=67 lang=java
 *
 * [67] Add Binary
 */

// @lc code=start
class Solution {
    public String addBinary(String a, String b) {
        if(a == null || a.isEmpty()) {//Kiểm tra chuỗi null hoặc rỗng
            return "0";//Khi chuỗi null hoặc rỗng thì trả về "0"
        }
        if(b == null || b.isEmpty()) {//Kiểm tra chuỗi null hoặc rỗng
            return "0";//Khi chuỗi null hoặc rỗng thì trả về "0"
        }
        StringBuilder result = new StringBuilder();//Biến để lưu kết quả
        int carry = 0;//Biến để lưu giá trị nhớ
        int i = a.length() - 1;//Chỉ số bắt đầu từ cuối chuỗi a
        int j = b.length() - 1;//Chỉ số bắt đầu từ cuối chuỗi b
        //Bắt đầu cộng từ cuối chuỗi a và b
        while(i >= 0 || j >= 0 || carry > 0) {//Kiểm tra điều kiện dừng
            if(i >= 0) {//Kiểm tra chỉ số i có hợp lệ không
                carry += a.charAt(i--) - '0';//Lấy giá trị của ký tự tại chỉ số i và cộng vào carry
            }
        if(j >= 0) {//Kiểm tra chỉ số j có hợp lệ không
            carry += b.charAt(j--) - '0';//Lấy giá trị của ký tự tại chỉ số j và cộng vào carry
        }
        result.append(carry % 2);//Thêm giá trị của carry vào kết quả
        carry /= 2;//Cập nhật giá trị của carry
    }
    return result.reverse().toString();//Trả về kết quả sau khi đảo ngược
}
}
// @lc code=end

