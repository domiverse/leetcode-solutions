/*
 * @lc app=leetcode id=88 lang=java
 *
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {// Hàm gộp hai mảng đã sắp xếp nums1 và nums2 vào nums1
        if(nums1 == null || nums2 == null || m < 0 || n < 0) { // Kiểm tra mảng nums1 và nums2 có null hoặc kích thước không hợp lệ
            return; // Trả về nếu mảng rỗng hoặc kích thước không hợp lệ
        }
        // Chỉ số cuối cùng của mảng nums1
        int i = m + n - 1; // Chỉ số cuối cùng của mảng nums1 sau khi gộp
        // Chỉ số cuối cùng của mảng nums1 và nums2
        int p1 = m - 1; // Chỉ số cuối cùng của mảng nums1 (phần đã sắp xếp)
        int p2 = n - 1; // Chỉ số cuối cùng của mảng nums2 (phần đã sắp xếp)
        // Gộp mảng từ cuối về đầu
        while(p1 >= 0 && p2 >= 0) { // Trong khi còn phần tử trong cả hai mảng
            if(nums1[p1] > nums2[p2]) { // So sánh phần tử cuối cùng của nums1 và nums2
                nums1[i--] = nums1[p1--]; // So sánh và chèn phần tử lớn hơn vào cuối mảng nums1
            } else {// Nếu phần tử của nums2 lớn hơn hoặc bằng
                nums1[i--] = nums2[p2--]; // Chèn phần tử của nums2 vào cuối mảng nums1
            } // Giảm chỉ số i để tiếp tục chèn phần tử tiếp theo
        }
        // Sao chép phần còn lại của mảng nums2 (nếu có)
        while(p2 >= 0) { // Nếu còn phần tử trong nums2
            nums1[i--] = nums2[p2--];// Chèn phần tử của nums2 vào mảng nums1
        }
    }
}
// @lc code=end

