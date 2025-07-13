/*
 * @lc app=leetcode id=88 lang=java
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(nums1 == null || nums2 == null || m < 0 || n < 0) {
            return; // Trả về nếu mảng rỗng hoặc kích thước không hợp lệ
        }
        // Chỉ số cuối cùng của mảng nums1
        int i = m + n - 1;
        // Chỉ số cuối cùng của mảng nums1 và nums2
        int p1 = m - 1;
        int p2 = n - 1;
        // Gộp mảng từ cuối về đầu
        while(p1 >= 0 && p2 >= 0) {
            if(nums1[p1] > nums2[p2]) {
                nums1[i--] = nums1[p1--];
            } else {
                nums1[i--] = nums2[p2--];
            }
        }
        // Sao chép phần còn lại của mảng nums2 (nếu có)
        while(p2 >= 0) {
            nums1[i--] = nums2[p2--];
        }
    }
}
// @lc code=end

