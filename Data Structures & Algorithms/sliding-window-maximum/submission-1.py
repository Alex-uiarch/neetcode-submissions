from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 0:
            return []
        
        cycles = len(nums) - k + 1
        left = 0
        right = k - 1
        maxNumbers = []
        dq = deque()

        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        maxNumbers.append(nums[dq[0]])

        

        for i in range(cycles - 1):
            left += 1
            right += 1
            

            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)
            
            while dq and dq[0] < left:
                dq.popleft()

            maxNumbers.append(nums[dq[0]])

            


            

            


            
            

        return maxNumbers
