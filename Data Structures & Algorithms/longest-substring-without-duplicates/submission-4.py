class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        c = set()

        left = 0

        for i in range(len(s)):            
            while s[i] in c:
                c.remove(s[left])
                left+=1
            c.add(s[i])
            max_length = max(max_length, i - left + 1)
            
            
        
                        
        return max_length