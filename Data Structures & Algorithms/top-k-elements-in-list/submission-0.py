class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        values = {}
        for i in nums: 
            values[i] = values.get(i, 0) + 1 ##frequency count 
            top_k =sorted(values, key=values.get, reverse=True)[:k]
        return top_k
        