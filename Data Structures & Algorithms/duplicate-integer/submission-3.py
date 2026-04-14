class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for x in nums: 
            counts[x] = counts.get(x, 0) + 1
            if counts[x] > 1: 
                return True 
        return False
        