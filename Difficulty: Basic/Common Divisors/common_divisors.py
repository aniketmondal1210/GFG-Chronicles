#User function Template for python3
class Solution:
    def commDiv (self, a, b):
        # code here 
        count = 0
        for i in range(1,a+1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count
