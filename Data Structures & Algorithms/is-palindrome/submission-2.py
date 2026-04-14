class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_chars = []
        for char in s:
            if char.isalnum():
                clean_chars.append(char.lower())

            clean = "".join(clean_chars)

            rev = "".join(reversed(clean))

        return clean == rev
        
        

        
        