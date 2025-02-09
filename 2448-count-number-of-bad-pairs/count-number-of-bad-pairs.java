class Solution {
    public long countBadPairs(int[] nums) {
        int n = nums.length;
        long totalPairs = ((long)n * (n - 1))/2;

        // j - i != nums[j] - nums[i]
        // nums[i] - i = nums[j] - j // Good pairs

        Map<Integer, Integer> map = new HashMap<>();
        long goodPairs = 0;

        for (int i = 0; i < n; i++) {
            int value = map.getOrDefault(nums[i] - i, 0);
            goodPairs += value;
            map.put(nums[i] - i, value + 1);
        }

        return totalPairs - goodPairs;        
    }
}