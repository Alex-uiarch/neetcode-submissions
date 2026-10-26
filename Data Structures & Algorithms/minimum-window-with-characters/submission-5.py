
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        dct = {}
        for x in t:
            dct[x] = dct.get(x, 0) + 1

        window = {}
        left = 0
        right = 0

        formed = 0
        required = len(dct)

        bestStart = 0
        bestLen = float('inf')

        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in dct and window[char] == dct[char]:
                formed += 1

            right += 1

            while formed == required:
                if right - left < bestLen:
                    bestStart = left
                    bestLen = right - left

                char = s[left]
                window[char] -= 1

                if char in dct and window[char] < dct[char]:
                    formed -= 1

                left += 1

        if bestLen == float('inf'):
            return ''

        return s[bestStart:bestStart + bestLen]
