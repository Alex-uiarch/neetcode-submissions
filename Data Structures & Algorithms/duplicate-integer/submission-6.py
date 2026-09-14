import json
class Solution:
    
    def hasDuplicate(self, n):
        g = set()

        for x in n:
            if x in g:
                return True
            else:
                g.add(x)
        return False
        

