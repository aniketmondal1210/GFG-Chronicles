class Solution:
    def missingNumber(self, arr):
        # code here
        xor_arr = 0
        xor_all = 0
        for i in arr:
            xor_arr ^= i
        for j in range(1,len(arr)+2):
            xor_all ^= j
        return xor_all ^ xor_arr
