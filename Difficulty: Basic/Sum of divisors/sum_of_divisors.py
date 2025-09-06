#User function Template for python3
class Solution:
    def divSum (self, n):
        # code here
        result = []
        for i in range(1,int(n**0.5)+1):
            if n % i == 0:
                result.append(i)
                if i != (n//i):
                    result.append(n//i)
        return sum(result) - n
