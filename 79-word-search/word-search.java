class Solution {
    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;

        boolean[][] visited = new boolean[rows][cols];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == word.charAt(0) && dfs(board, i, j, 0, word, visited)) {
                    return true;
                }
            }
        }

        return false;        
    }

    private boolean dfs(char[][] board, int row, int col, int index, String word, boolean[][] visited) {
           int rows = board.length;
            int cols = board[0].length;
          if (index == word.length()) {
              return true;
          }
          if (row < 0 || row >= rows || col < 0 || col >= cols || visited[row][col] == true || word.charAt(index) != board[row][col]) return false;

          visited[row][col] = true;

          if (dfs(board, row + 1, col, index + 1, word, visited) || dfs(board, row - 1, col, index + 1, word, visited) || dfs(board, row, col + 1, index + 1, word, visited) || dfs(board, row, col - 1, index + 1, word, visited)) {
            return true;
          }

          visited[row][col] = false;       

          return false;
    }
}