class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] bucket = new ArrayList[nums.length + 1];

        // Bucket sort
        for (int key : map.keySet()) {
            int freq =  map.get(key);
                  if(bucket[freq]==null) {
                    bucket[freq] = new ArrayList<>();
                  }
             bucket[freq].add(key);
        }

        List<Integer> res = new ArrayList<>();
        for (int idx = bucket.length - 1; idx >= 0;  idx--) {
             if(bucket[idx]!= null){
                List<Integer> list = bucket[idx]; 
                res.addAll(list);
             }
             if (res.size() >= k) break;
        }

        int[] arr = res.stream().mapToInt(Integer::intValue).toArray();
        return arr;

    }
}