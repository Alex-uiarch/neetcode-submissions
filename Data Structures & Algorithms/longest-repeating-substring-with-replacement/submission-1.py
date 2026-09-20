class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}

        for x in s:

            if x not in counts:
                counts[x] = 1
            else:
                counts[x] += 1

        if (len(s) - max(counts.values())) <= k:
            return len(s)


        left = 0
        counts = {}
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
            
            while ((right - left + 1) - max(counts.values())) > k:
                counts[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length