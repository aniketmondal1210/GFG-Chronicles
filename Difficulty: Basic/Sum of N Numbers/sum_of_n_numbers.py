class Solution:
    def sumoffirstn(self, n: int) -> int:
        #code here 
        sum = 0
        for i in range(1,n+1):
            sum += i
        return sum


OR


class Solution:
    def sumOfNumbers(self, n):
        # code here
        return n*(n+1)//2
