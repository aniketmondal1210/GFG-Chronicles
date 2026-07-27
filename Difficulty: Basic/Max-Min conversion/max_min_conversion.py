class Solution:
    def findSum(self, n):
        """ code here """
        s = str(n)
        maxi = int(s.replace('5', '6'))
        mini = int(s.replace('6', '5'))
        return maxi + mini
