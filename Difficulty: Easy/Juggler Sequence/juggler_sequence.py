"""
n: int
return: list of int
"""
class Solution:
    def jugglerSequence(self, n):
        # Code here
        result = [n]
        while n != 1:
            if n % 2 == 0:
                n = int(n ** 0.5)
            else:
                n = int(n ** 1.5) 
            result.append(n)
        return result
