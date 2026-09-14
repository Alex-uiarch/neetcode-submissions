class Solution:
    def searchMatrix(self, nums: List[int], target: int) -> int:


        lst = []
        for x in nums:
            for y  in x:
                lst.append(y)

        left = 0
        right = len(lst) - 1

        while left <= right:
            mid = (left + right) // 2
            if lst[mid] > target:
                right = mid - 1
            elif lst[mid] < target:
                left = mid + 1
            else:
                return True

        return False
        
        
