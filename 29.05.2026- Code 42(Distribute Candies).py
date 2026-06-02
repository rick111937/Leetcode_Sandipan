from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_allowed = len(candyType) // 2
        unique_types = len(set(candyType))
        return min(unique_types, max_allowed)
