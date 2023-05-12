class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> map = new HashMap<>();

        if (ransomNote.length() > magazine.length()) {
            return false;
        }
        for (char ch : magazine.toCharArray()) {
             map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        for (char ch : ransomNote.toCharArray()) {
             int freq = map.getOrDefault(ch, 0);
             if (freq == 0) {
                 return false;
             }
             map.put(ch, freq - 1);
        }

        return true;
    }
}