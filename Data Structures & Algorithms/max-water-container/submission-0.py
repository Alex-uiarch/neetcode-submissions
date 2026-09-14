class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        max_area = 0

        while left < right:
            s = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, s)

            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1

        return max_area
