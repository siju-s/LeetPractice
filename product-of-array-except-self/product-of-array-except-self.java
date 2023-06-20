class Solution {
    // public int[] productExceptSelf(int[] nums) {
    //     int[] leftProd = new int[nums.length];
    //     int[] rightProd = new int[nums.length];
    //     int[] ans = new int[nums.length];

    //     leftProd[0] = 1;
    //     rightProd[nums.length - 1] = 1;
    //     for (int i = 1; i < nums.length; i++) {
    //         leftProd[i] = nums[i - 1] * leftProd[i - 1]; 
    //     }

    //     for (int i = nums.length - 2; i >= 0; i--) {
    //         rightProd[i] = nums[i + 1] * rightProd[i + 1]; 
    //     }

    //     for (int i = 0; i < nums.length; i++) {
    //         ans[i] = leftProd[i] * rightProd[i];
    //     }

    //     return ans;
    // }

    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];

        ans[0] = 1;

        for (int i = 1; i < nums.length; i++) {
            ans[i] = nums[i - 1] * ans[i - 1]; 
        }

        int prod = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            ans[i] = ans[i] * prod;
            prod = prod * nums[i]; 
        }
        return ans;
    }
}