class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums) 
        dp[0] = 1





        
        for i in range(1, len(nums)):
            maximum = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    maximum = max(maximum, dp[j])
                dp[i] = maximum + 1

        return max(dp)


            