class Solution:
    def totalDigits(self,n):
        # code here 
        summ = 0
        for i in range(1, n + 1):
            summ += len(str(i))
        return summ
