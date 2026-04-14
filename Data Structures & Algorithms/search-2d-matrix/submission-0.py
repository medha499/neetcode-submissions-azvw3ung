class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r: 
            for i in matrix: 
                if target in i: 
                    return True 
                elif i[-1] < target: 
                    l +=1
                r -= 1
            
        return False

        