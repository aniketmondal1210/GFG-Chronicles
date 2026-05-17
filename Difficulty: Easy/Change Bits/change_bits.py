#User function Template for python3
class Solution:
    def changeBits(self, N):
        # code here 
        a = bin(N)[2:]
        new_a = a.replace('0', '1')
        new_number = int(new_a, 2)
        diff = new_number - N
        return [diff, new_number]
