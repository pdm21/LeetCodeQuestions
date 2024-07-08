class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_alltime = float('inf')
        max_alltime = float('-inf')
        
        for p in prices:
            max_profit_td = p - min_alltime
            max_alltime = max(max_profit_td, max_alltime)
            min_alltime = min(p, min_alltime)
            
        return max(0, max_alltime)