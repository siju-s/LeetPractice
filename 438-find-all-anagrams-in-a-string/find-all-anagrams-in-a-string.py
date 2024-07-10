class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result

        count_p = [0] * 26
        count_s = [0] * 26
        for ch in p:
            count_p[ord(ch) - ord('a')] += 1
  
        l = 0
        windowLen = len(p)
        
        for r in range(len(s)):
            count_s[ord(s[r]) - ord('a')] += 1

            if (r >= windowLen):
                count_s[ord(s[r - windowLen]) - ord('a')] -= 1

            if count_p == count_s:
                result.append(r - windowLen + 1)    
   

        return result        
             
  
        

        

                 
        