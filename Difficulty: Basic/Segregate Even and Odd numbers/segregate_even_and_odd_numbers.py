#User function Template for python3
class Solution:
    def segregateEvenOdd(self,arr):
        # code here
        odd = []
        even = []
        for i in arr:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        even.sort()
        odd.sort()
        arr[:] = even + odd
        return arr
