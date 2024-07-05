class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
         map = {}

         for i, num in enumerate(nums):
            print("pos is ", i, "num is ", num)

            if map.get(num, -1) == -1:
                map[num] = i

            else:
                pos = map[num]
                if abs(pos - i) <= k:
                    return True
                elif abs(pos - i) > k:
                     map[num] = i


         return False                


        