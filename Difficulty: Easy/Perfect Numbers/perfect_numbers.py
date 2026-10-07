class Solution:
    def isPerfect(self, n):
        # code here 
        if n <= 1:
            return False
        summ = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                summ += i
                if i != n // i:
                    summ += n // i
        return summ == n
