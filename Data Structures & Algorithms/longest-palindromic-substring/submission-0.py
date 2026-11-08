class Solution:
    def longestPalindrome(self, s: str) -> str:
        ln = len(s)





        max_len = 1
        start = 0

        dp = [[0] * ln for i in range(ln)]
        for i in range(ln):
            dp[i][i] = 1

        for i in range(ln - 1):
            j = i + 1
            if  s[i] == s[j]:
                dp[i][j] = 1
                if j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1


        for length in range(3, ln + 1):
            for i in range(ln - length + 1):
                j = length + i - 1
                if s[i] == s[j] and  dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1

                    if j - i + 1 > max_len:
                        start = i
                        max_len = j - i + 1




        
                

        return s[start: start + max_len]



