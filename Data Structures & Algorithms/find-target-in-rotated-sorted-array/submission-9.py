class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        """if len(nums) < 4:
            if target in nums:
                return nums.index(target)
            else:
                return -1"""

        


        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        #print(mid)

        minimum = left
        left = 0
        right = len(nums) - 1

        if nums[right] > target:
            left = minimum
        elif nums[right] < target:
            right = minimum - 1
        else:
            return right




        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                return mid
            


        return -1



