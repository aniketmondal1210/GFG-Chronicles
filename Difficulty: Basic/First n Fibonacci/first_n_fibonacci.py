#User function Template for python3
class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        result = [0,1]
        a = result[0]
        b = result[1]
        for i in range(n-2):
            a,b = b,a+b
            result.append(b)
        return result[:n]
