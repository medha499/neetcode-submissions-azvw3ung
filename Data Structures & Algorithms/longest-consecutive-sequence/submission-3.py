class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:  # edge case: empty list
            return 0
    
        nums = sorted(set(nums))  # remove duplicates and sort
        max_length = 1  # initialize max_length
        current_length = 1  # track the length of the current sequence
    
        for i in range(1, len(nums)):  # iterate over nums starting from the second element
            if nums[i] - nums[i-1] == 1:  # check if current number is consecutive to the previous one
                current_length += 1  # if yes, increment the current sequence length
            else:
                max_length = max(max_length, current_length)  # update max_length if necessary
                current_length = 1  # reset current_length
    
    # After the loop, update max_length one last time
        return max(max_length, current_length)