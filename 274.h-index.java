/*
 * @lc app=leetcode id=274 lang=java
 *
 * [274] H-Index
 */

// @lc code=start

class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        for(int i = 0; i< citations.length ; i++){
            if(citations[i] >=citations.length-i){
                return citations.length-i;
            }
        }
        return 0;
    }
}g
// @lc code=end

