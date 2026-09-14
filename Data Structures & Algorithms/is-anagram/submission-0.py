class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = sorted([x for x in s]), sorted([x for x in t])
        
        if t == s:
            return True
        else: 
            return False
        

