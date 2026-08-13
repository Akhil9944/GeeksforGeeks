class Solution:
    def isPalinArray(self, arr):
         # code here
         return all(str(num)==str(num)[::-1] for num in arr)