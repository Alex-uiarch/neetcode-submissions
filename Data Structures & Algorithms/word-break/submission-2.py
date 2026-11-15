class Solution:
    def __init__(self):
        self.memo = {}
    def dfs(self, s: str, index: int, dct: dict[str, int]) -> bool:
        if index == len(s):
            return True

        if index in self.memo:
            return self.memo[index]



        for x in dct:


            if (index + dct[x]) <= len(s):
               
                if s[index: index + dct[x]] == x:

                    result = self.dfs(s, index + dct[x], dct)
                    if result:
                        self.memo[index] = True
                        return True

        self.memo[index] = False
        return False



            
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dct = {}
        for x in wordDict:
            dct[x] = len(x)

        unswer = self.dfs(s, 0, dct)
        self.memo = {}
        return unswer