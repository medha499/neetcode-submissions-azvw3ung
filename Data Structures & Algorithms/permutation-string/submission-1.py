class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        len_s1 = len(s1)

    # Iterate over substrings of s2 with the same length as s1
        for i in range(len(s2) - len_s1 + 1):
        # Check if the sorted substring is equal to sorted s1
            if sorted(s2[i:i+len_s1]) == sorted_s1:
                return True

        return False