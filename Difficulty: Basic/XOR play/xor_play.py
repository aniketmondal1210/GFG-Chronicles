#User function Template for python3
class Solution:
    def xor_play(self, n):
        # code here
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i != n:
                    divisors.append(i)
                if i != n // i and n // i != n:
                    divisors.append(n // i)

        divisors.sort()

        xor_result = 0
        for d in divisors:
            xor_result ^= d
            
        return *divisors, xor_result
