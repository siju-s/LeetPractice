class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Set<Character>[] rows, cols, square
        // sq index 0: row 0-2, col 0-2
        // sq index 1: row 0-2, col 3-5
        // sq index 8: row 6-8, col 6-8 

        int rows = board.length;
        int cols = board[0].length;

        Set<Character>[] rowSet = new HashSet[9];
        Set<Character>[] colSet = new HashSet[9];
        Set<Character>[] cubesSet = new HashSet[9];

        for(int i = 0; i < rows; i++) {
            rowSet[i] = new HashSet<>();
            colSet[i] = new HashSet<>();
            cubesSet[i] = new HashSet<>();
        }


        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                 char ch = board[i][j];

                 if (ch == '.') continue;

                 if (rowSet[i].contains(ch)) {
                    return false;
                 }
                 rowSet[i].add(ch);

                 if (colSet[j].contains(ch)) {
                    return false;
                 }
                 colSet[j].add(ch);

                 int index = i/3 * 3 + j/3;

                 if (cubesSet[index].contains(ch)) {
                    return false;
                 }
                 cubesSet[index].add(ch);
            }
        }

        return true;

    }
}