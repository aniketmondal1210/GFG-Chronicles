import math
class Solution:
    def primorial(self, n):
        # code here
        result = []
        for i in range(1,n+1):
            if self.is_prime(i):
                result.append(i)
        return math.prod(result)
        
    def is_prime(self,n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
