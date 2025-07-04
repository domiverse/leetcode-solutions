/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> danhSach = new HashMap<>();
        for(int i =0; i< nums.length; i++){
            danhSach.put(nums[i], i);
        }
        for(int i = 0; i< nums.length; i++){
            int phanBu = target - nums[i];
            if(danhSach.containsKey(phanBu) && danhSach.get(phanBu) != i){
                return new int[]{i, danhSach.get(phanBu)};
            }
        }
        return new int[]{};
    }
}
// @lc code=end