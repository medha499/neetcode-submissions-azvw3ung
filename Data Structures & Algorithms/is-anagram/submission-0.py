class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        else: 
            first_s = {}
            second_t = {}

            for i in s:
                first_s[i] = first_s.get(i, 0) + 1
            
            for j in t:
                second_t[j] = second_t.get(j, 0) + 1
        
        return first_s == second_t






        