class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1] * n, [1] * n

        left_product = 1
        for i in range(n):
            left[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            right[i] *= right_product
            right_product *= nums[i]

        return [x*y for x, y in zip(left, right)]

