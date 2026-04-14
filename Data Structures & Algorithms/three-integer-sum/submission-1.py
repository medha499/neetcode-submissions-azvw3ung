class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        finalL = []
        for i in range(len(nums)- 2): 
            a = nums[i]
        # Skip duplicates to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r: 
                total = a + nums[l] + nums[r]
                if total == 0: 
                    finalL.append([a, nums[l], nums[r]])
                # Move pointers and skip duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1   # need smaller sum

        return finalL
