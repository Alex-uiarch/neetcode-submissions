class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)

        half = (n + m + 1) // 2
        left = 0
        right = n

        while left <= right:
            i = (left + right) // 2
            j = half - i

            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < n else float('inf')
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < m else float('inf')

            if nums1_left > nums2_right:
                right = i - 1
            elif nums2_left > nums1_right:
                left = i + 1
            else:
                break

        left_max = max(nums1[i - 1] if i > 0 else float('-inf'), nums2[j - 1] if j > 0 else float('-inf'))

        if (n + m) % 2 == 0:
            right_min = min(nums1[i] if i < n else float('inf'), nums2[j] if j < m else float('inf'))
            return (left_max + right_min) / 2
        return left_max


        
