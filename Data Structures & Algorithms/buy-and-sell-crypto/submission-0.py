class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maiordiferenca = 0
        tam = len(prices)

        for i in range(tam):
            for j in range(i, tam):
                 dif = prices[j] - prices[i]

                 if dif > maiordiferenca:
                    maiordiferenca = dif

        return maiordiferenca