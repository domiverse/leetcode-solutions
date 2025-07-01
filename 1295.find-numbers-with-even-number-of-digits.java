/*
 * @lc app=leetcode id=1295 lang=java
 *
 * [1295] Find Numbers with Even Number of Digits
 */

// @lc code=start
class Solution {
    private boolean hasEvenDigits(int num) {
    int demSoChan = 0;
    while( num != 0){
        demSoChan++;
        num = num / 10;
    }
    return (demSoChan & 1) == 0;
    }

    public int findNumbers(int[] nums) {
        int tongCacSoChan = 0;
        for(int num : nums){
            if(hasEvenDigits(num))
            tongCacSoChan++;
        } 
        return tongCacSoChan;
    }
}
// @lc code=end

