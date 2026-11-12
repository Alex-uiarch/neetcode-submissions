class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        if len(s) < 2:
            return 1

        dp = [0] * (len(s) + 1)

        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):

            dp[i] = (dp[i - 1] if int(s[i - 1]) != 0 else 0) + (dp[i - 2] if int(s[i - 2:i]) <= 26 and  int(s[i - 2:i]) >= 10 else 0)



        return dp[-1]


