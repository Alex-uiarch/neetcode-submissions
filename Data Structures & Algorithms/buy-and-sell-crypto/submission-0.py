class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        diff = 0
        sell = 0
        for i in range(1, len(prices)):
            if buy < prices[i] and ((prices[i] - buy) > diff):
                diff = (prices[i] - buy)

            if buy > prices[i]:
                buy = prices[i]


            # if buy > prices[i]:
            #     buy =  prices[i]
            #     sell = prices[i]
            # if (sell - prices[i]) > diff:
            #     diff = sell - prices[i]
            #     sell = prices[i]

            

        return diff

            
            
