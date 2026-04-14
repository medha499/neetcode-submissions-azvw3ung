class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:  # Change i to s to represent the string being processed
            res += str(len(s)) + "#" + s  # Changed rest to res and fixed concatenation
        return res



    def decode(self, s: str) -> List[str]:
        res, i = [], 0 
        ###print(len(string))
        while i < len(s): 
            j = i
            while s[j] != "#": 
                j += 1 
            length = int(s[i:j])  # This correctly extracts the number

            res.append(s[j+1:j+1+length])  # Changed str to string for correct access
            i = j + 1 + length  # Update index to the next part of the string
        
        return res  # Add return statement to return the decoded list

