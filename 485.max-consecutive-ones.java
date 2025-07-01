/*
 * @lc app=leetcode id=485 lang=java
 *
 * [485] Max Consecutive Ones
 */

// @lc code=start
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
            int maxConsecutive = 0;
            int conTro = 0;
            for(int i = 0; i < nums.length; i++){
                if(nums[i] == 0){
                    conTro = 0;
                }else{
                    conTro++;
                }if(conTro > maxConsecutive){
                    maxConsecutive = conTro;
                }
            }
            return maxConsecutive;
        }
    }
// @lc code=end

