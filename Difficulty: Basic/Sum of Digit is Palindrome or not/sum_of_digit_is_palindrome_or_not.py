#User function Template for python3
class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        sum = 0
        for i in str(n):
            sum += int(i)
        return str(sum)[::-1] == str(sum)
