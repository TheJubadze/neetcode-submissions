class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
        let w = 0
        for(let r = 0; r < nums.length; r++) {
            if(nums[r] != val) {
                nums[w] = nums[r];
                w++;
            }
        }
        return w;
    }
}
