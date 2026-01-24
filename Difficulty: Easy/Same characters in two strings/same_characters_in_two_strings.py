#User function Template for python3
class Solution:
    def sameChar(self, A, B):
        # code here
        count = 0
        for i in range(len(A)):
            if A[i].lower() != B[i].lower():
                count += 1
        return len(A) - count
