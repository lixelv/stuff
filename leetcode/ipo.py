from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        benefit = [(profits[i] - capital[i], capital[i]) for i in range(len(profits))]
        benefit.sort(key=lambda x: x[0])
        
        while k > 0:
            if be
