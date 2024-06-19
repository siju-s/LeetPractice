class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, p = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if (nums1[i] > nums2[j]):
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            print(nums1[p])
            p -= 1

        while i >= 0:
            nums1[p] = nums1[i]
            i -= 1
            p -= 1

        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1            
        