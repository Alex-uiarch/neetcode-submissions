class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            summ = 0

            for x in piles:
                c = x // mid
                s = x % mid
                if s != 0:
                    c += 1
                summ += c
            if summ > h:
                left = mid + 1
            else:
                right = mid
        return left
