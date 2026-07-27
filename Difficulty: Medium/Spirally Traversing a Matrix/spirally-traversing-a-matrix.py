class Solution:
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:
            return []
        
        n = len(mat)
        m = len(mat[0])
        
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        result = []
        
        while top <= bottom and left <= right:
            # 1. Traverse Left to Right
            for j in range(left, right + 1):
                result.append(mat[top][j])
            top += 1
            
            # 2. Traverse Top to Bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            # 3. Traverse Right to Left (if a row remains)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(mat[bottom][j])
                bottom -= 1
                
            # 4. Traverse Bottom to Top (if a column remains)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
                
        return result