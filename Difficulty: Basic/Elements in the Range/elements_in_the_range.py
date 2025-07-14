class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        flag = False
        for i in range(A,B+1):
            if i in arr:
                flag = True
            else:
                flag = False
                break
        return flag
