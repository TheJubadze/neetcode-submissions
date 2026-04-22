class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let w = 1;
        for (let r = 1; r < nums.length; r++)
            if (nums[r - 1] !== nums[r])
                nums[w++] = nums[r];

        return w;
    }
}
