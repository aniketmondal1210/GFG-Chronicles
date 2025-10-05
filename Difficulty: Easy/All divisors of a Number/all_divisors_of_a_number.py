#User function Template for python3
class Solution:
    def print_divisors(self, N):
        divisors = set()
        i = 1
        while i * i <= N:
            if N % i == 0:
                divisors.add(i)
                divisors.add(N // i)
            i += 1
        
        for d in sorted(divisors):
            print(d, end=" ")
