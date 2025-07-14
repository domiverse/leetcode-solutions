
import java.util.Arrays;

/*
 * @lc app=leetcode id=26 lang=java
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums == null || nums.length == 0) {
            return 0;
        }
        int uniqueCount = 1;
        for(int i = 1; i< nums.length; i++){
            if(nums[i] != nums[uniqueCount - 1]){
                nums[uniqueCount] = nums[i];
                uniqueCount++;
            }
        }
        return uniqueCount;
    }
}
// @lc code=end

