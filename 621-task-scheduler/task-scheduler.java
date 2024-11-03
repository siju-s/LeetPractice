class Solution {
    // SC: O(26) -> O(1)
    // TC: O(m) where m->tasks
    public int leastInterval(char[] tasks, int n) {
        // Build freq map
        int[] freq = new int[26];

        for (char task : tasks) {
            freq[task - 'A']++;
        }

        // Convert freq to PQ
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int cnt : freq) {
            if (cnt > 0) {
                maxHeap.add(cnt);
            }
        }
        // queue to store (count, time when available) 
        Queue<int[]> queue = new LinkedList<>();
        int time = 0;
        while (!maxHeap.isEmpty() || !queue.isEmpty()) {
            time++;
            // If heap empty, jump to queue time
            if (maxHeap.isEmpty()) {
               time = queue.peek()[1];
            }
            else {
                int count = maxHeap.poll() - 1;
                if (count > 0) {
                    queue.add(new int[]{count, time + n});
                }
            }
            if (!queue.isEmpty() && queue.peek()[1] == time) {
                maxHeap.offer(queue.poll()[0]);
            }
        }

        return time;
    }
}
