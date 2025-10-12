#User function Template for python3
class Solution:
    def segregateElements(self, arr):
        # Your code goes here
        pos = []
        neg = []
        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        arr[:] = pos + neg
        return arr
