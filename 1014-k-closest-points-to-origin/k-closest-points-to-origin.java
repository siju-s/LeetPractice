// class Element {
//     double value;
//     int index;

//     public Element(double value, int index) {
//         this.value = value;
//         this.index = index;
//     }
// }

// class Solution {
//     public int[][] kClosest(int[][] points, int k) {
//         PriorityQueue<Element> minHeap = new PriorityQueue<>((a,b) -> Double.compare(a.value, b.value));

//         for (int i = 0; i < points.length; i++) {
//             int[] point = points[i];
//             double distance = calculateDistance(point[0], 0, point[1], 0);
//             minHeap.add(new Element(distance, i));
//         }
//         int[][] result = new int[k][2];

//         int index = 0;
//         while (k > 0) {
//             Element minElement = minHeap.poll();
//             result[index] = points[minElement.index];
//             index++;
//             k--;
//         }

//         return result;
//     }

//     private double calculateDistance(int x1, int x2, int y1, int y2) {
//         return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
//     }


// }

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a,b) -> Integer.compare(a[0], b[0]));

        for (int i = 0; i < points.length; i++) {
            int[] point = points[i];
            int distance = point[0] * point[0] + point[1] * point[1];
            minHeap.offer(new int[]{distance, point[0], point[1]});
        }
        int[][] result = new int[k][2];

        int index = 0;
        while (k > 0) {
            int[] elements = minHeap.poll();
            result[index] = new int[]{elements[1], elements[2]};
            index++;
            k--;
        }

        return result;
    }
}    
