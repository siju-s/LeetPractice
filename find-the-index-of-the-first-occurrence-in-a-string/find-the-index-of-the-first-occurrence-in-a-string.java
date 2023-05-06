class Solution {
    public int strStr(String haystack, String needle) {
        
        if (needle.isEmpty()) {
            return 0;
        }
        // Return -1 if haystack len < needle len, 
        if (haystack.length() < needle.length()) {
            return -1;
        }
        
        // Window size is len of needle
        int windowSize = needle.length();
        

        for (int i = 0; i < haystack.length(); i++) {
            
            int hayIdx = i;
            int needleIdx = 0; //Resetting to 0 at every iteration to check from start of needle
            
            while(hayIdx < haystack.length() && needleIdx < needle.length() && haystack.charAt(hayIdx)
                  == needle.charAt(needleIdx)) {
                      hayIdx++;
                      needleIdx++;
            }
                  
            if (needleIdx == needle.length()) {
                return i;
            }      
            
        }
                  
        return -1;
    }
}