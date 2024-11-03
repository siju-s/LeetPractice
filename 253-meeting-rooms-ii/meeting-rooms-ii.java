class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        PriorityQueue<Integer> queue = new PriorityQueue<>();

        for (int[] interval : intervals) {
            if(!queue.isEmpty() && queue.peek() <= interval[0]) {
                queue.poll();
            }

            queue.offer(interval[1]);
        }

        return queue.size();

    
    }
}