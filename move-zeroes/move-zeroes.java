class Solution {
    public void moveZeroes(int[] nums) {
        int j = 0;

        for(int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (num != 0) {
                nums[j] = nums[i];
                j++;
            }
        }

        for (; j < nums.length; j++) {
            nums[j] = 0;
        }
    }
}