class Solution:
	def matSearch(self, mat, x):
		# code here
		rows=len(mat)
		cols=len(mat[0])
		
		for i in range(rows):
		    for j in range(cols):
		        if mat[i][j]==x:
		            return True
		return False