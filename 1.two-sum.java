/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int tong) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int phan_bu = tong - nums[i];
            if (map.containsKey(phan_bu) && map.get(phan_bu) !=i){
                return new int[] {i, map.get(phan_bu)};
            }
        }
        return new int[]{};
}}

// @lc code=end

