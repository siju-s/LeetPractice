class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = HashMap<Int, Int>()

        for (i in nums.indices) {
            val num = nums[i]
            if (map.containsKey(num)) {
                return intArrayOf(map.getOrDefault(num, 0), i)
            }
            else {
                map.put(target - num, i)    
            }
        }

        return intArrayOf(0, 0)
    }
}