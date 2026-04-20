class Solution:
    def countBitsFlip(self, a, b):
        #code here
        max_len = max(len(bin(a)[2:]), len(bin(b)[2:]))
        c = bin(a)[2:].zfill(max_len)
        d = bin(b)[2:].zfill(max_len)
        count = 0
        for i in range(len(c)):
            if c[i] != d[i]:
                count += 1
        return count
