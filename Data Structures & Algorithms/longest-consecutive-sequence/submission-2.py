class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)

        current_len = 1      # length of current streak
        max_len = 1          # longest streak seen so far

        for i in range(len(nums) - 1):

            if nums[i] == nums[i + 1]:
                continue     # skip duplicates

        # check for consecutive
            if nums[i + 1] == nums[i] + 1:
                current_len += 1
            else:
                current_len = 1   # reset when streak breaks

            max_len = max(max_len, current_len)

        return max_len