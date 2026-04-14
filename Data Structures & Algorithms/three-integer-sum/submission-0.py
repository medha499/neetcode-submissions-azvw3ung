class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        n = len(nums)
        for i in range(n):
            seen = set()          # for the Two Sum part
            target = -nums[i]

            for j in range(i + 1, n):
                complement = target - nums[j]

                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    res.add(triplet)   # set removes duplicates automatically

                seen.add(nums[j])

        return [list(t) for t in res]