class Solution:
    def transpose(self, mat):
        # code here
        rows=len(mat)
        cols=len(mat[0])
        
        res=[[0]*rows for i in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                res[j][i]=mat[i][j]
        return res