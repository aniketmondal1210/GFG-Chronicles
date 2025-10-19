class Solution:
    def countFactors (self, n):
        # code here
        factors = []
        for i in range(1,int(n**0.5)+1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        return len(factors)
