import math
class Solution:
    def addFraction(self, num1: int, den1: int, num2: int, den2: int) -> list[int]:
        # code hereclass Solution:
        num = num1 * den2 + num2 * den1
        den = den1 * den2
        g = math.gcd(num, den)
        return [num // g, den // g]
