#User function Template for python3
class Solution:
    def xorGate (self, arr, N):
        #code here
        result = 0
        for i in arr:
            result ^= i
        return result
