class Solution:
    def maximumSum(self, mat: list[list[int]], k: int) -> int:
        n = len(mat)
        
        # Step 1: Create a 2D Prefix Sum array of size (n + 1) x (n + 1)
        # pref[i][j] stores the sum of sub-matrix from (0,0) to (i-1, j-1)
        pref = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                pref[i][j] = (
                    mat[i - 1][j - 1] 
                    + pref[i - 1][j] 
                    + pref[i][j - 1] 
                    - pref[i - 1][j - 1]
                )
        
        max_sum = float('-inf')
        
        # Step 2 & 3: Iterate through all possible k x k sub-grids using pref
        for i in range(k, n + 1):
            for j in range(k, n + 1):
                current_sum = (
                    pref[i][j] 
                    - pref[i - k][j] 
                    - pref[i][j - k] 
                    + pref[i - k][j - k]
                )
                max_sum = max(max_sum, current_sum)
                
        return max_sum