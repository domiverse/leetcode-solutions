/*
 * @lc app=leetcode id=13 lang=java
 *
 * [13] Roman to Integer
 */

// @lc code=start
class Solution {
    public int romanToInt(String s) {
        int total = 0; // Biến để lưu tổng giá trị của các ký tự La Mã
        int prevValue = 0; // Biến để lưu giá trị của ký tự trước
        for (int i = s.length() - 1; i >= 0; i--) { // Duyệt chuỗi từ phải sang trái
            char c = s.charAt(i); // Lấy ký tự hiện tại
            int value = getValue(c); // Lấy giá trị của ký tự La Mã

            if (value < prevValue) { // Nếu giá trị hiện tại nhỏ hơn giá trị trước
                total -= value; // Trừ giá trị hiện tại khỏi tổng
            } else {
                total += value; // Ngược lại, cộng giá trị hiện tại vào tổng
            }
            prevValue = value; // Cập nhật giá trị trước cho lần lặp tiếp theo
        }
        return total;
    }

    private int getValue(char c) { // Hàm để lấy giá trị của ký tự La Mã
        // Sử dụng switch để xác định giá trị tương ứng với ký tự La Mã
        switch (c) {    // Trả về giá trị tương ứng với ký tự La Mã
            case 'I':   // Giá trị của 'I' là 1
                return 1;   // Giá trị của 'I' là 1
            case 'V':   // Giá trị của 'V' là 5
                return 5;   // Giá trị của 'V' là 5
            case 'X':   // Giá trị của 'X' là 10
                return 10;  // Giá trị của 'X' là 10
            case 'L':   // Giá trị của 'L' là 50
                return 50;  // Giá trị của 'L' là 50
            case 'C':  // Giá trị của 'C' là 100
                return 100; // Giá trị của 'C' là 100
            case 'D':  // Giá trị của 'D' là 500
                return 500; // Giá trị của 'D' là 500
            case 'M':  // Giá trị của 'M' là 1000
                return 1000; // Giá trị của 'M' là 1000
            default: // Nếu ký tự không hợp lệ, trả về 0
                return 0; // Giá trị mặc định là 0 nếu ký tự không hợp lệ
        } 

    }
}
// @lc code=end

