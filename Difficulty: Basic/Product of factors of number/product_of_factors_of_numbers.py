#User function Template for python3
class Solution:
    def factorProduct(self, N):
        result = []
        for i in range(1, int(N**0.5) + 1):
            if N % i == 0:
                result.append(i)
                if i != N // i:
                    result.append(N // i)
        mul = 1
        for j in result:
            mul *= j
        return mul%(10**9+7)
