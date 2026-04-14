class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n      # default = 0 days
        stack = []            # will store INDICES of days

        for i in range(n):
        # While current temp is warmer than temp at stack top index
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            stack.append(i)

        return result
        