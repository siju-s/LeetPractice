class Solution {

    // Time : O(2n), Space : O(1)
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] arr = new int[26];

        for (char ch : s.toCharArray()) {
            arr[ch - 'a']++;
        }

        for (char ch : t.toCharArray()) {
            int index = ch - 'a';
            arr[index]--;
            // Early termination
            if (arr[index] < 0) {
                return false;
            }
        }

        for (int num : arr) {
            if (num != 0) {
                return false;
            }
        }

        return true;



    }
}