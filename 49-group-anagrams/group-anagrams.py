class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs:
            arr = [0] * 26

            for ch in str:
                arr[ord(ch) - ord("a")]+=1

            result[tuple(arr)].append(str) 
        
        return result.values()