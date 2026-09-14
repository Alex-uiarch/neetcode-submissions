class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            current = nums[i]
            needed = target - current
            if needed in visited:
                return sorted([i, visited[needed]])
            else:
                visited[current] = i

