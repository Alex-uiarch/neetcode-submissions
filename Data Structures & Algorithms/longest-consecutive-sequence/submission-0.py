class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        max_len = 0

        for x in nums:
            if x - 1 not in nums:
                current = x
                current_len = 1
                while current + 1 in nums:
                    current += 1
                    current_len += 1
                max_len = max(max_len, current_len)
        return max_len
