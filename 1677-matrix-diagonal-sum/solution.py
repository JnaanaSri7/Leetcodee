class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        s=0
        j=n-1
        for i in range(n):
            if(i!=j):
                s=s+mat[i][i]+mat[i][j]
            else:
                s=s+mat[i][i]
            j=j-1
        return s
        
