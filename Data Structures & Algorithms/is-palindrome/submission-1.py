class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_1 = []
        str_2 = []

        for i in s: 
            if i.isalnum():
                ch = i.lower()
                str_1.append(ch)
                str_2.insert(0, ch) # reversal - since it will add latest to the front 

        if str_1 == str_2: 
            return True 
        return False
        

