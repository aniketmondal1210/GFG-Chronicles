class Solution:
    def sumoffirstn(self, n: int) -> int:
        #code here 
        sum = 0
        for i in range(1,n+1):
            sum += i
        return sum
