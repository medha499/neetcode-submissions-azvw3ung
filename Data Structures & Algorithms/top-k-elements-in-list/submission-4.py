class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterD = {}
        for i in nums: 
            counterD[i] = counterD.get(i, 0) + 1
        new_Str = sorted(counterD, key=lambda x: counterD[x], reverse=True)
        return new_Str[0:k]     