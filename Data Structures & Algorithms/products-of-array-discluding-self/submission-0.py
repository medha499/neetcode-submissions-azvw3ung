class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        visited = deque()

        # Work on a copy so we don't permanently change the original nums
        arr = nums[:]  

        for i in range(n):
            # 1) pop arr[i] and put into visited
            removed = arr.pop(i)
            visited.append(removed)

            # 2) compute product of remaining elements
            prod = 1
            for val in arr:
                prod *= val

            # 3) store in result[i]
            result[i] = prod

            # 4) restore array: take from visited and re-insert at i
            arr.insert(i, visited.popleft())

        return result
        