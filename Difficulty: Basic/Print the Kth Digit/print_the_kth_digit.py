#User function Template for python3
class Solution:
    def kthDigit(self, a, b, k):
        # code here
        z = str(a**b)
        return int(z[-k])
