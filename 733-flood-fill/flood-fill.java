class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        // 1. Change starting pixel to target color
        // 2. If adjacent pixels (dfs) matches the original color, change
        int original = image[sr][sc];

        if (original != color) {
            floodFill(image, sr, sc, original, color);
        }

        return image;
    }

    private void floodFill(int[][] image, int r, int c, int source, int target) {
        int rows = image.length;
        int cols = image[0].length;

        if (r < 0 || r >= rows || c < 0 || c >= cols || image[r][c] != source) return;
        
        image[r][c] = target;

        floodFill(image, r + 1, c, source, target);
        floodFill(image, r - 1, c, source, target);
        floodFill(image, r, c + 1, source, target);
        floodFill(image, r, c - 1, source, target);

    }
}