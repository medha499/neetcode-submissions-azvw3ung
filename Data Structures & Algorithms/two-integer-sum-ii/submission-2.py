class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Changed '1' to '0' to start from the first index
        while l < r: 
            if numbers[l] + numbers[r] == target: 
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:  # Check for correct condition
                l += 1
            else: 
                r -= 1
        return []

