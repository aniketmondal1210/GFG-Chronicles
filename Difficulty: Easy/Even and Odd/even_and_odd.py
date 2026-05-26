#User function Template for python3
class Solution:
    def reArrange(self, arr, N):
        # code here
        evens = []
        odds = []
        for i in arr:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        even_idx = 0
        odd_idx = 0
        for i in range(N):
            if i % 2 == 0:
                arr[i] = evens[even_idx]
                even_idx += 1
            else:
                arr[i] = odds[odd_idx]
                odd_idx += 1
        return arr
