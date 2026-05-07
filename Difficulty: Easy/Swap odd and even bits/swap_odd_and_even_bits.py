class Solution:
    def swapBits(self, n):
        #code here
        a = bin(n)[2:].zfill(32)
        bits = list(a)
        for i in range(0, 32, 2):
            bits[i], bits[i+1] = bits[i+1], bits[i]
        result = "".join(bits)
        return int(result, 2)
