class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        stack = nums[:]      # copy so we don't destroy original
        result = []

        for i in range(len(nums)):
            removed = stack.pop(i)   # take current element out

            product = 1
            for val in stack:        # multiply remaining elements
                product *= val

            result.append(product)

            stack.insert(i, removed)  # put it back in same spot

        return result


